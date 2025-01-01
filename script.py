from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Simulate the user licensing data
LICENSED_USERS = {
    "aviad": {"licensed": True, "usage_count": 5, "expiration_date": datetime.datetime(2024, 12, 31)},
    "john": {"licensed": False, "usage_count": 0, "expiration_date": datetime.datetime(2023, 12, 31)},
}

@app.route('/checkLicense', methods=['GET'])
def check_license():
    # Hardcode the user to 'aviad'
    user = "aviad"
    
    # Check if the user exists in the LICENSED_USERS data
    user_data = LICENSED_USERS.get(user)
    if not user_data:
        return jsonify({"error": f"User '{user}' not found"}), 404
    
    is_licensed = user_data["licensed"]
    return jsonify({"user": user, "licensed": 1 if is_licensed else 0})

@app.route('/is_license_expired', methods=['GET'])
def is_license_expired():
    # Hardcode the user to 'aviad'
    user = "aviad"
    
    # Check if the user exists in the LICENSED_USERS data
    user_data = LICENSED_USERS.get(user)
    if not user_data:
        return jsonify({"error": f"User '{user}' not found"}), 404

    # Check if the license has expired
    expiration_date = user_data["expiration_date"]
    expired = expiration_date < datetime.datetime.now()

    return jsonify({"user": user, "license_expired": 1 if expired else 0})

@app.route('/check_usage_count', methods=['GET'])
def check_usage_count():
    # Hardcode the user to 'aviad'
    user = "aviad"
    
    # Check if the user exists in the LICENSED_USERS data
    user_data = LICENSED_USERS.get(user)
    if not user_data:
        return jsonify({"error": f"User '{user}' not found"}), 404

    # Return the usage count of the license
    usage_count = user_data["usage_count"]
    return jsonify({"user": user, "usage_count": usage_count})

if __name__ == "__main__":
    # Run the service on port 5000
    app.run(host='0.0.0.0', port=5000)
