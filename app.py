from flask import Flask, jsonify
import jwt
import uuid
import datetime
from creds import CLIENT_ID, CLIENT_SECRET_ID, CLIENT_SECRET_KEY, SITE, USER_EMAIL

app = Flask(__name__)

@app.route('/get-token', methods=['GET'])
def get_token():
    payload = {
        "iss": CLIENT_ID,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
        "jti": str(uuid.uuid4()),
        "aud": "tableau",
        "sub": USER_EMAIL,
        "scp": ["tableau:views:embed", "tableau:content:read"]
    }

    headers = {
        "kid": CLIENT_SECRET_ID
    }

    token = jwt.encode(payload, CLIENT_SECRET_KEY, algorithm="HS256", headers=headers)

    return jsonify({"token": token})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
