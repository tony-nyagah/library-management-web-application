from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Book, Member

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config.from_object(__name__)

db.init_app(app)

with app.app_context():
    db.create_all()

CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify("pong!")


@app.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([book.serialize() for book in books]), 200


@app.route("/books", methods=["POST"])
def add_book():
    if request.json is None:
        return jsonify({"error": "request body is empty"}), 400
    title = request.json.get("title")
    author = request.json.get("author")
    synopsis = request.json.get("synopsis")
    available_copies = request.json.get("available_copies")
    if title is None or author is None or synopsis is None or available_copies is None:
        return jsonify({"error": "missing required fields"}), 400
    new_book = Book(
        title=title,
        author=author,
        synopsis=synopsis,
        available_copies=available_copies,
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.serialize()), 201


@app.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    book = Book.query.get(id)
    if book is None:
        return jsonify({"error": "book not found"}), 404
    return jsonify(book.serialize()), 200


@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    book = Book.query.get(id)
    if book is None:
        return jsonify({"error": "book not found"}), 404
    book.title = request.json.get("title", book.title) if request.json else book.title
    book.author = (
        request.json.get("author", book.author) if request.json else book.author
    )
    book.stock = request.json.get("stock", book.stock) if request.json else book.stock
    book.rent_price = (
        request.json.get("rent_price", book.rent_price)
        if request.json
        else book.rent_price
    )
    db.session.commit()
    return jsonify(book.serialize()), 200


@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return jsonify({"error": "book not found"}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({"result": "success"}), 200


@app.route("/members", methods=["GET"])
def get_members():
    members = Member.query.all()
    return jsonify([member.serialize() for member in members])


@app.route("/members/<int:id>", methods=["GET"])
def get_member(id):
    member = Member.query.get(id)
    if member is None:
        return "Member not found", 404
    return jsonify(member.serialize())


@app.route("/members", methods=["POST"])
def create_member():
    data = request.get_json()
    new_member = Member(
        first_name=data["first_name"], last_name=data["last_name"], email=data["email"]
    )  # Add other fields as necessary
    db.session.add(new_member)
    db.session.commit()
    return jsonify(new_member.serialize()), 201


@app.route("/members/<int:id>", methods=["PUT"])
def update_member(id):
    data = request.get_json()
    member = Member.query.get(id)
    if member is None:
        return "Member not found", 404
    member.name = data["name"]  # Update other fields as necessary
    db.session.commit()
    return jsonify(member.serialize())


@app.route("/members/<int:id>", methods=["DELETE"])
def delete_member(id):
    member = Member.query.get(id)
    if member is None:
        return "Member not found", 404
    db.session.delete(member)
    db.session.commit()
    return jsonify({"result": "success"}), 200


if __name__ == "__main__":
    app.run(debug=True)
