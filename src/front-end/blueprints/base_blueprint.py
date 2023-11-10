from flask import Blueprint
from typing import LiteralString
from sqlalchemy import Engine

class BaseBlueprint():
    def __init__(self, blueprint:Blueprint, url_prefix:LiteralString):
        self.blueprint = blueprint
        self.url_prefix = url_prefix