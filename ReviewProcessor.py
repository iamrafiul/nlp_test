from Hotel import Hotel
from Review import Review
import os
import json
import re

class ReviewProcessor:
	def __init__(self, keyword):
		self.files = ['reviews1.json', 'reviews2.json', 'reviews3.json', 'reviews4.json', 'reviews5.json']
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.hotels = list()
		self.keyword = keyword

	def parse_hotel_info(self, file_name):
		with open( os.path.join(self.dir_path, file_name), 'r+') as file_data:
			hotel_data = json.load(file_data)

		hotel_info = hotel_data['HotelInfo']

		hotel = Hotel()

		try:
			hotel.id = hotel_info['HotelID'] if 'HotelID' in hotel_info else ''
			hotel.name = hotel_info['Name'] if 'Name' in hotel_info else ''
			hotel.hotel_url = hotel_info['HotelURL'] if 'HotelURL' in hotel_info else ''
			hotel.price = hotel_info['Price'] if 'Price' in hotel_info else ''
			hotel.address = hotel_info['Address'] if 'Address' in hotel_info else ''
			hotel.img_url = hotel_info['ImgURL'] if 'ImgURL' in hotel_info else ''

			reviews = hotel_data['Reviews']

			for each in reviews:
				review = Review()

				try:
					review.id = each['ReviewID'] if 'ReviewID'in each else ''
					review.title = each['Title'] if 'Title' in each else ''
					review.content = each['Content'] if 'Content' in each else ''
					review.author = each['Author'] if 'Author' in each else ''
					review.author_location = each['AuthorLocation'] if 'AuthorLocation' in each else ''
					review.date_created = each['Date'] if 'Date' in each else ''
				except:
					pass

				hotel.reviews.append(review)
		except:
			pass
			
		return hotel

	def get_hotel_info_list(self):
		for file_name in self.files:
			hotel = self.parse_hotel_info(file_name)
			self.hotels.append(hotel)

	def filter_reviews(self):
		self.get_hotel_info_list()

		for hotel in self.hotels:
			regex = re.compile('[^A-Za-z0-9\s!?]')
			reviews = hotel.reviews
			print len(reviews)

			filtered_reviews = list()

			for review in reviews:
				isKeywordFound = False
				if review.title is not None:
					title_tokens = [ each.encode('utf-8') for each in review.title.split(' ')]
					title_tokens = [regex.sub('', each.lower()) for each in title_tokens if regex.sub('', each.lower()) is not '']
					
					if self.keyword in title_tokens:
						isKeywordFound = True
					
				if review.content is not None:
					content_tokens = [ each.encode('utf-8') for each in review.content.split(' ')]
					content_tokens = [regex.sub('', each.lower()) for each in content_tokens if regex.sub('', each.lower()) is not '']
					
					if self.keyword in content_tokens:
						isKeywordFound = True

				if isKeywordFound:
					filtered_reviews.append(review)

					#send to find semantics
			
			hotel.reviews = filtered_reviews
			print len(filtered_reviews)
			
				













