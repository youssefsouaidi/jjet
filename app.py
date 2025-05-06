from flask import Flask, jsonify
import jwt
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/generate-jwt", methods=["GET"])
def generate_jwt():
    secret = "eVqar2O97az0CWfqbEHJdnircKh17dfUGD1BerlTVM0="
    payload = {
        "iss": "1499c554-9265-4588-90c1-dcb83c4e278e",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
        "sub": "raiimad61@gmail.com"
    }
    token = jwt.encode(payload, secret, algorithm="HS256")
    return jsonify({"token": token})

if __name__ == "__main__":
    app.run()
