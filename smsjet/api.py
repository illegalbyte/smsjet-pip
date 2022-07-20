import requests 
import json 

class sms:
	def __init__(self, api_key):
		self.api_key = api_key
		self.url = "https://smsjet.net/api"
		self.headers = {
			"Content-Type": "application/json",
			"apikey": self.api_key
		}

	def send(self, phone: str, message: str):
		'''
		Send an SMS to a phone number. 
		
		phone: Format must include country code - use E.164 to be certain. 
		message: Message to send.
		
		'''
		data = {
			"phone_number": str(phone),
			"message": str(message)
		}
		url = self.url + "/send"
		r = requests.post(url, headers=self.headers, data=json.dumps(data))
		return r.json()

	def send(self, phone: str, message: str):
		'''
		Send an SMS to a phone number. 
		
		phone: Format must include country code - use E.164 to be certain. 
		message: Message to send.
		
		'''
		data = {
			"phone_number": str(phone),
			"message": str(message)
		}
		url = self.url + "/send"
		r = requests.post(url, headers=self.headers, data=json.dumps(data))
		return r.json()

smsjet = sms("APIKEY")

print(smsjet.send(phone="+61488010808", message="Hello World!"))

