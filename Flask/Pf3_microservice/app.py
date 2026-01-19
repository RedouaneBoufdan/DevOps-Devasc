from flask import Flask, request, jsonify
import hashlib
import re

app = Flask(__name__)

BANNED_PASSWORDS = {"password", "123456", "qwerty", "admin", "letmein", "welcome"}

def strength_score(pw):
    tips = []
    score = 0

    if len(pw) >= 12:
        score += 2
    elif len(pw) >= 8:
        score += 1
    else:
        tips.append("Gebruik minstens 8 tekens (liefst 12+).")

    if re.search(r"[A-Z]", pw):
        score += 1
    else:
        tips.append("Voeg minstens 1 hoofdletter toe.")

    if re.search(r"[a-z]", pw):
        score += 1
    else:
        tips.append("Voeg minstens 1 kleine letter toe.")

    if re.search(r"[0-9]", pw):
        score += 1
    else:
        tips.append("Voeg minstens 1 cijfer toe.")

    if re.search(r"[^A-Za-z0-9]", pw):
        score += 1
    else:
        tips.append("Voeg minstens 1 speciaal teken toe.")

    level = "zwak"
    if score >= 5:
        level = "sterk"
    elif score >= 3:
        level = "matig"

    return {"score": score, "level": level, "tips": tips}

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "pf3-microservice"})

@app.route("/strength", methods=["POST"])
def strength():
    data = request.get_json(silent=True) or {}
    pw = data.get("password", "")
    if not pw:
        return jsonify({"error": "JSON body moet 'password' bevatten."}), 400
    return jsonify(strength_score(pw))

@app.route("/hash", methods=["POST"])
def hash_pw():
    data = request.get_json(silent=True) or {}
    pw = data.get("password", "")
    if not pw:
        return jsonify({"error": "JSON body moet 'password' bevatten."}), 400
    h = hashlib.sha256(pw.encode()).hexdigest()
    return jsonify({"sha256": h})

@app.route("/check", methods=["POST"])
def check_banned():
    data = request.get_json(silent=True) or {}
    pw = data.get("password", "")
    if not pw:
        return jsonify({"error": "JSON body moet 'password' bevatten."}), 400
    return jsonify({"banned": pw.lower() in BANNED_PASSWORDS})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5051)
