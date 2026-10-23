from pathlib import Path

from flask import Flask, abort, render_template, send_from_directory


ROOT = Path(__file__).resolve().parent
app = Flask(__name__, template_folder=str(ROOT), static_folder=None)


@app.get("/")
@app.get("/index.html")
def home():
    return render_template("index.html")


@app.get("/<path:filename>")
def website_files(filename):
    if filename in {"styles.css", "script.js", "robots.txt", "sitemap.xml"}:
        return send_from_directory(ROOT, filename)

    if filename.startswith("assets/"):
        asset_name = filename.removeprefix("assets/")
        return send_from_directory(ROOT / "assets", asset_name)

    abort(404)


if __name__ == "__main__":
    print("Hemitech Kenya is running at http://127.0.0.1:8000")
    app.run(host="127.0.0.1", port=8000)
