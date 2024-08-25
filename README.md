My Library Flask Application
This Flask web application allows you to manage a personal library of books. You can add new books, edit their ratings, and delete books from the library. The application uses SQLAlchemy as the ORM to interact with an SQLite database.

Features
Add New Books: Add a new book to your library by entering the book title, author name, and rating.
Edit Book Rating: Update the rating of any book in your library.
Delete Books: Remove a book from your library.
Installation
Prerequisites
Python 3.7 or higher
Flask
Flask-SQLAlchemy
Step-by-Step Installation
Clone the repository:

sh
Copy code
git clone https://github.com/your-repo/my-library.git
cd my-library
Create a virtual environment (optional but recommended):

sh
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required packages:

sh
Copy code
pip install -r requirements.txt
Run the application:

sh
Copy code
python main.py
Access the application: Open your web browser and navigate to http://127.0.0.1:5000.

Project Structure
plaintext
Copy code
my-library/
│
├── templates/
│   ├── add.html        # HTML template for adding a new book
│   ├── edit.html       # HTML template for editing a book's rating
│   ├── index.html      # HTML template for displaying the list of books
│
├── main.py             # Main application file with routes and database models
├── requirements.txt    # List of Python packages required to run the project
└── README.md           # This README file
Usage
Home Page
The home page displays a list of all the books in the library. Each book has options to either delete it or edit its rating.
Add New Book
You can add a new book by clicking on the "Add New Book" link. Fill in the form with the book name, author name, and rating, and then submit it to add the book to the database.
Edit Book Rating
To edit a book's rating, click the "Edit Rating" link next to the book on the home page. You'll be redirected to a page where you can input a new rating. Submit the form to update the rating.
Delete a Book
To delete a book, click the "Delete" link next to the book on the home page. The book will be removed from the database.
Routes
/: Home page that displays all books in the library.
/add: Page for adding a new book to the library.
/edit?id=<book_id>: Page for editing the rating of a specific book.
/delete?id=<book_id>: Deletes a specific book from the library.
Database
The application uses SQLite as its database, storing information in the my-library.db file. The Book model has the following fields:

id: Unique identifier for each book (integer, primary key).
title: The title of the book (string, max 250 characters, unique).
author: The author of the book (string, max 250 characters).
rating: The rating of the book (float).
