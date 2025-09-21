# init_db.py
import sqlite3
from pathlib import Path

def init_db(db_name="quiz.db", schema_file="schema.sql"):
    schema_path = Path(schema_file)
    if not schema_path.exists():
        raise FileNotFoundError(f"Le fichier schema.sql est introuvable: {schema_path}")

    with sqlite3.connect(db_name) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        with open(schema_path, "r", encoding="utf-8") as f:
            conn.executescript(f.read())

    print(f"✅ Base '{db_name}' créée à partir de '{schema_file}' (foreign_keys = ON pour la création).")

if __name__ == "__main__":
    init_db("quiz.db", "schema.sql")
