from marshmallow import Schema, fields


class BookSchema(Schema):
    id = fields.Int()
    name = fields.Str()


def get_book_as_json(book):
    schema = BookSchema()
    return schema.dump(book)


def get_books_list_as_json(books_list):
    schema = BookSchema(many=True)
    return schema.dump(books_list)
