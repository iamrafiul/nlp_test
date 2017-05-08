import re

from Hotel import Hotel
from Review import Review
from FileManager import FileManager
from SemanticProcessor import SemanticProcessor


class ReviewProcessor:
	
	# Constructor
	def __init__(self, keyword):
		self.files = ['reviews1.json', 'reviews2.json', 'reviews3.json', 'reviews4.json', 'reviews5.json']
		self.hotels = list()
		self.keyword = keyword.lower()

	
	'''
		Parse hotel information	

		Input:
			- hotel_obj : object
			- hotel_data : dictionary

		Output:
			- hotel_obj : object

	'''
	def parse_hotel_data(self, hotel_obj, hotel_data):
		address_cleaner = re.compile('<.*?>')
		hotel_obj.id = hotel_data['HotelID'] if 'HotelID' in hotel_data else ''
		hotel_obj.name = hotel_data['Name'] if 'Name' in hotel_data else ''
		hotel_obj.hotel_url = hotel_data['HotelURL'] if 'HotelURL' in hotel_data else ''
		hotel_obj.price = hotel_data['Price'] if 'Price' in hotel_data else ''
		hotel_obj.address = re.sub(address_cleaner, '', hotel_data['Address']) if 'Address' in hotel_data else ''
		hotel_obj.img_url = hotel_data['ImgURL'] if 'ImgURL' in hotel_data else ''

		return hotel_obj

	'''
		Parse all the reviews of a particular hotel	

		Input:
			- data to parse : list of dictionary

		Output:
			- reviews : list

	'''
	def parse_review_data(self, reviews):
		review_list = list()
		for each in reviews:
			review = Review()
			
			review.id = each['ReviewID'] if 'ReviewID'in each else ''
			review.title = each['Title'] if 'Title' in each else ''
			review.content = each['Content'] if 'Content' in each else ''
			review.author = each['Author'] if 'Author' in each else ''
			review.author_location = each['AuthorLocation'] if 'AuthorLocation' in each else ''
			review.date_created = each['Date'] if 'Date' in each else ''

			review_list.append(review)

		return review_list


	'''
		Parse all information(hotel information, reviews) a hotel	

		Input:
			- filename : Name of the file to parse from

		Output:
			- hotel : object

	'''
	def parse_hotel_info(self, file_name):
		file_manager = FileManager()
		file_data = file_manager.read_file_data(file_name)

		hotel_info = file_data['HotelInfo']
		hotel_obj = Hotel()
		hotel = self.parse_hotel_data(hotel_obj, hotel_info)

		reviews = file_data['Reviews']
		review_list = self.parse_review_data(reviews)
		
		hotel.reviews = review_list
			
		return hotel


	'''
		Filter reviews which has the given keyword(topic) 

		Input:
			- reviews : list of reviews

		Output:
			- filtered_revies : filtered list of reviews

	'''
	def filter_reviews_with_keyword(self, reviews):
		filtered_reviews = list()
		for review in reviews:
			isKeywordFound = False
			if review.title is not None:
				if self.keyword in review.title.lower():
					isKeywordFound = True
				
			if review.content is not None:
				if self.keyword in review.content.lower():
					isKeywordFound = True

			if isKeywordFound:
				filtered_reviews.append(review)

		return filtered_reviews


	'''
		Get hotel which has the best score according to simple statictics

		Input:
			- None

		Output:
			- hotel : object

	'''
	def get_filtered_result(self):
		hotel_list = list()

		for file_name in self.files:
			hotel = self.parse_hotel_info(file_name)
			reviews = hotel.reviews
			filtered_reviews = self.filter_reviews_with_keyword(reviews)

			hotel.reviews = filtered_reviews

			hotel_list.append(hotel)

		return hotel_list

