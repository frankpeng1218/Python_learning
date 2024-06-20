from flask import Blueprint, render_template
import db.user_detail

user_detail = Blueprint("user_detail", __name__)

@user_detail.route("/user_detail/search-user_detail-list")
def search_user_detail_list():
    list = db.user_detail.search_user_detail_list()
    # list = [1,2,3,4,5,6,7]
    print(list)
    return render_template("user_detail.html", list=list)