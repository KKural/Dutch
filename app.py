# -*- coding: utf-8 -*-
"""Flask app for Dutch B1 Part 2 Interactive Course."""
import json
import os
from flask import Flask, render_template, jsonify, request

from course_data import CHAPTERS, SESSIONS

app = Flask(__name__)

PROGRESS_FILE = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "progress.json")


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"completed": [], "vocab": {}, "scores": {}}


def save_progress(data):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


@app.route("/")
def index():
    progress = load_progress()
    sessions_map = {s["id"]: s for s in SESSIONS}
    total = len(SESSIONS)
    done = len(progress.get("completed", []))
    pct = int(done / total * 100) if total else 0
    return render_template(
        "index.html",
        chapters=CHAPTERS,
        sessions=sessions_map,
        progress=progress,
        total=total,
        done=done,
        pct=pct,
    )


@app.route("/session/<int:sid>")
def session_view(sid):
    s = next((s for s in SESSIONS if s["id"] == sid), None)
    if not s:
        return "Session not found", 404
    progress = load_progress()
    prev_id = sid - 1 if sid > 1 else None
    next_id = sid + 1 if sid < len(SESSIONS) else None
    return render_template(
        "session.html", s=s, progress=progress, prev_id=prev_id, next_id=next_id
    )


@app.route("/api/progress", methods=["POST"])
def update_progress():
    data = request.get_json(force=True)
    progress = load_progress()

    if "complete_session" in data:
        sid = data["complete_session"]
        if sid not in progress["completed"]:
            progress["completed"].append(sid)

    if "vocab" in data:
        key = str(data.get("session_id", ""))
        progress["vocab"][key] = data["vocab"]

    if "score" in data:
        key = str(data.get("session_id", ""))
        progress["scores"][key] = data["score"]

    save_progress(progress)
    return jsonify({"ok": True})


@app.route("/api/progress/reset", methods=["POST"])
def reset_progress():
    save_progress({"completed": [], "vocab": {}, "scores": {}})
    return jsonify({"ok": True})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
