import os
import logging
from flask import Flask, request, jsonify
import requests

# ---------------- CONFIG ---------------- #

app = Flask(__name__)

PORT = int(os.environ.get("PORT", 3000))
BASE_URL = os.environ.get("BASE_URL", "")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# Reusable fast session (IMPORTANT FOR RENDER)
session = requests.Session()
session.headers.update({
    "User-Agent": "Render-Optimized-API/1.0"
})

TIMEOUT = 15


# ---------------- ROUTES ---------------- #

@app.route("/")
def home():
    return jsonify({
        "status": "running",
        "service": "GEN API",
        "deploy": "render"
    })


@app.route("/health")
def health():
    return "OK", 200


@app.route("/gen")
def generate():

    name = request.args.get("name")
    count = request.args.get("count", "1")
    region = request.args.get("region", "IND")

    if not name:
        return jsonify({
            "error": "Missing parameter: name"
        }), 400

    try:
        # Example external logic (edit if needed)
        result = {
            "name": name,
            "count": int(count),
            "region": region,
            "status": "success"
        }

        logging.info(f"GEN Request → {result}")

        return jsonify(result)

    except Exception as e:
        logging.error(str(e))
        return jsonify({
            "error": "internal_server_error",
            "message": str(e)
        }), 500


# ---------------- START SERVER ---------------- #

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)