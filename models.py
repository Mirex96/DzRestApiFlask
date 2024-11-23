users = []
posts = []

class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

class Post:
    def __init__(self, post_id, user_id, title, content):
        self.post_id = post_id
        self.user_id = user_id
        self.title = title
        self.content = content