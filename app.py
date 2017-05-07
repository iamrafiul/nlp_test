from flask import Flask, jsonify, request
import json

from ReviewProcessor import ReviewProcessor

app = Flask(__name__)

@app.route('/')
def index():
	review_proccesor = ReviewProcessor('good')
	hotels = review_proccesor.filter_reviews()
	
	return jsonify({'message': 'Filtering Reviews Done.'})

if __name__ == '__main__':
	app.run(debug=True)