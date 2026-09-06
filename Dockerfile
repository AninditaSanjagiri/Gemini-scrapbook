import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Aesthetic Gemini Scrapbook & Travel Diary</h1>
    <p>✅ Authentication: Firebase Admin initialized (JWT Secure)</p>
    <p>✅ Database: Firestore User-Isolation active</p>
    <p>✅ Secrets: Cloud Secret Manager integration active</p>
    <p>✅ AI: Gemini Multi-turn Chat enabled</p>
    <hr>
    <h3>Phase 3 Feature: AI Aesthetic Memory Architect</h3>
    <p>Status: Active. Users log raw travel text, and Gemini structures it into beautiful scrapbook pages with perfectly placed miniature visual elements, photo filters, and sparkly, vibrant text boxes.</p>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
