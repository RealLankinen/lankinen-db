from src import db

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    email = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    databases = db.relationship('database', backref='account', lazy=True)

    def __init__(self, email, password):
        self.email = email
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True