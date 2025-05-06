import requests
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/tableau-token')
def tableau_token():
    token_name = request.args.get('token_name')
    token_secret = request.args.get('token_secret')
    content_url = "raiimad61-4fe048d515"  
    if request.args.get('content_url'):
        content_url = request.args.get('content_url')

    tableau_api_version = "3.25"
    tableau_pod_url = "https://prod-uk-a.online.tableau.com" 
    signin_url = f"{tableau_pod_url}/api/{tableau_api_version}/auth/signin"

    payload = {
        "credentials": {
            "personalAccessTokenName": token_name,
            "personalAccessTokenSecret": token_secret,
            "site": {
                "contentUrl": content_url
            }
        }
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(signin_url, json=payload, headers=headers)
        print("Tableau response status_code:", response.status_code, flush=True)
        print("Tableau response text:", response.text, flush=True)

        try:
            data = response.json()
            return Response(response.text, status=response.status_code, mimetype="application/json")
        except ValueError:
            return Response(response.text, status=response.status_code, content_type=response.headers.get('Content-Type', 'text/plain'))
    except Exception as e:
        print("Request to Tableau API failed:", e, flush=True)
        return {"error": "Internal error", "details": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
