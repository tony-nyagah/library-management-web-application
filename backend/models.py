from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    synopsis = db.Column(db.String(600), nullable=False)
    available_copies = db.Column(db.Integer, default=1)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "synopsis": self.synopsis,
            "available_copies": self.available_copies,
        }


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    outstanding_debt = db.Column(db.Float, default=0.0)

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "outstanding_debt": self.outstanding_debt,
        }


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey("member.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
    rent_fee = db.Column(db.Float, default=0.0)
    date_issued = db.Column(db.DateTime, default=datetime.utcnow)
    date_returned = db.Column(db.DateTime)

    def serialize(self):
        return {
            "id": self.id,
            "member_id": self.member_id,
            "book_id": self.book_id,
            "rent_fee": self.rent_fee,
            "date_issued": self.date_issued,
            "date_returned": self.date_returned,
        }
