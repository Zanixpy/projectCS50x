from flask import Flask, redirect, render_template, request, g, jsonify
import sqlite3

# Configure application
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

def get_db_connection():
    conn = sqlite3.connect('quiz.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def home():
    conn = get_db_connection()
    themes = conn.execute("SELECT * FROM themes;").fetchall()
    themes = [dict(row) for row in themes]
    conn.close()
    return render_template("quiz.html", page="quiz", themes=themes)

@app.route("/anime", methods=["GET", "POST"])
def anime():
    if request.method == "POST":
        return render_template("anime.html", name="Anime", page="anime")

    return render_template("anime.html", name="Anime", page="anime")

@app.route("/manhwa", methods=["GET", "POST"])
def manhwa():
    return render_template("manhwa.html", name="Manhwa", page="manhwa")

@app.route("/api/anime/questions", methods=["GET"])
def apiAnimeQ():
    conn = get_db_connection()
    questions = conn.execute("SELECT DISTINCT questions.id, questions.question FROM themes, answers, questions WHERE themes.id = questions.theme_id AND questions.id = answers.question_id AND themes.name = 'Anime';").fetchall()
    conn.close()
    return jsonify([dict(q) for q in questions])

@app.route("/api/anime/answers", methods=["GET"])
def apiAnimeA():
    conn = get_db_connection()
    questions = conn.execute("SELECT * FROM themes;").fetchall()
    conn.close()
    return jsonify([dict(q) for q in questions])

@app.route("/api/manhwa/answers", methods=["GET"])
def apiManhwaA():
    conn = get_db_connection()
    questions = conn.execute("SELECT * FROM themes;").fetchall()
    conn.close()
    return jsonify([dict(q) for q in questions])

@app.route("/api/manhwa/questions", methods=["GET"])
def apiManhwaQ():
    conn = get_db_connection()
    questions = conn.execute("SELECT DISTINCT questions.id, questions.question FROM themes, answers, questions WHERE themes.id = questions.theme_id AND questions.id = answers.question_id AND themes.name = 'Manhwa';").fetchall()
    conn.close()
    return jsonify([dict(q) for q in questions])

















