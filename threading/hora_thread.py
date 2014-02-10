import threading
import datetime

class myThread (threading.Thread):
	def run(self):
		now = datetime.datetime.now()
		print("%s says Hello World at time: %s" % (self.getName(), now))

for i in range(2):
	t = myThread()
	t.start()

