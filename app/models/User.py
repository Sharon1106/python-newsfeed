# base database model class
from app.db import Base
from sqlalchemy import Column, Integer, String
# validate data before inserting it into your database
from sqlalchemy.orm import validates
# password-hashing function
import bcrypt

# runs before crating user class
salt = bcrypt.gensalt()

# User inherits from the base class
class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)

  # validates that email contains the @ character
  @validates('email')
  def validate_email(self, key, email):
    assert '@' in email 

    return email
  # validates that the password 4 characters or longer, if not throw error
  @validates('password')
  def validate_password(self, key, password):
    assert len(password) > 4
    # returns the hashed password usring bcrypt and salt to create (unique) credentials
    return bcrypt.hashpw(password.encode('utf-8'), salt)