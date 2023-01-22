
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def NewPot(id, db): 
    tableName = id.id
    new_table = Table(
        tableName,
        Base.metadata,
        Column("row_id", Integer, primary_key=True),
        Column("user_id", String),
        Column("role", String)
    )
    db.create_all()
    return new_table





