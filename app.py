from flask import Flask, jsonify
import jwt
import datetime
import os

app = Flask(__name__)

# Configuration — à remplacer par tes vraies infos
CLIENT_ID = "6d122907-3991-45f7-bbb5-b574e4349c76"
SECRET = "obR/uxRNrS5dl6lOSmcq/ugHQgoi+DezI+qSr07+mHA="
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
