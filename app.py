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
                "site": {
                    "contentUrl": "raiimad61-4fe048d515" 
                }
            }
        }

        headers = { "Content-Type": "application/json" }

        url = "https://prod-uk-a.online.tableau.com/api/3.25/auth/signin"

        response = requests.post(url, json=payload, headers=headers)

        print("Payload envoyé :", payload)
        print("Code HTTP :", response.status_code)
        print("Réponse brute :", repr(response.text))  

        if response.status_code != 200:
            return jsonify({
                "error": "Request failed",
                "status_code": response.status_code,
                "response": response.text
            }), response.status_code

        if not response.text.strip():
            return jsonify({
                "error": "Empty response from Tableau API",
                "status_code": response.status_code
            }), 500

        return jsonify(response.json())

    except Exception as e:
        print(" Erreur :", str(e))
        return jsonify({"error": "Internal error", "details": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
