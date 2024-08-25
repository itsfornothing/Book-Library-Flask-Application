from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my-library.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book: {self.title}, Author: {self.author}>'


with app.app_context():
    db.create_all()
all_books = []


@app.route('/')
def home():
    with app.app_context():
        book_count = db.session.query(Book).count()
        if book_count == 0:
            return render_template("index.html", text="Library Is Empty.")
        else:
            result = db.session.execute(db.select(Book).order_by(Book.title))
            books = result.scalars()
            return render_template("index.html", books=books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_book = Book(title=request.form["book_name"], author=request.form["author_name"],
                            rating=request.form["rating"])
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('home'))

    return render_template("add.html")


@app.route("/edit?id=<int:book_id>", methods=["POST", "GET"])
def edit_rating(book_id):
    if request.method == "POST":
        with app.app_context():
            book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
            book_to_update.rating = request.form["new_rating"]
            db.session.commit()
            return redirect(url_for('home'))
    book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    return render_template("edit.html", title=book.title, rating=book.rating)


@app.route("/delete?id=<int:book_id>", methods=["POST", "GET"])
def delete(book_id):
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        # or book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
