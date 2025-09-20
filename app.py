from flask import Flask, redirect, render_template, request, g
import sqlite3

# Configure application
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("quiz.html")

@app.route("/anime")
def anime():
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















