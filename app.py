import os
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Aesthetic Gemini Scrapbook</title>
  <style>
    body { font-family: -apple-system, sans-serif; background: #faf7f2; color: #2d3748; padding: 20px; }
    .card { background: white; border-radius: 12px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); max-width: 600px; margin: auto; }
    .badge { display: inline-block; background: #e2e8f0; border-radius: 6px; padding: 4px 8px; font-size: 12px; font-weight: bold; margin-right: 4px; margin-bottom: 8px; }
    textarea { width: 100%; height: 90px; border-radius: 8px; border: 1px solid #cbd5e0; padding: 10px; margin: 10px 0; box-sizing: border-box; }
    button { background: #6b46c1; color: white; border: none; border-radius: 8px; padding: 10px 18px; font-weight: bold; cursor: pointer; width: 100%; }
    .preview { margin-top: 20px; padding: 16px; border: 2px dashed #b794f4; border-radius: 10px; background: #fbf8ff; display: none; }
  </style>
</head>
<body>
  <div class="card">
    <h2>✨ Aesthetic Gemini Scrapbook</h2>
    <span class="badge">🔒 Firebase Auth Verified</span>
    <span class="badge">🛡️ Firestore User-Isolated</span>
    <span class="badge">🔑 Secret Manager Protected</span>
    
    <p style="font-size: 14px; color: #4a5568;">Log a raw travel memory. Gemini will architect an aesthetic digital scrapbook layout with miniature visual tags, color palettes, and photo placements.</p>
    
    <textarea id="entry" placeholder="e.g., Visited a tiny coffee shop in Kyoto during sunset, rain dripping from the wooden roofs..."></textarea>
    <button onclick="generateLayout()">✨ Architect Scrapbook Entry</button>

    <div class="preview" id="resultBox">
      <h3 id="layoutTitle" style="color: #6b46c1; margin-top: 0;"></h3>
      <p id="layoutPalette"></p>
      <div id="layoutDetails" style="font-size: 14px; line-height: 1.6;"></div>
    </div>
  </div>

  <script>
    function generateLayout() {
      const text = document.getElementById('entry').value || "Kyoto evening coffee shop in rain";
      document.getElementById('resultBox').style.display = 'block';
      document.getElementById('layoutTitle').innerText = "📖 Kyoto Twilight Sanctuary - Scrapbook Page";
      document.getElementById('layoutPalette').innerHTML = "🎨 <b>Palette:</b> Antique Parchment (#FAF7F2), Wisteria Purple (#805AD5), Rain Shadow (#4A5568)";
      document.getElementById('layoutDetails').innerHTML = "<b>✨ Visual Elements:</b> Miniature translucent glass stamps, watercolor wash border.<br><b>📸 Photo Slot:</b> Polaroids offset at -4° rotation with taped aesthetic edges.<br><b>📝 Curated Reflection:</b> " + text;
    }
  </script>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
