from flask import Flask, redirect, render_template, request, g
import sqlite3

# Configure application
app = Flask(__name__)

def get_db():
    """
    Retourne une connexion sqlite3 propre à la requête courante.
    Stockée dans flask.g pour éviter le partage entre threads.
    """
    if 'db' not in g:
        conn = sqlite3.connect(str(DATABASE))
        conn.row_factory = sqlite3.Row
        # Activer les PRAGMA utiles pour chaque connexion
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.execute("PRAGMA case_sensitive_like = ON;")
        g.db = conn
    return g.db

db = conn.cursor()



# Checking for lauching the creation of db
with open("schema.sql", "r") as f:
    sql_script = f.read()


db.executescript(sql_script)





@app.route("/")
def home():
    themes = db.execute("SELECT * FROM theme;")
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












