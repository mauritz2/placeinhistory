from app import app, db
from flask import render_template, jsonify, request, session
from models import Stimulus
from sqlalchemy.sql import func

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/play')
def play():
	# selects two random stimuli
	first_stimulus = Stimulus.query.order_by(func.random()).first()
	second_stimulus = Stimulus.query.order_by(func.random()).first()

	# makes sure a stimulus isn't compared to itself. if the code is run with a single stimulus in the db this is an infinite loop 
	while second_stimulus == first_stimulus:
		second_stimulus = Stimulus.query.order_by(func.random()).first()

	return render_template('play.html', first_stimulus = first_stimulus,
			second_stimulus=second_stimulus)

@app.route('/_evaluate_answer')
def evaluate_answer():

	# the solution that worked... the year info is passed from def play() into the template, then requested here
	first_start_year = request.args.get('first_start_year', 0, type=int)
	first_end_year = request.args.get('first_end_year', 0, type=int)
	second_start_year = request.args.get('second_start_year', 0, type=int)
	second_end_year = request.args.get('second_end_year', 0, type=int)

	# the players guess is requested from the template
	guess = request.args.get('answer', 0, type=str)	

	# finds the correct answer
	if first_start_year < second_start_year:
		answer = "before"
	elif second_end_year < first_start_year:
		answer = "after" 
	else:
		answer = "contemporary"

	if guess == answer:
		result = True
	else:
		result = False

	# returns a boolean to the template
	return jsonify(result=result)