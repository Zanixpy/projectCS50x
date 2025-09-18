from flask import Flask, redirect, render_template, request, g
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
g.con = conn
dbF = g.con
db = dbF.cursor()

# Checking for lauching the creation of db
with open("schema.sql", "r") as f:
    sql_script = f.read()


dbF.executescript(sql_script)





@app.route("/")
def home():
    themes = dbF.execute("SELECT * FROM theme;")
    print(themes)
    return render_template("quiz.html")

@app.route("/anime")
def anime():
    themes = db.execute("SELECT * FROM theme")
    return render_template("anime.html", name="Anime")

@app.route("/manhwa")
def manhwa():
    return render_template("manhwa.html", name="Manhwa")

@app.route("/api/anime")
def apiAnime():
    return

@app.route("/api/manhwa")
def apiManhwa():
    return


conn.commit()
conn.close()












