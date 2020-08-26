import os
import json
import datetime as dt
import enum

import sqlalchemy
import sqlalchemy.ext.declarative as sql_declarative

Base = sql_declarative.declarative_base()
ID_LEN = 100
STR_LEN = 500

class DrinkType(enum.Enum):
    Soft = 0
    Alcohol = 1

    @staticmethod
    def from_str(label: str):
        for key in DrinkType:
            if label.lower() == key.name.lower():
                return key

        raise NotImplementedError


class Drink(Base):
    __tablename__ = "drinks"

    drink_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    drink_name = sqlalchemy.Column(sqlalchemy.String(STR_LEN), nullable=False, unique=True)
    drink_type = sqlalchemy.Column(sqlalchemy.types.Enum(DrinkType))
    density = sqlalchemy.Column(sqlalchemy.DECIMAL)
    water_solubility = sqlalchemy.Column(sqlalchemy.Boolean)
    color = sqlalchemy.Column(sqlalchemy.String(STR_LEN))
