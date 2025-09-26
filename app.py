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
    conn = get_db_connection()
    themes = conn.execute("SELECT * FROM themes WHERE name='Anime';").fetchall()
    corrections = conn.execute("SELECT DISTINCT questions.id AS q_id, answers.id AS ans_id ,answers.answer FROM themes, answers, questions WHERE themes.id = questions.theme_id AND questions.id = answers.question_id AND themes.name = 'Anime' AND answers.is_correct = 1;").fetchall()
    themes = [dict(row) for row in themes]
    corrections = [dict(row) for row in corrections]
    conn.close()
    return render_template("anime.html", theme="Anime", page="anime", path=themes[0]['path'] )


@app.route("/manhwa", methods=["GET", "POST"])
def manhwa():
    conn = get_db_connection()
    themes = conn.execute("SELECT * FROM themes WHERE name='Manhwa';").fetchall()
    corrections = conn.execute("SELECT DISTINCT questions.id AS q_id, answers.id AS ans_id ,answers.answer FROM themes, answers, questions WHERE themes.id = questions.theme_id AND questions.id = answers.question_id AND themes.name = 'Manhwa' AND answers.is_correct = 1;").fetchall()
    themes = [dict(row) for row in themes]
    corrections = [dict(row) for row in corrections]
    conn.close()
    return render_template("manhwa.html", theme="Manhwa", page="manhwa", path=themes[0]['path'])

@app.route("/api/anime/questions", methods=["GET"])
def apiAnimeQ():
    conn = get_db_connection()
    questions = conn.execute(
        "SELECT DISTINCT questions.id, questions.question FROM themes, answers, questions WHERE themes.id = questions.theme_id AND questions.id = answers.question_id AND themes.name = 'Anime';").fetchall()
    conn.close()
    return jsonify([dict(q) for q in questions])


@app.route("/api/anime/answers", methods=["GET"])
def apiAnimeA():
    conn = get_db_connection()
    questions = conn.execute(
        "SELECT DISTINCT questions.id AS q_id , answers.id AS ans_id, answers.question_id, answers.answer, answers.is_correct FROM themes, answers, questions WHERE themes.id = questions.theme_id AND questions.id = answers.question_id AND themes.name = 'Anime';").fetchall()
    conn.close()
    return jsonify([dict(q) for q in questions])

@app.route("/api/manhwa/answers", methods=["GET"])
def apiManhwaA():
    conn = get_db_connection()
    questions = conn.execute(
        "SELECT DISTINCT questions.id AS q_id , answers.id AS ans_id, answers.question_id, answers.answer, answers.is_correct FROM themes, answers, questions WHERE themes.id = questions.theme_id AND questions.id = answers.question_id AND themes.name = 'Manhwa';").fetchall()
    conn.close()
    return jsonify([dict(q) for q in questions])

@app.route("/api/manhwa/questions", methods=["GET"])
def apiManhwaQ():
    conn = get_db_connection()
    questions = conn.execute("SELECT DISTINCT questions.id, questions.question FROM themes, answers, questions WHERE themes.id = questions.theme_id AND questions.id = answers.question_id AND themes.name = 'Manhwa';").fetchall()
    conn.close()
    return jsonify([dict(q) for q in questions])

@app.route("/api/anime/corrections", methods=["GET","POST"])
def apiAnimeC():
    if request.method == "POST":
        data = request.get_json(silent=True)
        conn = get_db_connection()
        corrections = conn.execute("SELECT DISTINCT questions.id AS q_id, questions.question AS quest, answers.id AS ans_id ,answers.answer FROM themes, answers, questions WHERE themes.id = questions.theme_id AND questions.id = answers.question_id AND themes.name = 'Anime' AND answers.is_correct = 1;").fetchall()
        corrections = [dict(row) for row in corrections]
        conn.close()
        if data:
            if len(corrections) != len(data):
                return jsonify({'error':"Mismatched informations"})
            for i in range(len(corrections)):
                if corrections[i]["q_id"] != data[i]["q_id"] or corrections[i]["quest"] != data[i]["quest"]:
                    return jsonify({'error':"Mismatched informations"})
                if corrections[i]["ans_id"] == data[i]["ans_id"]:
                    if corrections[i]["answer"] != data[i]["answer"]:
                        return jsonify({'error':"Mismatched informations"})
                    else:
                        data[i]["is_correct"] = 1
        else:
            return jsonify({'error':"No data received"})
    return jsonify(data)

@app.route("/api/manhwa/corrections", methods=["GET", "POST"])
def apiManhwaC():
    if request.method == "POST":
        data = request.get_json(silent=True)
        conn = get_db_connection()
        corrections = conn.execute("SELECT DISTINCT questions.id AS q_id, questions.question AS quest, answers.id AS ans_id ,answers.answer FROM themes, answers, questions WHERE themes.id = questions.theme_id AND questions.id = answers.question_id AND themes.name = 'Manhwa' AND answers.is_correct = 1;").fetchall()
        corrections = [dict(row) for row in corrections]
        conn.close()
        if data:
            if len(corrections) != len(data):
                return jsonify({'error':"Mismatched informations"})
            for i in range(len(corrections)):
                if corrections[i]["q_id"] != data[i]["q_id"] or corrections[i]["quest"] != data[i]["quest"]:
                    return jsonify({'error':"Mismatched informations"})
                if corrections[i]["ans_id"] == data[i]["ans_id"]:
                    if corrections[i]["answer"] != data[i]["answer"]:
                        return jsonify({'error':"Mismatched informations"})
                    else:
                        data[i]["is_correct"] = 1
        else:
            return jsonify({'error':"No data received"})
    return jsonify(data)



















