from flask import Flask, jsonify, request
import json

from ReviewProcessor import ReviewProcessor

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
	topic = request.args.get('topic')

	if len(topic) > 0:
		review_proccesor = ReviewProcessor(topic)
		hotel = review_proccesor.get_filtered_result()

		if hotel is not None:
			output = dict()

			output["name"] = hotel.name
			output["hotel_url"] = hotel.hotel_url
			output["address"] = hotel.address
			output["img_url"] = hotel.img_url
			output["positive_rating_count"] = hotel.ratings["positive"]
			output["negative_rating_count"] = hotel.ratings["negative"]
			output["score"] = hotel.score

		return jsonify({'result': output, 'status': '200 OK'})
	else:
		return jsonify({'message': "No search topic found. Please try with a search topic. A probable URL should be something like http://example.com/?topic=spa'", 'status': '204 No Content'})

if __name__ == '__main__':
	app.run(debug=True)