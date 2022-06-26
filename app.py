from flask import Flask, render_template, redirect, url_for, request
import cv2

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        if request.form['email'] == 'user@mail.com' or request.form['password'] == 'user':
            return redirect(url_for('voter_login'))
        elif request.form['email'] == 'admin@mail.com' or request.form['password'] == 'admin':
            return redirect(url_for('register_voter'))
        else:
            error = 'Invalid Credentials ! Please try again'
    return render_template("index.html", error=error)


@app.route("/register_voter")
def register_voter():
    return render_template("register_voter.html")


@app.route("/register_candidate")
def register_candidate():
    return render_template("register_candidate.html")


@app.route("/vote")
def vote():
    return render_template("vote.html")


@app.route("/voter_login")
def voter_login():
    return render_template("voter_login.html")


@app.route("/vote_tallying")
def vote_tallying():
    return render_template("vote_tallying.html")


def facial_recognition():
    pass


if __name__ == "__main__":
    app.run()
