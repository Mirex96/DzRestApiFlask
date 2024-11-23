from flask import Blueprint, request, jsonify
from models import users, User

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(user_id=len(users) + 1, username=data['username'], email=data['email'])
    users.append(new_user)
    return jsonify({"message": "User created successfully!"}), 201