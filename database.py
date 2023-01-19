from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    inspect, func, Column, DateTime, Integer, String, Boolean, JSON
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from creds import database_credentials


# Connect to database
db = database_credentials()
Base = declarative_base()

# Create a class-based model for the "Users" database
class User(Base):
    __tablename__ = "Users"
    UserId = Column(Integer, primary_key=True)
    FirstName = Column(String(50))
    LastName = Column(String(50))
    EmailAddress = Column(String(200))
    Password = Column(String(50))


# Create a new instance of sessionamaker, then point to our engine
Session = sessionmaker(db)


# Open an actual session by calling the subclass defined above
session = Session()


# Creating the database using the declative_base subclass
Base.metadata.create_all(db)


# Commit our session to the database
session.commit()


# Close connection
session.close()


