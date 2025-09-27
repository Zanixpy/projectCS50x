# Quiz Web Application
#### Video Demo: <URL HERE>
#### Description:

This project is a **web-based quiz application** built with **Flask (Python)**, **SQLite** for persistent data storage, and **JavaScript** for dynamic user interaction. It is my final project for **CS50x 2025**. The application allows users to select a quiz theme between anime or manhwa, answer a short set of multiple-choice questions, receive an immediate score, and then return to the home page to try again or choose a different theme.

---

## Features

- **Theme Selection**: On the homepage, the user is presented with two available quiz themes. Each theme contains a set of three multiple-choice questions.  
- **Multiple-Choice Questions**: Each question provides three possible answers. The user selects one option per question.  
- **Score Calculation**: When the user submits their answers, the application calculates the total score based on correctness. The score is displayed immediately after submission.  
- **Replay and Navigation**: After completing a quiz, the user can return to the home page and either retake the same theme or try another theme.  
- **Simple and Responsive Interface**: The interface is lightweight and built using HTML templates and CSS, with JavaScript enabling dynamic interactions.  

---

## File Structure and Explanation

The project is organized into several files and directories:

- **`app.py`**  
  This is the main application file. It defines the Flask routes, manages HTTP requests, connects to the database, and renders templates. Key routes include:
  - `/`: Displays the homepage with available quiz themes.  
  - `/anime`: Displays the quiz for anime theme.  
  - `/manhwa`: Displays the quiz for manhwa theme.  
  - `/api/anime/questions`: GET endpoint that retrieves questions for the anime quiz.  
  - `/api/manhwa/questions`: GET endpoint that retrieves questions for the manhwa quiz.  
  - `/api/anime/answers`: GET endpoint that retrieves answers for the anime quiz.  
  - `/api/manhwa/answers`: GET endpoint that retrieves answers for the manhwa quiz.
  - `/api/anime/corrections`: POST endpoint that processes the submitted answers and calculates the score for anime theme.
  - `/api/manhwa/corrections`: POST endpoint that processes the submitted answers and calculates the score for manhwa theme.

- **`schema.sql`**  
  This file initializes the SQLite database. It defines the tables for storing quiz themes, questions, and answers. Each question is associated with one theme, and each answer is linked to its corresponding question.  

- **`templates/`**  
  This directory contains the HTML files used to render the application. Templates include:
  - `quiz.html`: The homepage where users select a quiz theme.  
  - `anime.html`: The page displaying the questions and answer options for anime theme.
  - `manhwa.html`: The page displaying the questions and answer options for manhwa theme.  
  - `layout.html`: A base template that includes common elements like the header and footer, which other templates extend.
  - `layout_quiz.html`: a base template specifically for quiz pages, ensuring consistent styling and structure.

- **`static/`**  
  Contains static assets such as CSS for styling and JavaScript for interactive elements. JavaScript is used to handle client-side behavior, such as input validation or improving user experience during quiz interactions.
  - `style.css`: Contains the CSS styles for the application.
  - `styleQ.css`: Contains the CSS styles for the quiz pages.
  - `game.js`: Contains JavaScript code to enhance interactivity.
  - `home.png`: An image used on the quiz pages.


- **`requirements.txt`**
  Lists the Python dependencies needed to run the application.

- **`README.md`**  
  This document, which describes the project’s purpose, functionality, design, and instructions for running it.  

---

## Design Decisions

When creating this project, I had to make several design choices:  

1. **Technology Stack**: I chose Flask because it is lightweight, beginner-friendly, and ideal for a small web application. Flask makes it easy to define routes and render templates while keeping the code organized. SQLite was chosen because it is easy to set up and requires no external server, making it perfect for a small quiz application.  

2. **Database Structure**: Instead of hardcoding questions directly into Python, I structured them in SQLite. This makes it easier to expand the quiz in the future by simply adding rows to the database. Questions and answers are relationally linked, which mirrors real-world database design.  

3. **Quiz Length**: For this version of the project, each theme contains exactly three questions with three possible answers. This keeps the application simple while still demonstrating functionality. However, the structure of the code and database allows for easy scalability.  

4. **User Sessions**: I decided not to implement user accounts or sessions in this version, as the focus was on the quiz itself rather than authentication. However, this could be a valuable future improvement.  

---

## Learning Outcomes

Working on this project gave me practical experience in:  
- Building a complete **Flask web application** from scratch.  
- Designing and interacting with a **relational database** using SQLite and SQL queries.  
- Writing **dynamic templates** using Jinja2 in Flask.  
- Handling both **GET and POST requests** and managing form submissions securely.  
- Using **JavaScript** to enhance interactivity and improve user experience.  
- Organizing code and separating concerns between frontend, backend, and database layers.  
- Documenting a project thoroughly with a structured README.  

---

## Future Improvements

- Adding more quiz themes and a larger pool of questions.  
- Allowing users to create accounts, save progress, and view past scores.  
- Implementing difficulty levels (easy, medium, hard).  
- Adding a timer to increase challenge.  
- Improving the UI with a frontend framework such as Bootstrap or Tailwind CSS.  

---

## AI Assistance
I utilized AI tools to help me for creating the database with the .sql file and quiz.py file. He also helped me to understand api calls. I used AI to help me with the README file.
## How to Run the Project

1. Clone the repository in terminal: git clone https://github.com/Zanixpy/projectCS50x
   cd <your-repo-name>
2. Install the required dependencies: pip install -r requirements.txt
3. Create the database by running the following command in terminal: python quiz.py
4. Start the Flask application: flask run
5. Open your web browser with the URL provided in the terminal
