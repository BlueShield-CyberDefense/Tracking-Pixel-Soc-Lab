from flask import Flask, request, send_file, render_template
import os
import json
from datetime import datetime

app = Flask(__name__)

# Ensure logs folder exists
if not os.path.exists("logs"):
    os.makedirs("logs")

LOG_FILE = "logs/events.jsonl"

@app.route("/")
def home():
    return "<h2>Tracking Pixel SOC Lab</h2>"

# Tracking pixel endpoint
@app.route("/pixel.gif")
def pixel():
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "ip": request.remote_addr,
        "user_agent": request.headers.get("User-Agent"),
        "referer": request.headers.get("Referer"),
        "params": request.args.to_dict()
    }

    # Append to JSONL log file
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")

    # Send 1x1 GIF
    return send_file(
        "1x1.gif",
        mimetype="image/gif"
    )

@app.route("/dashboard")
def dashboard():
    events = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE) as f:
            for line in f:
                events.append(json.loads(line))
    events = list(reversed(events[-200:]))

    return render_template("dashboard.html", events=events)

if __name__ == "__main__":
    app.run(debug=True)
