from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    inspect, ForeignKey, Column, DateTime, Integer, Float, String, Boolean, JSON
)
from sqlalchemy.dialects.postgresql import ARRAY
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
    FirstName = Column(String(50), nullable=False)
    LastName = Column(String(50), nullable=False)
    EmailAddress = Column(String(200), nullable=False, unique=True)
    Password = Column(String(50), nullable=False)


# Create a class-based model for the "Pots" database
class Pot(Base):
    __tablename__ = "Pots"
    PotId = Column(Integer, primary_key=True)
    PotTitle = Column(String(50), nullable=False)
    GoalAmount = Column(Float, nullable=False)
    PayCycle = Column(String(200), nullable=False)
    PaymentAmount = Column(Float, nullable=False)
    isPrivate = Column(Boolean, unique=False, default=True)
    Creator = Column(Integer, ForeignKey(User.UserId))
    Peers = Column(ARRAY(String), nullable=False)



# Create a new instance of sessionamaker, then point to our engine
Session = sessionmaker(db)


# Open an actual session by calling the subclass defined above
session = Session()


# Creating the database using the declative_base subclass
Base.metadata.create_all(db)


# Commit our session to the database
session.commit()


# Get Users
users = session.query(User)

def get_users():
    inspector = inspect(db.engine)
    if inspector.has_table("Users") == True:
        results = []

        for user in users:
            new = {
                "Id": user.UserId,
                "Name": user.FirstName + user.LastName,
                "Email": user.EmailAddress,
                "Password": user.Password
            }
            results.append(new) 

        return results
    else:
        print('error')
        return None


# Get Pots
pots = session.query(Pot)

def get_pots():
    inspector = inspect(db.engine)
    if inspector.has_table("Pots") == True:
        results = []

        for pot in pots:
            new = {
                "Id": pot.PotId,
                "Title": pot.PotTitle,
                "Goal": pot.GoalAmount,
                "Cycle": pot.PayCycle,
                "PaymentAmount": pot.PaymentAmount,
                "Private": pot.isPrivate,
                "Creator": pot.Creator,
                "PeersEmails": pot.Peers
            }
            results.append(new) 

        return results
    else:
        print('error creating pot')
        return None
