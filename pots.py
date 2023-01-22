
new_pot_table = db.Table(tableName,
db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
db.Column('user_email', db.String, db.ForeignKey('users.email')),
db.Column('role', db.String)
)

db.create_all()

tableName = str(latest_id.id)
            new_pot_table = db.Table(tableName,
            db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
            db.Column('user_email', db.String, db.ForeignKey('users.email')),
            db.Column('role', db.String)
            )

            db.create_all()




