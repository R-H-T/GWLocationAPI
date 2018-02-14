# coding: utf-8
__author__ = "Roberth Hansson-Tornéus"
__copyright__ = "Copyright ©2018 – Roberth Hansson-Tornéus"

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from model import *

db = None


class DatabaseManager:
    """Database Manager"""
    session = None
    engine = None

    def __init__(self, path='sqlite:///app.db'):
        DatabaseManager.engine = create_engine(path)
        global db
        db = DatabaseManager.session
        DatabaseManager.session = sessionmaker(bind=DatabaseManager.engine, autocommit=False, autoflush=False)
        from model.database import Base
        DatabaseManager.session = scoped_session(DatabaseManager.session)
        Base.metadata.create_all(bind=DatabaseManager.engine)
