from flask import Blueprint
user = Blueprint("user", __name__)

@user.route("/user/login")
def login():
    return "登入成功"