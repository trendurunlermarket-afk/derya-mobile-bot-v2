from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def home():
    return "Derya Mobile Bot v2 is running 💚"

@app.get("/healthz")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
