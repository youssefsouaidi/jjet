from flask import Flask, jsonify
import jwt
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/generate-jwt", methods=["GET"])
def generate_jwt():
    secret = "votre_clé_secrète"
    payload = {
        "iss": "your-client-id",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
        "sub": "user@email.com"
    }
    token = jwt.encode(payload, secret, algorithm="HS256")
    return jsonify({"token": token})

if __name__ == "__main__":
    app.run()
