from books_repository import BooksRepository
from flask_restful import Resource, reqparse
from flask import request


class BooksController(Resource):
    books_repository = BooksRepository()

    book_req_valid_args = reqparse.RequestParser()
    book_req_valid_args.add_argument("id", type=int)
    book_req_valid_args.add_argument("name", type=str, required=True)

    def get(self):
        query_parameters = request.args
        book_id = query_parameters.get('id')

        if book_id:
            return self.books_repository.get_by_id(int(book_id))
        else:
            return self.books_repository.get_all()

    def post(self):
        new_book = self.book_req_valid_args.parse_args()
        return self.books_repository.save(new_book)

    def put(self):
        update_book_req_valid = self.book_req_valid_args.copy()
        update_book_req_valid.replace_argument("id", type=int, required=True)

        new_data = update_book_req_valid.parse_args()

        result = self.books_repository.update(new_data["id"], new_data)
        return result

    def delete(self):
        query_parameters = request.args
        book_id = query_parameters.get('id')

        if book_id:
            return self.books_repository.delete(book_id)
        else:
            return False
