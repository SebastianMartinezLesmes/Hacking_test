from flask import Flask, request, jsonify
import hmac

app = Flask(__name__)

SECRET = "h4ck"

@app.route("/login", methods=["POST"])
def login():
    user_input = request.json.get("password", "")
    if hmac.compare_digest(user_input, SECRET):  # Comparación constante en tiempo
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "unauthorized"}), 401

if __name__ == "__main__":
    app.run(debug=False)
