#!/usr/bin/python3
"""API Security and Authentication Techniques"""

from flask import Flask, jsonify, request

from flask_httpauth import HTTPBasicAuth

from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token, get_jwt_identity
from flask_jwt_extended import jwt_required, JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config-["JWT_SECRET_KEY"] = "123"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("hello"),
              "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("bye"),
               "role": "admin"}
}

# Basic Authentication


@auth.verify_password
def verify_password(username, password):
    if (username in users and
            check_password_hash(users[username]['password'], password)):
        return username


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# JSON Web Token(JWT) Authentication


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    if (username in users and
            check_password_hash(users[username]['password'], password)):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Unauthorized username or password"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    get_jwt_identity()
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@auth.login_required(role='admin')
def admin_only():
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
