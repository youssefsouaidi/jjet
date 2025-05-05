from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)

@app.route("/tableau-token", methods=["GET"])
def get_token():
    try:
        payload = {
            "credentials": {
                "personalAccessTokenName": os.environ.get("TABLEAU_TOKEN_NAME"),
                "personalAccessTokenSecret": os.environ.get("TABLEAU_TOKEN_SECRET"),
                "site": { "contentUrl": "" }
            }
        }
        headers = { "Content-Type": "application/json" }
        response = requests.post("https://api.tableau.com/api/3.19/auth/signin", json=payload, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        print("❌ Erreur :", e)
        return jsonify({"error": "Internal error", "details": str(e)}), 500
