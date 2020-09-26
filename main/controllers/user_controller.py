from flask_restful import Resource, reqparse
from flask import request
from user_repository import UserRepository


class UserController(Resource):
    user_repository = UserRepository()

    user_req_valid_args = reqparse.RequestParser()
    user_req_valid_args.add_argument("id", type=int)
    user_req_valid_args.add_argument("name", type=str, required=True)
    user_req_valid_args.add_argument("email", type=str, required=True)

    def get(self):
        query_parameters = request.args
        user_id = query_parameters.get('id')

        if user_id:
            return self.user_repository.get_by_id(int(user_id))
        else:
            return self.user_repository.get_all()

    def post(self):
        new_user = self.user_req_valid_args.parse_args()

        result = self.user_repository.save(new_user)

        if result is None:
            print("user save failed")
            return "user save failed"
        else:
            print("user saved successfully")
            return result

    def put(self):
        update_user_req_valid = self.user_req_valid_args.copy()
        update_user_req_valid.replace_argument("id", type=int, required=True)

        new_data = update_user_req_valid.parse_args()

        result = self.user_repository.update(new_data["id"], new_data)

        if result is None:
            print("user update failed")
            return "user update failed"
        else:
            print("user updated successfully")
            return result

    def delete(self):
        query_parameters = request.args
        user_id = query_parameters.get('id')

        return self.user_repository.delete(int(user_id))
