import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


"""
Pulls terms from the geoTerms collection in database
"""


@app.route("/")
@app.route("/get_geoTerms")
def get_geoTerms():
    # Sorts terms alphabetically
    geoTerms = list(mongo.db.geoTerms.find().sort("geology_term"))
    return render_template("terms.html", geoTerms=geoTerms)


"""
Registers a new user and adds to user collection in database
"""


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Checks db to see if user already in use
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        # Generates a hashed password for security and stores in database
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


"""
Allows users to log in to site
"""


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Checks db to see if user already in use
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Checks if hashed password matches user password
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                        request.form.get("username")))
                return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # Password incorrect
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # If the Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


"""
User profile page
"""


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


"""
Logs user out of their profile
"""


@app.route("/logout")
def logout():
    # removes user from session cookies once logged out
    flash("You have logged out.")
    session.pop("user")
    return redirect(url_for("login"))


"""
Allows users to add new terms to the database
"""


@app.route("/add_term", methods=["GET", "POST"])
def add_term():
    # allows users to add new terms and definitions
    if request.method == "POST":
        geoTerms = {
            "geology_term": request.form.get("geology_term"),
            "definition": request.form.get("definition"),
            "created_by": session["user"]
        }
        mongo.db.geoTerms.insert_one(geoTerms)
        flash("Thanks, new geology term and definition added")
        return redirect(url_for("get_geoTerms"))

    geoTerms = mongo.db.geoTerms.find().sort("geology_term", 1)
    return render_template("add_term.html")


"""
Allows users to edit existing terms in the database
"""


@app.route("/edit_term/<term_id>", methods=["GET", "POST"])
def edit_term(term_id):
    # allows users to edit existing terms and definitions
    if request.method == "POST":
        geoTerms = {
            "geology_term": request.form.get("geology_term"),
            "definition": request.form.get("definition"),
            "created_by": session["user"]
        }
        mongo.db.geoTerms.update({"_id": ObjectId(term_id)}, geoTerms)
        flash("Thanks, geology term and definition updated")

    term = mongo.db.geoTerms.find_one({"_id": ObjectId(term_id)})
    return render_template("edit_term.html", term=term)


"""
Allows users to delete existing terms in the database
"""


@app.route("/delete_term/<term_id>")
def delete_term(term_id):
    mongo.db.geoTerms.remove({"_id": ObjectId(term_id)})
    flash("Thanks, geology term and definition deleted.")
    return redirect(url_for("get_terms"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
