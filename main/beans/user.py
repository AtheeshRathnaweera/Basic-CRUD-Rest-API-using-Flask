from sqlalchemy import Column, String, Integer, Date
from base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    date_created = Column(Date)

    def __init__(self, name, email, date_created):
        self.name = name
        self.email = email
        self.date_created = date_created
