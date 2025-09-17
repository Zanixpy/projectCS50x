CREATE TABLE IF NOT EXISTS theme(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS questions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    theme_id INTEGER NOT NULL,
    question TEXT NOT NULL,
    correct_answer_id INTEGER NOT NULL,
    FOREIGN KEY (theme_id) REFERENCES theme(id),
    FOREIGN KEY (correct_answer_id) REFERENCES answers(id)
)
