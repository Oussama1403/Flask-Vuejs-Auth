from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

# Instantiate the app
app = Flask(__name__)

# Configure MongoDB
app.config["MONGO_URI"] = (
    "mongodb://localhost:27017/flask_vue_auth_db"  # Replace 'flask_vue_auth_db' with your database name
)
mongo = PyMongo(app)

# ensure email field is unique
mongo.db.users.create_index("email", unique=True)

# Configure JWT
app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key"  # Replace with your own secret key
jwt = JWTManager(app)

# Enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


# User registration
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    print(data)
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"message": "Username, email or password are required"}), 400

    if mongo.db.users.find_one({"email": email}):
        return jsonify({"message": "User already exists"}), 400

    hashed_password = generate_password_hash(password)
    mongo.db.users.insert_one(
        {"username": username, "email": email, "password": hashed_password}
    )

    return jsonify({"message": "User registered successfully"}), 201


# User login
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    print("Received login data:", data)
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    user = mongo.db.users.find_one({"username": username})

    if user and check_password_hash(user["password"], password):
        # Include user_id in the token
        additional_info = {"user_id": str(user["_id"]), "username": user["username"]}
        access_token = create_access_token(
            identity=str(user["_id"]),
            additional_claims=additional_info,
            expires_delta=timedelta(days=1),
        )
        return jsonify({"access_token": access_token}), 200

    return jsonify({"message": "Invalid credentials"}), 401


# protected route
@app.route("/hello", methods=["GET", "POST"])
@jwt_required()
def hello():
    # current_user = get_jwt_identity() 'username' can be retrieved from the backend but it is already retrieved in the frontend (hello view).
    return jsonify({"message": "login success"}), 200


if __name__ == "__main__":
    app.run(debug=True)
