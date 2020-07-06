import os
import json
import datetime as dt

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text, ForeignKey, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
ID_LEN = 100
STR_LEN = 500


class Drink(Base):
    __tablename__ = "drinks"

    drink_id = Column(Integer, primary_key=True, autoincrement=True)
    drink_name = Column(String(STR_LEN), nullable=False, unique=True)
    drink_type = Column(String(STR_LEN))
    density = Column(DECIMAL)
    water_solubility = Column(Boolean)
    color = Column(String(STR_LEN))
