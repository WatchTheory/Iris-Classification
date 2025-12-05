from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import pickle
import numpy


app = Flask(__name__)

# load your picke file here 
app.config["SECRET_KEY"] = "your_secret_key"
upload_model = pickle.load(open('Eda-Education_pkl_file','rb'))


# Route to pages 
@app.route("/")
def index():
    return render_template("home.html")


# @app.route("/member", methods=["GET", "POST"])
# def member():
#     name = False
#     email = False
#     form = MemberInfo()
#     if form.validate_on_submit():
#         name = form.name.data
#         email = form.email.data
#         form.name.data = ""
#     return render_template("member.html", name=name, email=email, form=form)


# @app.route("/member/<name>")
# def member(name):
#     return render_template("member.html", name=name)


# Works
@app.route("/about")
def about():
    return render_template("about.html")


# Works
@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app.run(debug=True)

# def main():
#     print("Hello from basic!")


# if __name__ == "__main__":
#     main(debug=True)



