from flask import Blueprint
from sqlalchemy import Engine
from typing import LiteralString


class BaseService:
    def __init__(self, engine: Engine, blueprint: Blueprint, url_prefix: LiteralString):
        self.engine = engine
        self.blueprint = blueprint
        self.url_prefix = url_prefix