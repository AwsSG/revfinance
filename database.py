from flask import Flask, Blueprint, render_template, session, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    inspect, ForeignKey, Column, Integer, Float, String, Boolean
)
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import sessionmaker
from datetime import datetime

"""


# Create a class-based model for the "Users" database
class Users(db.Model):
    UserId = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    EmailAddress = db.Column(db.String(200), nullable=False, unique=True)
    Password = db.Column(db.String(50), nullable=False)

    # Create String
    def __repr__(self):
        return '<Name %r>' % self.name

# Create a class-based model for the "Pots" database
class Pots(db.Model):
    PotId = db.Column(db.Integer, primary_key=True)
    PotTitle = db.Column(db.String(50), nullable=False)
    GoalAmount = db.Column(db.Float, nullable=False)
    PayCycle = db.Column(db.String(200), nullable=False)
    PaymentAmount = db.Column(db.Float, nullable=False)
    isPrivate = db.Column(db.Boolean, unique=False, default=True)
    Creator = db.Column(db.Integer, ForeignKey(Users.UserId))
    Peers = db.Column(db.ARRAY(String), nullable=False)
    Created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Create String
    def __repr__(self):
        return '<Name %r>' % self.name

# Create the database
db.create_all()


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
"""