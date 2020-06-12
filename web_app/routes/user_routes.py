# web_app/routes/user_routes.py

from flask import Blueprint, jsonify, request, render_template #, flash, redirect
from web_app.models import db, User, parse_records

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/users.json")
def list_users_json():

    user_records = User.query.all()
    print(user_records)
    users = parse_records(user_records)

    return jsonify(users)

@user_routes.route("/users")
def list_users():

    user_records = User.query.all()
    print(user_records)
    users = parse_records(user_records)

    return render_template("users.html", message="Here is a dump of the users stored in the database:", users=users)

#@user_routes.route("/users/new")
#def new_user():
#    return render_template("new_user.html")

#@user_routes.route("/users/create", methods=["POST"])
#def create_user():
#    print("FORM DATA:", dict(request.form))
    
#    new_user = User(username=request.form["username"])
#    db.session.add(new_user)
#    db.session.commit()

#    return jsonify({
#        "message": "USER CREATED",
#        "user": dict(request.form)
#    })