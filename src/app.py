import os
import hashlib
from flask import Flask, request, jsonify, send_from_directory
from datetime import datetime
from db import get_connection

app = Flask(__name__)

UPLOAD_FOLDER = "storage"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def generate_checksum(filepath):
    with open(filepath, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

@app.route("/")
def home():
    return "Artifact Manager Running 🚀"

# ✅ Upload and store in DB
@app.route("/upload", methods=["POST"])
def upload_artifact():
    file = request.files["file"]
    version = request.form.get("version", "1.0")

    filename = file.filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    checksum = generate_checksum(filepath)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO artifacts (name, version, upload_time, checksum, file_path) VALUES (%s, %s, %s, %s, %s)",
        (filename, version, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), checksum, filepath)
    )

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Artifact uploaded successfully"})

# ✅ Fetch from DB
@app.route("/artifacts", methods=["GET"])
def list_artifacts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT name, version, upload_time FROM artifacts")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    artifacts = []
    for row in rows:
        artifacts.append({
            "name": row[0],
            "version": row[1],
            "upload_time": row[2]
        })

    return jsonify(artifacts)

@app.route("/download/<filename>", methods=["GET"])
def download_artifact(filename):
    file_path = os.path.join(os.getcwd(), "storage", filename)

    if os.path.exists(file_path):
        return send_from_directory(os.path.join(os.getcwd(), "storage"), filename, as_attachment=True)
    else:
        return {"error": "File not found"}, 404

@app.route("/health", methods=["GET"])
def health():
    return {"status": "healthy"}

@app.route("/ui")
def ui():
    return send_from_directory(os.path.join(os.getcwd(), "src/frontend"), "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))