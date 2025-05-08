from flask import Flask, redirect
import jwt
import time
import uuid

app = Flask(__name__)

CLIENT_ID = "1499c554-9265-4588-90c1-dcb83c4e278e"
CLIENT_SECRET = "eVqar2097azOCWfqbEHJdnircKh17dfUGD1BerITVMO=" 
EMAIL = "raiimad61@gmail.com"

TABLEAU_URL = (
    "https://prod-uk-a.online.tableau.com/t/raiimad61-4fe048d515/views/Book22/Dashboard1"
)

@app.route("/")
def generate_token_and_redirect():
    payload = {
        "iss": CLIENT_ID,
        "sub": EMAIL,
        "aud": "tableau",
        "scp": ["tableau:views:embed"],
        "exp": int(time.time()) + 600, 
        "jti": str(uuid.uuid4())
    }

    token = jwt.encode(payload, CLIENT_SECRET, algorithm="HS256")

    final_url = f"{TABLEAU_URL}?embed=yes&token={token}"
    return redirect(final_url, code=302)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
