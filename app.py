from flask import Flask
from routes.users import user_routes
from routes.posts import post_routes

app = Flask(__name__)

app.register_blueprint(user_routes, url_prefix='/users')
app.register_blueprint(post_routes, url_prefix='/posts')

if __name__ == '__main__':
    app.run(debug=True)