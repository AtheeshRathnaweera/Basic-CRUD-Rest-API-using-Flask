from datetime import datetime

from flask import jsonify
from base import Session
from user import User
from user_serializer import get_users_list_as_json, get_user_as_json


class UserRepository:
    session = Session()

    def get_all(self):
        all_books = self.session.query(User).all()
        return jsonify(get_users_list_as_json(all_books))

    def get_by_id(self, user_id):
        book = self.session.query(User).get(user_id)
        return jsonify(get_user_as_json(book))

    def save(self, new_user):
        new_user = User(new_user["name"], new_user["email"], datetime.now())
        self.session.add(new_user)
        self.session.commit()

        return jsonify(get_user_as_json(new_user))

    def update(self, user_id, new_user):
        exist_user = self.session.query(User).filter(User.id == user_id).first()
        exist_user.name = new_user["name"]
        exist_user.email = new_user["email"]
        self.session.commit()

        return jsonify(get_user_as_json(exist_user))

    def delete(self, user_id):
        result = self.session.query(User).filter(User.id == user_id).delete()
        self.session.commit()

        if result == 0:
            return False
        else:
            return True
