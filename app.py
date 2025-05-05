import os
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/tableau-token", methods=["GET"])
def get_token():
    token_name = os.environ.get("TABLEAU_TOKEN_NAME")
    token_secret = os.environ.get("TABLEAU_TOKEN_SECRET")

    url = "https://api.tableau.com/api/3.19/auth/signin"
    payload = {
        "credentials": {
            "personalAccessTokenName": token_name,
            "personalAccessTokenSecret": token_secret,
            "site": { "contentUrl": "" }
        }
    }
    headers = { "Content-Type": "application/json" }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500
