#!/usr/bin/python3

"""
Contains the definition of a State and an instance.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Class that defines a state.

    Args:
        id (int): The id of the state.
        name (str): The name of the state.
    """
    __tablename__ = "states"
    id = Column('id', Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column('name', String(128), nullable=False)
