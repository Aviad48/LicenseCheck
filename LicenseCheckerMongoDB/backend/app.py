import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
import os


app = Flask(__name__)

# Explicit CORS setup
CORS(app, resources={r"/*": {"origins": "*"}})

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("backend.log"), logging.StreamHandler()]
)

logger = logging.getLogger()

# Fetch MongoDB connection string from environment variable
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(mongo_uri)

# Database and collection setup
db = client["user_database"]  # Database name
collection = db["user_records"]  # Collection name

# Middleware to log incoming requests
@app.before_request
def log_request():
    logger.info(f"Incoming {request.method} request to {request.path}")
    if request.method != "OPTIONS":  # Skip preflight request logging
        logger.debug(f"Request data: {request.get_json()}")

# Handle CORS preflight requests
@app.route("/add_user", methods=["OPTIONS"])
def handle_preflight():
    response = jsonify({"message": "Preflight OK"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
    return response, 200

# Add a user
@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        data = request.get_json()

        # Check if all required fields are present
        required_fields = ["first_name", "last_name", "username", "email", "user_number", "license_codes", "start_date", "end_date"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

        # Process the data
        first_name = data["first_name"]
        last_name = data["last_name"]
        username = data["username"]
        email = data["email"]
        user_number = data["user_number"]
        license_codes = data["license_codes"]
        start_date = datetime.strptime(data["start_date"], "%Y-%m-%d")
        end_date = datetime.strptime(data["end_date"], "%Y-%m-%d")

        record = {
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
            "user_number": user_number,
            "license_codes": license_codes,
            "start_date": start_date,
            "end_date": end_date,
        }
        collection.insert_one(record)
        logger.info(f"User {user_number} added successfully")
        return jsonify({"message": "User added successfully"}), 201

    except Exception as e:
        logger.error(f"Error adding user: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
