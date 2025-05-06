from flask import Flask, jsonify
import jwt
import datetime
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Configuration — à remplacer par tes vraies infos
CLIENT_ID = "1499c554-9265-4588-90c1-dcb83c4e278e"
SECRET = "eVqar2O97az0CWfqbEHJdnircKh17dfUGD1BerlTVM0"
ISSUER = CLIENT_ID  # en général, c’est le client_id
AUDIENCE = "https://prod-uk-a.online.tableau.com"

@app.route("/generate-jwt", methods=["GET"])
def generate_jwt():
    try:
        now = datetime.datetime.utcnow()
        payload = {
            "iss": ISSUER,
            "aud": AUDIENCE,
            "sub": "apex.oracle.com",  # domain autorisé
            "exp": now + datetime.timedelta(minutes=15),
            "iat": now,
            "jti": os.urandom(16).hex(),
        }

        token = jwt.encode(payload, SECRET, algorithm="HS256")

        return jsonify({
            "token": token,
            "exp": payload["exp"].isoformat()
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
