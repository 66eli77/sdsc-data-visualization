# Eli Dai a11062387
# VIS 198  assignment 2
import pygame
import sys
import json
import hashlib
import urllib2

from Renderer import Render

class Job:

	def __init__(self, jobDict):
		if jobDict == 0:
			self.name = 1
		else:
			#self.name = jobDict["account_name"]
			self.qtime = jobDict["qtime"]
			self.queue = jobDict["queue"]
			self.state = jobDict["job_state"]
			self.wallrequest = jobDict["walltime_req"]
			self.starttime = jobDict["start_time"]
			self.mtime = jobDict["mtime"]
			self.owner = jobDict["job_owner"]
			self.node = jobDict["nodect"]
			self.id = jobDict["job_id"]
			self.core = jobDict["ppn"]
			#if (jobDict["job_state"] == "R"):
			#	self.run = jobDict["walltime_used"]
    
			self.color = "I don't know"
			self.size = "I don't konw"
    
	def getData(self):
		req = urllib2.Request('http://sentinel.sdsc.edu/data/jobs/gordon')
		response = urllib2.urlopen(req)
		jsonStr = response.read()
		data = json.loads(jsonStr)["jobs"]
		dic = {}
		for x in range(0, len(data)):
			dic[x] = Job(data[x])
		return dic

def main():
	pygame.init()
	fpsClock = pygame.time.Clock()
	pseudoJob = Job(0)
	myjob = pseudoJob.getData()
	R = Render()	
	count = 0

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					sys.exit()
		count += 1
		if (count == 3000):
			myjob = pseudoJob.getData()
			count = 0

		R.draw(myjob)
	

		pygame.display.flip()
		fpsClock.tick(30)
		
		
	    
if __name__=="__main__":
    main()