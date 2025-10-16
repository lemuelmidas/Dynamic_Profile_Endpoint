from flask import Flask, jsonify
import requests
from datetime import datetime, timezone
import os

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return '''
    <h2>Welcome! 👋</h2>
    <p>This is your Stage 0 Backend Task API.</p>
    <p>Visit your endpoint here 👉 
        <a href="/me" target="_blank">/me</a>
    </p>
    '''

# /me route
@app.route("/me", methods=["GET"])
def get_profile():
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        cat_data = response.json()
        cat_fact = cat_data.get("fact", "Cats are mysterious creatures!")
    except Exception:
        cat_fact = "Could not fetch cat fact at this time."

    data = {
        "status": "success",
        "user": {
            "email": "simplecoder@gmail.com",
            "name": "Simple Coder",
            "stack": "Python/Flask"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)
