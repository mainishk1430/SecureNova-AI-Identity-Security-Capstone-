
import os
from functools import wraps
from urllib.parse import urlencode

import jwt
from jwt import PyJWKClient

from dotenv import load_dotenv
from flask import (
Flask, abort, jsonify, redirect,
render_template, session, url_for, request
)
from authlib.integrations.flask_client import OAuth

load_dotenv()

app = Flask(__name__)

app.config.update(
SECRET_KEY=os.environ["FLASK_SECRET_KEY"],
SESSION_COOKIE_HTTPONLY=True,
SESSION_COOKIE_SAMESITE="Lax",
SESSION_COOKIE_SECURE=False,  # Localhost development only
)

domain = os.environ["AUTH0_DOMAIN"].strip().rstrip("/")
client_id = os.environ["AUTH0_CLIENT_ID"]
client_secret = os.environ["AUTH0_CLIENT_SECRET"]
audience = os.environ["AUTH0_AUDIENCE"]

# Auth0 JWT validation configuration
issuer = f"https://{domain}/"
jwks_client = PyJWKClient(f"{issuer}.well-known/jwks.json")


def verify_m2m_token():
auth_header = request.headers.get("Authorization", "")

if not auth_header.startswith("Bearer "):
abort(401, description="Missing Bearer token")

token = auth_header.split(" ", 1)[1]

try:
signing_key = jwks_client.get_signing_key_from_jwt(token)

claims = jwt.decode(
token,
signing_key.key,
algorithms=["RS256"],
audience=audience,
issuer=issuer,
)

if "read:ai-data" not in claims.get("scope", "").split():
abort(403, description="Missing read:ai-data permission")

return claims

except jwt.ExpiredSignatureError:
abort(401, description="Token expired")

except (jwt.InvalidTokenError, jwt.PyJWKClientError):
abort(401, description="Invalid token")


oauth = OAuth(app)

oauth.register(
name="auth0",
client_id=client_id,
client_secret=client_secret,
server_metadata_url=f"https://{domain}/.well-known/openid-configuration",
client_kwargs={
"scope": "openid profile email read:ai-data",
"code_challenge_method": "S256",
},
authorize_params={
"audience": audience,
},
)


def login_required(view):
@wraps(view)
def wrapped(*args, **kwargs):
if "user" not in session:
return redirect(url_for("login"))
return view(*args, **kwargs)
return wrapped


def has_scope(required_scope):
granted = session.get("scope", "").split()
return required_scope in granted


@app.route("/")
def index():
return render_template(
"index.html",
user=session.get("user"),
)


@app.route("/login")
def login():
redirect_uri = url_for("callback", _external=True)
return oauth.auth0.authorize_redirect(redirect_uri)


@app.route("/callback")
def callback():
token = oauth.auth0.authorize_access_token()

userinfo = token.get("userinfo", {})

session.clear()
session["user"] = userinfo
session["access_token"] = token["access_token"]
session["scope"] = token.get("scope", "")
session["id_token"] = token.get("id_token")

id_token_claims = jwt.decode(
token["id_token"],
options={"verify_signature": False}
)
return redirect(url_for("index"))


# M2M-protected API endpoint
@app.route("/chat", methods=["GET"])
def chat():
claims = verify_m2m_token()

return jsonify({
"message": "Authenticated M2M access to AI data successful.",
"client_id": claims.get("azp"),
"scope": claims.get("scope"),
}), 200


# User-session-protected admin endpoint
@app.route("/admin")
@login_required
def admin():
if not has_scope("write:admin"):
abort(403, description="Missing write:admin permission")

return jsonify({"message": "Admin access granted."})


@app.route("/logout")
def logout():
session.clear()

params = urlencode({
"client_id": client_id,
"returnTo": os.environ["APP_BASE_URL"],
})

return redirect(f"https://{domain}/v2/logout?{params}")


@app.errorhandler(401)
def unauthorized(error):
return jsonify({
"error": "unauthorized",
"message": error.description,
}), 401


@app.errorhandler(403)
def forbidden(error):
return jsonify({
"error": "forbidden",
"message": error.description,
}), 403


if __name__ == "__main__":
app.run(host="127.0.0.1", port=3000, debug=False)
