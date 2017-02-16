from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic  # for class

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import json 
import requests
from secrets import access_token
from scraper import get_data, get_video
from models import QueryResults
from django.db.utils import OperationalError

# Create your views here.
def hello(request):

	return HttpResponse("Hey!")

class CommonUrl(generic.View): #this class will inherit its properties from generic.view class of django
	#we will use the constructor of base class 
	#and override its POST and GET methods

	def get(self, request, *args, **kwargs):
		return HttpResponse("Hello")  #all the get requests for the corresponding url will be handled by this function

class ChatBot(generic.View):

	def get(self, request, *args, **kwargs):
		print self.request.GET #will print all the parameters of GET request
		if self.request.GET.get('hub.verify_token') == '123456789':
			return HttpResponse(self.request.GET['hub.challenge']) #fb sends all the tokens with the name of hub
		else:
			return HttpResponse('Error, invalid token')

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		#print self.request.body
		#incoming information coming in the form of string
		#encode is the property of string
		# utf-8 hides all the special characters in the string
		# the string object is passed to json.loads
		# json.dumps -> converts dict to string 
		# json.loads -> converts json string to dictionary
		message = json.loads(self.request.body.encode('utf-8'))
		#iterate over the dictionary to get the message
		for entry in message['entry']:
			for msg in entry['messaging']:
				print msg['message']['text']
				reply_to_message(msg['sender']['id'], msg['message']['text'])

		return HttpResponse("None")

def reply_to_message(user_id, message):
	url = 'https://graph.facebook.com/v2.6/me/messages?access_token=' + access_token

	resp = generate_response(message)
	#make the payload dictionary
	send_resp = {"recipient":{"id":user_id}, "message":{"text":resp}}
	response_msg = json.dumps(send_resp)
	#using the requests library, send a POST request to the generated URL above
	status = requests.post(url, headers={"Content-Type": "application/json"},data=response_msg)
	print status.json()

def generate_response(msg):
	"""
	indices_list = []
	try:
		indices_list = QueryResults.objects.get(keyname = sno)
	except OperationalError:
		pass
	"""

	if 'search' in msg:
		q = ''.join([ix for ix in msg.split('search', 1)[1]])
		#result = get_data(q)  #display the data resulting from a query search 
		return get_data(q)

	elif int(msg) in range(1,100): #fetch the link of that video
		link = get_video(int(msg))
		return link
	else:
		return "Use search 'search-term' to look for the video you want"
	#return msg
	

