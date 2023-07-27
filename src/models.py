import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    weight = Column(Integer)
    color_eyes  = Column (String (25))
    born_date = Column(Integer)
    height = Column(Integer)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters)
    name= Column(String(100), nullable=False)
    diameter = Column(Integer)
    population = Column(Integer)

class Ships(Base):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters)
    name= Column(String(100))
    model= Column(String(100)) 
    crew = Column(Integer)


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    character_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters)
    ship_id = Column(Integer, ForeignKey('ships.id'))
    ships = relationship(Ships)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')