import os
import base64
from datetime import datetime
from collections import UserDict
from django.conf import settings


class Utils:
	def date_converter(date: str) -> str:
		date = date.removesuffix("Z")
		date = datetime.fromisoformat(date)
		date = date.date()
		return date

	def handle_file_upload(uploaded_file, uploadDIR: str, filename: str):

		fileDIR = os.path.join(settings.BASE_DIR, "files", uploadDIR)

		if not os.path.exists(fileDIR):
			os.makedirs(fileDIR)

		temp_file = os.path.join(fileDIR, filename)

		with open(temp_file, "wb+") as file:
			for chunk in uploaded_file.chunks():
				file.write(chunk)

		return file
	
	def get_ordinal(number: int) -> str:
		if 11 <= (number % 100) <=13:
			suffix = 'th'
		else:
			suffix = [
				'th',
				'st',
				'nd',
				'rd',
				'th'
			][min(number % 10, 4)]
		return f"{str(number)}{suffix}"

	def read_to_base64(image_path: str) -> bytes:
		with open(image_path, 'rb') as image_file:
			data = base64.b64encode(image_file.read())
		return data


class CleanDict(UserDict):
	
	def __setitem__(self, key, value) -> None:
		if (value == '') or (str(value).isspace()) or (value is None):
			return
		else:
			value = value

		truthy_options = ['true', 'yes', '1']
		falsy_options = ['false', 'no', '0']
		
		if str(value).lower() in truthy_options:
			value = True
		elif str(value).lower() in falsy_options:
			value = False

		super().__setitem__(key, value)
