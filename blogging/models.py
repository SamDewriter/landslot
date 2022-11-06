import datetime

from flask_login import UserMixin
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text

from . import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))
    blogs = db.relationship("Blog", backref='users', lazy='dynamic')
    
    def __repr__(self) -> str:
        return f"Name: {self.first_name} {self.last_name}"
    
class Blog(db.Model):
    
    __tablename__ = 'blogs'
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    author = Column(Integer, ForeignKey('users.id'))
    image_url = Column(String(150), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    
    def __repr__(self) -> str:
        return f'Blog Post {self.id}'
