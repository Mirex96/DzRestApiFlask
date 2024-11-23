from flask import Blueprint, request, jsonify
from models import posts, Post

post_routes = Blueprint('post_routes', __name__)

@post_routes.route('/', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(post_id=len(posts) + 1, user_id=data['user_id'], title=data['title'], content=data['content'])
    posts.append(new_post)
    return jsonify({"message": "Post created successfully!"}), 201

@post_routes.route('/', methods=['GET'])
def get_posts():
    return jsonify([post.__dict__ for post in posts]), 200

@post_routes.route('/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    for post in posts:
        if post.post_id == post_id:
            post.title = data['title']
            post.content = data['content']
            return jsonify({"message": "Post updated successfully!"}), 200
    return jsonify({"error": "Post not found"}), 404

@post_routes.route('/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    posts = [post for post in posts if post.post_id != post_id]
    return jsonify({"message": "Post deleted successfully!"}), 200