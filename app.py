from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

BOOKS_FILE = 'books.json'



def load_books():
    with open(BOOKS_FILE, 'r') as f:
        return json.load(f)

def save_books(books):
    with open(BOOKS_FILE, 'w') as f:
        json.dump(books, f, indent=4)

@app.route("/", methods=["GET", "POST"])
def home():
    books = load_books()

    # --- Add Book Form Submission ---
    if request.method == "POST" and "title" in request.form:
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "description": request.form["description"]
        }
        books.append(new_book)
        save_books(books)
        return redirect(url_for("home"))

    # --- Search Handling ---
    query = request.args.get("query")
    results = []
    if query:
        results = [b for b in books if query.lower() in b["title"].lower()]
        return render_template("home.html", books=books, results=results, query=query, title="Home - BookWorld", page_css="home.css")

    return render_template("home.html", books=books, title="Home - BookWorld", page_css="home.css")

@app.route("/books")
def books():
    with open("books.json") as f:
        books = json.load(f)
    return render_template("books.html", books=books, title="Books", page_css="books.css")

@app.route("/book/<int:book_id>")
def book_detail(book_id):
    with open("books.json") as f:
        books = json.load(f)
    book = books[book_id]
    return render_template("book_detail.html", book=book, title=book['title'], page_css="book_detail.css")


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query'].lower()
        books = load_books()
        results = [book for book in books if query in book['title'].lower()]
        return render_template('search.html', books=results, query=query)
    return render_template('search.html', books=[], query="", title="Search", page_css="search.css")


@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        # handle form data and save to JSON
        ...
        return redirect("/books")
    return render_template("add_book.html", title="Add Book", page_css="add_book.css")



if __name__ == '__main__':
    app.run(debug=True)
