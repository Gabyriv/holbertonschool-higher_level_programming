#!/usr/bin/python3

"""
Model for city objects
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import relationship
from model_state import Base


class City(Base):
    """City class that inherits from Base"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship('State')
