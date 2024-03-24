# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    # Relationships
    tasks = db.relationship('Task', backref='user', lazy=True)
    
    profile = db.relationship('UserProfile', back_populates='user', uselist=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

class UserProfile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    sexe = db.Column(db.String(10), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    
    # Relationships
    # Define the back reference to User
    user = db.relationship('User', back_populates='profile')
    
    def __repr__(self):
        return '<UserProfile %r>' % self.first_name

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    def __repr__(self):
        return '<Task %r>' % self.title

