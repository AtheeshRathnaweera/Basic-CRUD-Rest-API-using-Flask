from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/librarymanagement?charset=utf8mb4', pool_recycle=3600)

Session = sessionmaker(bind=engine)

Base = declarative_base()  # base class for classes definitions
