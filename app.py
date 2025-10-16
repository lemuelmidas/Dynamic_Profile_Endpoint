from flask import Flask, jsonify
import requests
from datetime import datetime, timezone
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome! Try /me endpoint 🚀"


# Basic config (optional env vars)
USER_EMAIL = os.getenv("USER_EMAIL", "simplecoder@gmail.com")
USER_NAME = os.getenv("USER_NAME", "Simple coder")
USER_STACK = os.getenv("USER_STACK", "Python/Flask")

CAT_FACT_API = "https://catfact.ninja/fact"

@app.route("/me", methods=["GET"])
def get_profile():
    try:
        # Fetch cat fact
        response = requests.get(CAT_FACT_API, timeout=5)
        response.raise_for_status()
        cat_data = response.json()
        cat_fact = cat_data.get("fact", "Cats are mysterious creatures!")
    except Exception as e:
        # Fallback message if API fails
        cat_fact = "Could not fetch cat fact at this time."

    # Build response
    data = {
        "status": "success",
        "user": {
            "email": USER_EMAIL,
            "name": USER_NAME,
            "stack": USER_STACK
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return jsonify(data), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
