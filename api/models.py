from api import db
from datetime import datetime


class Task(db.Model):
	__tablename__='task'

	id = db.Column(db.Integer, primary_key=True)
	task = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime, default=datetime.utcnow)
	