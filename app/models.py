# structuring the data in database, setting up the field properties
from datetime import datetime, timedelta
from app import db


class Foodservice(db.Model):
	__tablename__ = 'foodservice'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=False, unique=False, nullable=False)
	address = db.Column(db.String(96), index=False, unique=False, nullable=False)
	cuisine_type = db.Column(db.String(64), index=False, unique=False, nullable=True)
	hours = db.Column(db.String(24), index=False, unique=False, nullable=True)
	phone = db.Column(db.String(16), index=False, unique=False, nullable=True)
	reviews = db.relationship("Review", backref='foodservices', lazy='dynamic')
	# a Foodservice can have many reviews
	
	def __repr__(self):
		return f'<Food Service id: {str(self.id)}> - <Food Service name: {self.name}>'


class Review(db.Model):
	__tablename__ = 'review'

	__searchable__ = ['content']
	review_id = db.Column(db.Integer, primary_key=True)
	foodservice_id = db.Column(db.Integer, db.ForeignKey('foodservice.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	content = db.Column(db.String(192), nullable=False)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	rating = db.Column(db.Integer, nullable=False, default='1')

	def __repr__(self):
		return '<Review id: {}> - <Review post: {}>'.format(self.review_id, self.content)


class User(db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True, nullable=False)
	email = db.Column(db.String(128), index=True, unique=True, nullable=False)
	password_hash = db.Column(db.String(128))
	aboutme = db.Column(db.String(140))
	lastseen = db.Column(db.DateTime, default=datetime.utcnow)
	reviews = db.relationship('Review', backref='author', lazy='dynamic')
	# a User can author many reviews

	def __repr__(self):
		return f'<User id: {str(self.id)}> - <User name: {self.username}>'




