import flask
from flask_restful import Api
from user_controller import UserController
from books_controller import BooksController
from base import Session, engine, Base
from book import Book

# generate database schema
Base.metadata.create_all(engine)

base_url = "/api/v1/"

app = flask.Flask(__name__)
api = Api(app)

api.add_resource(UserController, base_url + "users")
api.add_resource(BooksController, base_url + "books")

if __name__ == "__main__":
    app.run(debug=True)
