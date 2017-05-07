from flask import Flask, jsonify, request
import json

from ReviewParser import ReviewParser

app = Flask(__name__)

@app.route('/')
def index():
	review_parser = ReviewParser(keyword='')
	hotels = review_parser.get_hotel_info_list()
	return jsonify({'hotel_info': [repr(each) for each in hotels]})

if __name__ == '__main__':
	app.run(debug=True)