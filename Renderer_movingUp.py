# Eli Dai a11062387
# VIS 198  assignment 2
import pygame
import hashlib

class Render:

	def __init__(self):
		print("init")
		self.screen = pygame.display.set_mode((8440, 900))

	def draw(self, jobData):
		blue = 0, 51, 102
		pink = 210,180,140
		self.screen.fill(blue)
		widthQandH = 1
		widthR = 1
		for n in range(0, len(jobData)):

			if(jobData[n].state == "Q"):
				rectQ = pygame.Rect(widthQandH, 850, (jobData[n].node * jobData[n].core)/3,( -jobData[n].wallrequest / 900))
				pygame.draw.rect(self.screen, self.hexColor(jobData[n].owner), rectQ)
				if (n != len(jobData) -1):
					widthQandH += (jobData[n].node * jobData[n].core)/3 + 1
				else:
					widthQandH = 1

			if(jobData[n].state == "H"):	
				rectH = pygame.Rect(widthQandH, 850, (jobData[n].node * jobData[n].core)/3,( -jobData[n].wallrequest / 900))
				pygame.draw.rect(self.screen,(120,120,120), rectH)	
				if (n != len(jobData) -1):
					widthQandH += (jobData[n].node * jobData[n].core)/3 + 1
				else:
					widthQandH = 1

			if(jobData[n].state == "R"):
				rect = pygame.Rect(widthR, 300, (jobData[n].node * jobData[n].core), (jobData[n].wallrequest / 900)+(jobData[n].starttime)/900)
				pygame.draw.rect(self.screen, self.hexColor(jobData[n].owner), rect)
				rectInside = pygame.Rect(widthR, 300, (jobData[n].node * jobData[n].core), (jobData[n].starttime)/900) 
				pygame.draw.rect(self.screen, (255, 255, 255), rectInside)
				if (n != len(jobData) -1):
					widthR += (jobData[n].node * jobData[n].core) + 1
				else:
					widthR = 1

	# Create a hex color value from a value
	def hexColor(self, x):
		hexVal = int(hashlib.md5(x).hexdigest(), 16) % 0xffffff
		return ( hexVal >> 16, hexVal >> 8  & 0xff, hexVal & 0xff)

	def flip(self):
		print("flip")