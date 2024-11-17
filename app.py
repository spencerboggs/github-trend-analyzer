from flask import Flask, render_template, request, redirect, url_for
import json
import os
from collect import scrape_trending
from clear_data import clear_data

app = Flask(__name__)
JSON_FILE = "trending_data.json"

@app.route("/")
def index():
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, "w") as f:
            json.dump([], f)

    with open(JSON_FILE, "r") as f:
        repos = json.load(f)
    return render_template("index.html", repos=repos)

@app.route("/scrape", methods=["POST"])
def scrape():
    new_data = scrape_trending()
    if new_data is not None:
        with open(JSON_FILE, "r") as f:
            existing_data = json.load(f)

        # Merge new data with existing data
        existing_names = {repo["name"] for repo in existing_data}
        for repo in new_data:
            if repo["name"] not in existing_names:
                existing_data.append(repo)

        # Sort by star count
        for repo in existing_data:
            if isinstance(repo["stars"], str):
                repo["stars"] = int(repo["stars"].replace(",", ""))
        existing_data = sorted(existing_data, key=lambda x: x["stars"], reverse=True)

        with open(JSON_FILE, "w") as f:
            json.dump(existing_data, f, indent=4)

    return redirect(url_for("index"))

@app.route("/clear", methods=["POST"])
def clear():
    clear_data()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
