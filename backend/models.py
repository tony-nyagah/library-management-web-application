from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    stock = db.Column(db.Integer, default=0)
    rent_price = db.Column(db.Float, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "stock": self.stock,
            "rent_price": self.rent_price,
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
