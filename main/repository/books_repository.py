from base import Session
from book import Book
from flask import jsonify
from book_serializer import get_book_as_json, get_books_list_as_json


class BooksRepository:
    session = Session()

    def get_all(self):
        all_books = self.session.query(Book).all()
        return jsonify(get_books_list_as_json(all_books))

    def get_by_id(self, book_id):
        book = self.session.query(Book).get(book_id)
        return jsonify(get_book_as_json(book))

    def save(self, new_book):
        new_book = Book(new_book["name"])
        self.session.add(new_book)
        self.session.commit()

        return jsonify(get_book_as_json(new_book))

    def update(self, book_id, new_data):
        exist_book = self.session.query(Book).filter(Book.id == book_id).first()
        exist_book.name = new_data["name"]
        self.session.commit()

        return jsonify(get_book_as_json(exist_book))

    def delete(self, book_id):
        result = self.session.query(Book).filter(Book.id == book_id).delete()
        self.session.commit()

        if result == 0:
            return False
        else:
            return True

