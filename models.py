from flaskblog import db
from datetime import datetime
from flask_login import UserMixin
from flaskblog import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User( db.Model,UserMixin):
    __tablename__ = 'user' 
    id = db.Column('id', db.Integer, primary_key=True)
    first = db.Column('first', db.String(80), nullable=False)
    last = db.Column('last', db.String(80), nullable=False)
    username = db.Column('username', db.String(80), unique=True, nullable=False)
    email = db.Column('email', db.String(120), unique=True, nullable=False)
    password = db.Column('password', db.String(100), nullable=False)

    reactions = db.relationship('Reaction', cascade="all,delete", backref = db.backref('user', lazy=True))
    posts = db.relationship('Post', cascade="all,delete", backref = db.backref('user', lazy=True))
    comments = db.relationship('Comment', cascade="all,delete", backref = db.backref('user', lazy=True))
    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    __tablename__ = 'post' 
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(80), nullable=False)
    content = db.Column('content', db.Text, nullable=False)
    date = db.Column('date', db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    comments = db.relationship('Comment', cascade="all,delete", backref = db.backref('post', lazy=True))
    reactions = db.relationship('Reaction', cascade="all,delete", backref = db.backref('post', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.title



class Button(db.Model):
    __tablename__ = 'button' 
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(50), nullable=False)

    reactions = db.relationship('Reaction', cascade="all,delete", backref = db.backref('button', lazy=True))

    def __repr__(self):
        return '<Button %r>' % self.name

class Reaction(db.Model):
    __tablename__ = 'reaction' 
    id = db.Column('id', db.Integer, primary_key=True)
    post_id = db.Column('post_id', db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
    button_id = db.Column('button_id', db.Integer, db.ForeignKey('button.id'), nullable=False)
    state = db.Column('state', db.Boolean, nullable=False, default=True)
    

    def __repr__(self):
        return '<Reaction %r>' % self.state

class Comment(db.Model):
    id = db.Column('id', db.Integer, primary_key=True) 
    content = db.Column('content', db.String(140))
    post_id = db.Column('post_id', db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column('created_at', db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Comment %r>' % self.content


db.create_all()
db.session.commit()

if Button.query.first() == None:
    like = Button(name = 'like')
    shocked = Button(name = 'shocked')
    laugh = Button(name ='laugh')
    db.session.add(like)
    db.session.add(shocked)
    db.session.add(laugh)
    db.session.commit()