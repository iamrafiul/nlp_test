from FileManager import FileManager
import re

class SemanticProcessor:

	# Constructor
	def __init__(self):
		self.file_name = 'semantics.json'
		self.file_manager = FileManager()
		self.file_data = self.file_manager.read_file_data(self.file_name)


	# Get positive semantics
	def get_positive_semantics(self):
		return self.file_data['positive']

	# Get negative semantics
	def get_negative_semantics(self):
		return self.file_data['negative']

	# Get intensifiers
	def get_intensifiers(self):
		return self.file_data['intensifier']


	'''
		Split(Tokenize) a big string into words.

		Input:
			- data : str

		Output:
			- tokens : list of tokens from data
	
	'''
	def tokenize(self, data):
		regex = re.compile('[^A-Za-z0-9\s!?]')
		splitted_words = [ each.encode('utf-8') for each in data.split(' ')]
		tokens = [regex.sub('', each.lower()) for each in splitted_words if regex.sub('', each.lower()) is not '']

		return tokens

	'''
		Count impact factor of a review.

		Input:
			- data : list of tokens
			- semantic: list of semantic(positive/negative) with value
			- intensifiers: list of intensifiers with value

		Output:
			- count : float value of impact
	
	'''
	def count_impact(self, data, semantic, intensifiers):
		count = 0.0
		for each in semantic:
			phrase = each["phrase"]
			value = each["value"]
			key_val, intensifier_val = 0.0, 0.0
			if phrase in data:
				key_val = float(value)
				key_index = data.index(phrase)
				if 0 < key_index:
					prev_word = data[key_index - 1]
					for intensifier in intensifiers:
						if intensifier["phrase"] == prev_word:
							intensifier_val = float(intensifier["multiplier"])
							break
				
			value = float(key_val * intensifier_val) if intensifier_val > 0.0 else key_val
			count += value

		return count


	'''
		Process reviews from the impact factors using semantics and return the best hotel on the given topic

		Input:
			- reviews : list of reviews

		Output:
			- reviews: list of reviews given as input
			- total_pos_count: total positive score 
			- total_neg_count: total negative score
	
	'''
	def process_reviews_using_semantics(self, reviews):
		total_pos_count = 0.0
		total_neg_count = 0.0
		for review in reviews:
			pos_count = 0.0
			neg_count = 0.0

			intensifiers = self.get_intensifiers()
			positives = self.get_positive_semantics()
			negatives = self.get_negative_semantics()

			if review.title is not None:
				title_tokens = self.tokenize(review.title)			
				title_pos_count = self.count_impact(title_tokens, positives, intensifiers)
				title_neg_count = self.count_impact(title_tokens, negatives, intensifiers)

			if review.content is not None:
				content_tokens = self.tokenize(review.content)
				content_pos_count = self.count_impact(title_tokens, positives, intensifiers)
				content_neg_count = self.count_impact(title_tokens, negatives, intensifiers)
				
			pos_count = title_pos_count + content_pos_count
			neg_count = title_neg_count + content_neg_count

			total_pos_count += pos_count
			total_neg_count += neg_count

			review.ratings["positive"] = pos_count
			review.ratings["negative"] = neg_count

		return reviews, total_pos_count, total_neg_count

