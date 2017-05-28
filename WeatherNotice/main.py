from apscheduler.scheduler import Scheduler
import atexit
from flask import Flask
import requests

'''
1. Schedule job to send SMS every morning
2. Schedule job to look up weather and do analysis and perhaps sned SMS
3. Listen user SMS, cancel scheduled job, look up weather and do analysis and perhaps sned SMS

2 + 3 need to schedule new job as well
'''

def get_weather():
	# read configuration
	# construct url
	# send request
	# receive response
	# retry == 4 to get 99.99%
	# deserialize to JSON
    return requests.get('http://example.com').content

def daily_job():
	# get_weather with enum 0
	# extract daily info
	# send SMS

def hourly_job():
	# get_weather with enum 1
	# extract hourly info
	# send SMS or not

@app.route('/SMS', methods=['POST'])
def userUpdate():
	# update configuration
	# cancel job
	# run hourly job immediately
	# add new job
	pass

def main():
	app = Flask(__name__)
	# start scheduler
	# add daily and hourly job to scheduler
    app.run()


# https://stackoverflow.com/a/419185
if __name__ == '__main__':
	main()
