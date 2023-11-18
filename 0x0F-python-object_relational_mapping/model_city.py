#!/usr/bin/python3
"""Model for the city class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Class representing the cities table"""
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
