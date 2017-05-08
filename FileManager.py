import os
import json

class FileManager:
	def __init__(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))

	def read_file_data(self, file_name):
		with open( os.path.join(self.dir_path, file_name), 'r') as file_data:
			hotel_data = json.load(file_data)
		return hotel_data

