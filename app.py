from flask import Flask, jsonify, request
import json

from ReviewProcessor import ReviewProcessor

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
	topic = request.args.get('topic')

	if len(topic) > 0:
		review_proccesor = ReviewProcessor(topic)
		hotels = review_proccesor.get_filtered_result()

		return jsonify({'result': repr(hotels), 'status': '200 OK'})
	else:
		return jsonify({'message': "No search topic found. Please try with a search topic. A probable URL should be something like http://example.com/?topic=spa'", 'status': '204 No Content'})

if __name__ == '__main__':
	app.run(debug=True)