from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Book, Member

# instantiate the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config.from_object(__name__)

db.init_app(app)

with app.app_context():
    db.create_all()

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


# sanity check route
@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify("pong!")


@app.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([book.serialize() for book in books]), 200


@app.route("/books", methods=["POST"])
def add_book():
    new_book = Book(
        title=request.json["title"],
        author=request.json["author"],
        stock=request.json["stock"],
        rent_price=request.json["rent_price"],
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
    book.title = request.json.get("title", book.title)
    book.author = request.json.get("author", book.author)
    book.stock = request.json.get("stock", book.stock)
    book.rent_price = request.json.get("rent_price", book.rent_price)
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
    app.run()
