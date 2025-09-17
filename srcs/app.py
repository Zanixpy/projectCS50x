from flask import Flask, redirect, render_template, request
import sqlite3

# Configure application
app = Flask(__name__)

# Connecting my db
conn = sqlite3.connect('quiz.db')

# Activate foreign key option
conn.execute("PRAGMA foreign_keys = ON;")

# Activate sensitivy case for LIKE
conn.execute("PRAGMA case_sensitive_like = ON;")

# Access the db to edit
db = conn.cursor()

# Checking for lauching the creation of db
with open("schema.sql", "r") as f:
    sql_script = f.read()

db.executescript(sql_script)

@app.route("/")
def home():

    return render_template("quiz.html")

@app.route("/anime")
def home():

    return render_template("anime.html")

@app.route("/manhwa")
def home():

    return render_template("manhwa.html")


conn.commit()
conn.close()












