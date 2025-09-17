from flask import Flask, redirect, render_template, request,
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
cur = conn.cursor()

# Checking for lauching the creation of db
check_db = False





