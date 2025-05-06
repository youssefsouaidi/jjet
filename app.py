import requests
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/tableau-token')
def tableau_token():
    # Get query parameters
    token_name = request.args.get('token_name')
    token_secret = request.args.get('token_secret')
    content_url = "raiimad61-4fe048d515"  # Default to empty string (default site)
    # If a contentUrl is needed for a specific site, it can be provided as an optional parameter
    if request.args.get('content_url'):
        content_url = request.args.get('content_url')

    # Tableau Cloud API endpoint (use the correct pod URL and API version)
    tableau_api_version = "3.25"
    tableau_pod_url = "https://prod-uk-a.online.tableau.com"  # Example pod URL, adjust if needed
    signin_url = f"{tableau_pod_url}/api/{tableau_api_version}/auth/signin"

    # Prepare the PAT sign-in payload
    payload = {
        "credentials": {
            "personalAccessTokenName": token_name,
            "personalAccessTokenSecret": token_secret,
            "site": {
                "contentUrl": content_url
            }
        }
    }

    # Set headers for JSON request/response
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    try:
        # Make the sign-in request to Tableau Cloud
        response = requests.post(signin_url, json=payload, headers=headers)
        # Log the status code and response text for debugging
        print("Tableau response status_code:", response.status_code, flush=True)
        print("Tableau response text:", response.text, flush=True)

        # Try to parse the response as JSON
        try:
            data = response.json()
            # If parsing succeeds, return the JSON content with the same HTTP status
            return Response(response.text, status=response.status_code, mimetype="application/json")
        except ValueError:
            # If JSON parsing fails, return the raw text with the same HTTP status
            return Response(response.text, status=response.status_code, content_type=response.headers.get('Content-Type', 'text/plain'))
    except Exception as e:
        # Log any exception that occurred during the request
        print("Request to Tableau API failed:", e, flush=True)
        # Return a generic internal error with details
        return {"error": "Internal error", "details": str(e)}, 500

if __name__ == "__main__":
    # Run the Flask app (for local testing or development)
    app.run(host="0.0.0.0", port=10000)
