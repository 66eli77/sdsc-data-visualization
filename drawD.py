#!/usr/bin/env python2
import pygame
import sys
import json
import hashlib

from jobD import Job

def main():
	pygame.init()
	fpsClock = pygame.time.Clock()
	size = 1920, 1200
	background = pygame.image.load("go.jpg")
	screen = pygame.display.set_mode(size)
	screen.blit(background,(0,0))
	width = 1
	pseudoJob = Job(0)
	myjob = pseudoJob.getData()
	
	count = 0


	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					sys.exit()
											
		for n in range(0, len(myjob)):
			drawing(width, myjob[n], screen)
			if (n != len(myjob) -1):
				width += (myjob[n].node * myjob[n].core) + 1
			else:
				width = 1
		
		count += 1
		
		if (count == 300):		
			myjob = pseudoJob.getData()
			count = 0

		#print myjob[0].qtime
		pygame.display.flip()
		fpsClock.tick(3)
		
		
def drawing(width, Job, screen):
	rect = pygame.Rect(width, 850, (Job.node * Job.core),( -Job.wallrequest / 800))
	pygame.draw.rect(screen, _hexColor(Job.owner), rect)	
	if(Job.state == "R"):
		rect1 = pygame.Rect(width + 5, 850, (Job.node * Job.core) - 10, (-Job.run)/800)
		pygame.draw.rect(screen, (255, 255, 255), rect1)
	
	
# Create a hex color value from a value
def _hexColor(x):
    hexVal = int(hashlib.md5(x).hexdigest(), 16) % 0xffffff
    return ( hexVal >> 16
           , hexVal >> 8  & 0xff
           , hexVal       & 0xff
           )
	    
if __name__=="__main__":
    main()