from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class BorrowRecord(Base):
    __tablename__ = 'borrow_records'

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    date_created = Column(Date)

    book = relationship("Book", backref="borrow_records")
    user = relationship("User", backref="borrow_records")

    def __init__(self, book, user, date_created):
        self.book = book
        self.user = user
        self.date_created = date_created
