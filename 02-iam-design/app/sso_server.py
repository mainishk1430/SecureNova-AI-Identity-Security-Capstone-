import os
from dotenv import load_dotenv
from flask import Flask, redirect, session, url_for, jsonify
from authlib.integrations.flask_client import OAuth

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")
domain = os.getenv("AUTH0_DOMAIN")

oauth = OAuth(app)
oauth.register(
    name="auth0",
    client_id=os.getenv("SSO_CLIENT_ID"),
    client_secret=os.getenv("SSO_CLIENT_SECRET"),
    server_metadata_url=f"https://{domain}/.well-known/openid-configuration",
    client_kwargs={"scope": "openid profile email"},
)

@app.route("/")
def index():
    if "user" not in session:
        return '<a href="/login">Login with Auth0 SSO</a>'
    return jsonify({
        "message": "SSO login successful!",
        "user": session["user"]
    })

@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        "http://localhost:3001/callback"
    )

@app.route("/callback")
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token.get("userinfo", {})
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect("http://localhost:3001/")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3001, debug=False)
