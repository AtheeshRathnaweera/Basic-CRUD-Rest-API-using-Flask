from marshmallow import Schema, fields

from book_serializer import BookSchema
from user_serializer import UserSchema


class BorrowRecordsSchema(Schema):
    id = fields.Int()
    book = fields.Nested(BookSchema)
    user = fields.Nested(UserSchema)
    date_created = fields.DateTime()


def get_borrow_record_as_json(borrow_record):
    schema = BorrowRecordsSchema()
    return schema.dump(borrow_record)


def get_users_list_as_json(borrow_records_list):
    schema = BorrowRecordsSchema(many=True)
    return schema.dump(borrow_records_list)
