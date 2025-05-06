from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/tableau-token", methods=["GET"])
def get_token():
    try:
        token_name = request.args.get("token_name")
        token_secret = request.args.get("token_secret")

        if not token_name or not token_secret:
            return jsonify({"error": "Missing token_name or token_secret"}), 400

        payload = {
            "credentials": {
                "personalAccessTokenName": token_name,
                "personalAccessTokenSecret": token_secret,
                "site": { "contentUrl": "raiimad61-4fe048d515" }
            }
        }

        headers = { "Content-Type": "application/json" }

        # ✅ URL correcte avec ton pod Tableau Cloud
        url = "https://prod-uk-a.online.tableau.com/api/3.25/auth/signin"

        response = requests.post(url, json=payload, headers=headers)
        print("🔁 Tableau response:", response.text)

        response.raise_for_status()
        return jsonify(response.json())

    except Exception as e:
        print("❌ Erreur :", e)
        return jsonify({"error": "Internal error", "details": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
