import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

followers = Table('followers', Base.metadata,
    Column('user_from_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('user_to_id', Integer, ForeignKey('follower.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=True)
    firstname = Column(String(250), nullable=True)
    lastname  = Column(String(250), nullable=True)
    email  = Column(String(250), nullable=True)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    def to_dict(self):
        return {}
class Follower(Base):
    __tablename__ = 'follower'

    id = Column(Integer, primary_key=True)

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=True)
    url = Column(String(500))
    post_id = Column(Integer, ForeignKey('post.id'))
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
