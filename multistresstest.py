import threading
import urllib
import random
import time
import sys

if len(sys.argv) > 1:
	url = sys.argv[1]
else:
	url = ""

if len(url) > 0:
	pass

else:
	print "You need to specify a URL, defaulting to localhost"
	url = "http://localhost"

max = 0
times = []
count = 0
threads = []

def get_average(array):

	total = 0

	length = len(array)

	for item in array:
		total = total + item
	
	average = total/length
	
	times = []
	return(average)

def geturl(url):

        start = time.time()
	something = urllib.urlopen(url)
        end = time.time()
        total = end - start
        return(total)

def initthreads(max):

	print "I will init threads now"	
	print "You told me %s" % (max)

	max = long(max)

	delay = 1.0/max

	for i in range(0,max):
		item_id = random.randint(0,4140)
        	#item_id = 4106
		#url = "http://www.gibsonandlily.com/comments/%s" % (item_id)
		#url = "http://www.gibsonandlily.com/static"
		#url = "http://www.gibsonandlily.com/static/staticloader.cgi"

		

		#url = "http://thingist.com"
		StressTest(url).start()
		time.sleep(delay)		
		if i == (max - 1):
			print "This one is last"
			time.sleep(.5)

class StressTest(threading.Thread):
	
	def __init__(self, url):
		self.url = url
		threading.Thread.__init__(self)
	
	def run(self):

		self.start = time.time()
		urllib.urlopen(self.url)
		self.end = time.time()
		self.total = self.end - self.start
		print "%s seconds" % (self.total)		
		times.append(self.total)	

while max != "end":
	
	count = 0	
	times = []
	print "Say \'end\' to quit"
	max = raw_input("How many urls should I load? ")
	
	try:
		max = int(max)
		initthreads(max)
	except:
		if max == "average":
			average = get_average(times)
			print "Average: %s" % (average)
