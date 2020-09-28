from flask_restful import Resource, reqparse
from flask import request

from borrow_records_repository import BorrowRecordsRepository


class BorrowRecordsController(Resource):
    borrow_records_repository = BorrowRecordsRepository()

    borrow_record_req_valid_args = reqparse.RequestParser()
    borrow_record_req_valid_args.add_argument("id", type=int)
    borrow_record_req_valid_args.add_argument("book", type=dict, required=True)
    borrow_record_req_valid_args.add_argument("user", type=dict, required=True)

    def get(self):
        query_parameters = request.args
        borrow_record_id = query_parameters.get('id')

        if borrow_record_id:
            return self.borrow_records_repository.get_by_id(int(borrow_record_id))
        else:
            return self.borrow_records_repository.get_all()

    def post(self):
        new_borrow_record = self.borrow_record_req_valid_args.parse_args()
        return self.borrow_records_repository.save(new_borrow_record)

    def put(self):
        update_borrow_record_req_valid_args = self.borrow_record_req_valid_args.copy()
        update_borrow_record_req_valid_args.replace_argument("id", type=int, required=True)

        new_data = update_borrow_record_req_valid_args.parse_args()

        return self.borrow_records_repository.update(new_data["id"], new_data)

    def delete(self):
        query_parameters = request.args
        borrow_record_id = query_parameters.get('id')

        return self.borrow_records_repository.delete(borrow_record_id)
