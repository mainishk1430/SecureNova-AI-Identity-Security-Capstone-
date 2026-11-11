import os
import time
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
CLIENT_ID = os.getenv("M2M_CLIENT_ID")
CLIENT_SECRET = os.getenv("M2M_CLIENT_SECRET")
AUDIENCE = os.getenv("AUTH0_AUDIENCE")
BASE_URL = os.getenv("APP_BASE_URL", "http://localhost:3000")

def log(message):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")

def main():
    required = [AUTH0_DOMAIN, CLIENT_ID, CLIENT_SECRET, AUDIENCE]
    if not all(required):
        raise SystemExit("Missing M2M credentials in .env")

    token_url = f"https://{AUTH0_DOMAIN}/oauth/token"

    log("Requesting M2M access token...")
    response = requests.post(token_url, json={
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "audience": AUDIENCE,
        "grant_type": "client_credentials",
        "scope": "read:ai-data write:admin"
    }, timeout=20)

    response.raise_for_status()
    token_data = response.json()
    access_token = token_data["access_token"]
    expires_in = token_data.get("expires_in")

    log(f"Token received. expires_in={expires_in} seconds")

    chat_url = f"{BASE_URL}/chat"
    headers = {"Authorization": f"Bearer {access_token}"}

    log("Calling /chat with valid token...")
    result = requests.get(chat_url, headers=headers, timeout=20)
    log(f"Valid token response: {result.status_code} {result.text}")

    if expires_in is None or expires_in > 60:
        log("WARNING: Auth0 token lifetime is greater than 60 seconds.")
        log("Configure the API token lifetime to 60 seconds before the expiry test.")
        return

    log(f"Waiting {expires_in + 5} seconds for token expiry...")
    time.sleep(expires_in + 5)

    log("Replaying expired token...")
    replay = requests.get(chat_url, headers=headers, timeout=20)
    log(f"Expired token response: {replay.status_code} {replay.text}")

    if result.status_code == 200 and replay.status_code == 401:
        log("SUCCESS: Valid token accepted; expired token rejected.")
    else:
        log("CHECK FAILED: Expected 200 for valid token and 401 for expired token.")

if __name__ == "__main__":
    main()
