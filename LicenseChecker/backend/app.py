from flask import Flask, request, jsonify
import datetime
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Simulate the user licensing data
LICENSED_USERS = {
    "aviad": {"licensed": True, "usage_count": 5, "expiration_date": datetime.datetime(2024, 12, 31)},
    "yakove": {"licensed": False, "usage_count": 0, "expiration_date": datetime.datetime(2023, 12, 31)},
}

@app.route('/checkLicense', methods=['GET'])
def check_license():
    user = request.args.get("user")
    
    if user != "aviad":
        return jsonify({"error": "Access denied"}), 403

    user_data = LICENSED_USERS.get(user)
    if not user_data:
        return jsonify({"error": f"User '{user}' not found"}), 404
    
    is_licensed = user_data["licensed"]
    return jsonify({"user": user, "licensed": 1 if is_licensed else 0})

@app.route('/is_license_expired', methods=['GET'])
def is_license_expired():
    user = request.args.get("user")
    
    if user != "aviad":
        return jsonify({"error": "Access denied"}), 403

    user_data = LICENSED_USERS.get(user)
    if not user_data:
        return jsonify({"error": f"User '{user}' not found"}), 404

    expiration_date = user_data["expiration_date"]
    expired = expiration_date < datetime.datetime.now()

    return jsonify({"user": user, "license_expired": 1 if expired else 0})

@app.route('/check_usage_count', methods=['GET'])
def check_usage_count():
    user = request.args.get("user")
    
    if user != "aviad":
        return jsonify({"error": "Access denied"}), 403

    user_data = LICENSED_USERS.get(user)
    if not user_data:
        return jsonify({"error": f"User '{user}' not found"}), 404

    usage_count = user_data["usage_count"]
    return jsonify({"user": user, "usage_count": usage_count})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
