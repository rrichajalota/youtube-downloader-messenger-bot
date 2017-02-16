import requests
from bs4 import BeautifulSoup as BS
from models import QueryResults
from django.db.utils import OperationalError
#import os

def get_data(query): 
	#taken youtube web API and added our query string to it
	url = 'https://www.youtube.com/results?search_query=' + query
	r = requests.get(url)
	html = r.text
	soup = BS(html)

	vids = soup.find_all('a', class_='yt-uix-tile-link')
	num = 1
	
	#save the query results in the databse
	for ix in vids:
		#print num, ix.text #, ix['href']
		new_data_element = QueryResults(sno = num, text = ix.text)
		new_data_element.save()
		num += 1 

	#get all data from the database to display it
	all_data = QueryResults.objects.all()
	data = ''
	for dt in all_data:
		data = data + str(dt) + '\n'
	return data

"""
	try:
		index = int(raw_input('Enter the S.NO. of the video that you would like to download:'))
	except (EOFError):
		print "error!!"

	video_url = 'https://www.youtube.com' + vids[index]['href']

	#print video_url
	#os.system('youtube-dl ' + video_url)
"""

get_data(query= "goong english subtitles")


#youtube-dl downloads a video to our system locally. 
#command: youtube-dl video-url

def get_video(index):
	video_url = 'https://www.youtube.com' + vids[index]['href']
	return video_url