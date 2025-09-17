""" Table theme for theme quiz"""
CREATE TABLE IF NOT EXISTS theme(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    name TEXT NOT NULL
);

""" Table contains all questions"""
CREATE TABLE IF NOT EXISTS questions(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    theme_id INTEGER NOT NULL,
    question TEXT NOT NULL,
    FOREIGN KEY (theme_id) REFERENCES theme(id),
);

""" Table contains all answers from questions"""
CREATE TABLE IF NOT EXISTS answers(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    question_id INTEGER NOT NULL,
    answer TEXT NOT NULL,
    is_correct BOOLEAN NOT NULL,
    FOREIGN KEY (question_id) REFERENCES questions(id)
);

""" At the end to do a leadboard, that contains username"""
CREATE TABLE IF NOT EXISTS records(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    position INTEGER NOT NULL,
    theme_id INTEGER NOT NULL,
    username TEXT NOT NULL,
    score INTEGER NOT NULL,
    FOREIGN KEY theme_id REFERENCES theme(id)
);


"""Inserting values"""

"""For theme table"""
INSERT OR IGNORE INTO theme (id, name) VALUES (1, "Anime");
INSERT OR IGNORE INTO theme (id, name) VALUES (2, "Manhwa");

"""For questions table"""
INSERT OR IGNORE INTO questions (theme_id, question) VALUES (   
    (1, "Dans Naruto, quel est le nom du démon renard scellé en Naruto ?"),   
    (1, "Dans Tokyo Ghoul, comment s’appelle l'organisation qui traque les goules ?"),   
    (1, "Dans Shingeki no Kyojin (SNK), quel est le véritable nom du Titan Colossal ?"),   
    (2, "REMPLIR"),
    (2, "REMPLIR"),
    (2, "REMPLIR"),
);

"""For answers table"""

INSERT OR IGNORE INTO answers (question_id, answer, is_correct) VALUES (   
    (1, "Shukaku", 0),   
    (1, "Kurama", 1),   
    (1, "Matatabi", 0),   
    (2, "Pierrot", 0),   
    (2, "Aogiri Tree", 0),
    (2, "CCG", 1),   
    (3, "Bertolt Hoover", 1),   
    (3, "Reiner Braun", 0),   
    (3, "Zeke Yeager", 0),
    (4, "", 0),   
    (4, "", 0),   
    (4, "", 1),   
    (5, "", 1),   
    (5, "", 0),   
    (5, "", 0),
    (6, "", 0),
    (6, "", 1),
    (6, "", 0),
);





