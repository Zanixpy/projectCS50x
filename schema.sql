CREATE TABLE IF NOT EXISTS themes(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    name TEXT NOT NULL,
    path TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS questions(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    theme_id INTEGER NOT NULL,
    question TEXT NOT NULL,
    FOREIGN KEY (theme_id) REFERENCES themes(id)
);

CREATE TABLE IF NOT EXISTS answers(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    question_id INTEGER NOT NULL,
    answer TEXT NOT NULL,
    is_correct BOOLEAN NOT NULL,
    FOREIGN KEY (question_id) REFERENCES questions(id)
);


INSERT OR IGNORE INTO themes (id, name, path) VALUES (1, "Anime", "/anime");
INSERT OR IGNORE INTO themes (id, name, path) VALUES (2, "Manhwa", "/manhwa");

INSERT OR IGNORE INTO questions (theme_id, question) VALUES
    (1, "In Naruto, what is the name of the fox demon sealed inside Naruto?"),
    (1, "In Tokyo Ghoul, what is the name of the organization that hunts ghouls?"),
    (1, "In Shingeki no Kyojin (Attack on Titan), what is the true name of the Colossal Titan?"),
    (2, "What is the name of Zack Lee's rival in Lookism?"),
    (2, "What is one of the main characteristics of Lloyd Frontera in The Real Estate Developer?"),
    (2, "Which main character in a manhwa used to say 'ARISE'?");


INSERT OR IGNORE INTO answers (question_id, answer, is_correct) VALUES
    (1, "Shukaku", 0),
    (1, "Kurama", 1),
    (1, "Matatabi", 0),
    (2, "Pierrot", 0),
    (2, "Aogiri Tree", 0),
    (2, "CCG", 1),
    (3, "Bertolt Hoover", 1),
    (3, "Reiner Braun", 0),
    (3, "Zeke Yeager", 0),
    (4, "Vasco", 0),
    (4, "Daniel Park", 0),
    (4, "Johan Seong", 1),
    (5, "Ugly", 1),
    (5, "Handsome", 0),
    (5, "Jealous", 0),
    (6, "Javier", 0),
    (6, "Sung jin woo", 1),
    (6, "Gun Park", 0);






