from flask import Flask, request, jsonify
import time

app = Flask(__name__)

SECRET = "h4ck"

def insecure_compare(a, b):
    for x, y in zip(a, b):
        if x != y:
            return False
        time.sleep(0.05)  # Comparación lenta
    return len(a) == len(b)

@app.route("/login", methods=["POST"])
def login():
    user_input = request.json.get("password", "")
    if insecure_compare(user_input, SECRET):
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "unauthorized"}), 401

if __name__ == "__main__":
    app.run(debug=False)
