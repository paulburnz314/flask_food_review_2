from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/home/food_service/<string:name>/review/<int:id>')
def foodservices(name, id):
	return "Food Service: " + name + ", review id: " + str(id)


@app.route('/reviews')
def reviews(id):
	return render_template('reviews.html')

