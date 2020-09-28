from datetime import datetime

from base import Session
from flask import jsonify

from book import Book
from borrow_record import BorrowRecord
from borrow_records_serializer import get_borrow_record_as_json, get_users_list_as_json
from user import User


class BorrowRecordsRepository:
    session = Session()

    def get_all(self):
        all_borrow_records = self.session.query(BorrowRecord).all()
        return jsonify(get_users_list_as_json(all_borrow_records))

    def get_by_id(self, book_record_id):
        borrow_record = self.session.query(BorrowRecord).get(book_record_id)
        return jsonify(get_borrow_record_as_json(borrow_record))

    def save(self, new_borrow_record):
        exist_book = self.session.query(Book).filter(Book.id == new_borrow_record["book"]["id"]).first()
        exist_user = self.session.query(User).filter(User.id == new_borrow_record["user"]["id"]).first()

        new_borrow_record = BorrowRecord(exist_book, exist_user, datetime.now())
        self.session.add(new_borrow_record)
        self.session.commit()

        return jsonify(get_borrow_record_as_json(new_borrow_record))

    def update(self, borrow_record_id, borrow_record):
        exist_borrow_record = self.session.query(BorrowRecord).filter(BorrowRecord.id == borrow_record_id).first()

        exist_book = self.session.query(Book).filter(Book.id == borrow_record["book"]["id"]).first()
        exist_user = self.session.query(User).filter(User.id == borrow_record["user"]["id"]).first()

        exist_borrow_record.book = exist_book
        exist_borrow_record.user = exist_user

        self.session.commit()
        return jsonify(get_borrow_record_as_json(exist_borrow_record))

    def delete(self, borrow_record_id):
        result = self.session.query(BorrowRecord).filter(BorrowRecord.id == borrow_record_id).delete()
        self.session.commit()

        if result == 0:
            return False
        else:
            return True
