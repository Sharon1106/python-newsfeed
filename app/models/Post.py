from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property

class Post(Base):
  __tablename__ = 'posts'
  id = Column(Integer, primary_key=True)
  title = Column(String(100), nullable=False)
  post_url = Column(String(100), nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'))
  # built in datetime module to generate timestamps
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
  # dynamic property that performs a count
  vote_count = column_property(
    select([func.count(Vote.id)]).where(Vote.post_id == id)
  )
  # Foreign Key 
  user = relationship('User')
  # deleting a post from the database also deletes all its associated comments
  comments = relationship('Comment', cascade='all,delete')
  
