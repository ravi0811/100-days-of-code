from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        new_book = {
            'title': request.form['title'],
            'author': request.form['author'],
            'rating': request.form['rating']
        }
        all_books.append(new_book)
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = int(request.form["id"])
        all_books[book_id]['rating'] = request.form["rating"]
        return redirect(url_for('home'))
    
    book_id = int(request.args.get('id'))
    book_selected = all_books[book_id]
    return render_template("edit_rating.html", book=book_selected, book_id=book_id)


if __name__ == "__main__":
    app.run(debug=True)
