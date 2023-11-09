from flask import Blueprint
from sqlalchemy import Engine
import datetime


class BaseService:
    def __init__(self, engine: Engine):
        self.engine = engine

    def serialize_datetime(obj):
        if(isinstance(obj, datetime.datetime)):
            return obj.isoformat()
        raise TypeError("Cannot serialize")