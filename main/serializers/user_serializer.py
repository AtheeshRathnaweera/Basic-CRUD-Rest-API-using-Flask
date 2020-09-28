from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    email = fields.Email()
    date_created = fields.DateTime()


def get_user_as_json(user):
    schema = UserSchema()
    return schema.dump(user)


def get_users_list_as_json(users_list):
    schema = UserSchema(many=True)
    return schema.dump(users_list)
