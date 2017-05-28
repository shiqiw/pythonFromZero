from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time
import os

class Scheduler:
	sched = BackgroundScheduler()

	@staticmethod
	def start():
		Scheduler.sched.start()

	@staticmethod
	def add_job(job, interval, id=None):
		Scheduler.sched.add_job(job, 'interval', hours=interval, job_id=id)

	@staticmethod
	def remove_job(job_id):
		Scheduler.sched.remove_job(job_id)

	@staticmethod
	def stop():
		Scheduler.sched.stop()