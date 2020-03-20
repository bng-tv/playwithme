import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

from playwithme.config import SQLA_URI

engine = create_engine(SQLA_URI)
base = declarative_base(bind=engine)


def session():
    return scoped_session(sessionmaker(bind=engine))()


class StorageModel(base):
    __tablename__ = "entries"
    id = Column(Integer, autoincrement=True, primary_key=True)
    twitch = Column(String(255))
    handle = Column(String(255))
    game = Column(String(255))
    date = Column(DateTime, default=datetime.datetime.utcnow())
