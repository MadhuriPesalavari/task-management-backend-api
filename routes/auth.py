from flask import Blueprint, request
from models.user import User
from extensions import db
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


# =========================
# REGISTER ROUTE
# =========================
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return {"message": "No JSON data received"}, 400

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return {"message": "Missing fields"}, 400

    # check duplicate user
    if User.query.filter_by(email=email).first():
        return {"message": "User already exists"}, 400

    user = User(username=username, email=email)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return {"message": "User Registered"}, 201


# =========================
# LOGIN ROUTE
# =========================
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return {"message": "No JSON data received"}, 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {"message": "Missing fields"}, 400

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return {"message": "Invalid credentials"}, 401

    token = create_access_token(identity=str(user.id))

    return {
        "token": token,
        "message": "Login successful"
    }, 200