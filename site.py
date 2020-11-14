from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form
from passlib.hash import sha256_crypt

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")


if __name__ == "__main__":
	app.run(debug=True)
