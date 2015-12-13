from app import db

class Stimulus(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	image = db.Column(db.String, nullable=False)
	start_year = db.Column(db.Integer, nullable=False)
	end_year = db.Column(db.Integer, nullable=False)
	stimulus_type = db.Column(db.String, nullable=False) #person, event are used
	wiki_link = db.Column(db.String, nullable=False)
	description = db.Column(db.String, nullable=False)