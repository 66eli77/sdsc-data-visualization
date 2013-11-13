# Eli Dai a11062387
# VIS 198  assignment 2
import pygame
import hashlib

class Render:

	def __init__(self):
		print("init")
		self.screen = pygame.display.set_mode((1440, 900))
		
	def draw(self, jobData):
		width = 1
		for n in range(0, len(jobData)):
			if(jobData[n].state == "Q"):
				rectQ = pygame.Rect(width, 850, (jobData[n].node * jobData[n].core)/3,( -jobData[n].wallrequest / 600))
				pygame.draw.rect(self.screen, self.hexColor(jobData[n].owner), rectQ)
			if(jobData[n].state == "H"):	
				rectH = pygame.Rect(width, 850, (jobData[n].node * jobData[n].core)/3,( -jobData[n].wallrequest / 600))
				pygame.draw.rect(self.screen,(120,120,120), rectH)	
			if(jobData[n].state == "R"):
				rect = pygame.Rect(width, 850, (jobData[n].node * jobData[n].core)/3,( -jobData[n].wallrequest / 600))
				pygame.draw.rect(self.screen, self.hexColor(jobData[n].owner), rect)
				rectInside = pygame.Rect(width + 1, 850, (jobData[n].node * jobData[n].core)/3 - 3, (jobData[n].starttime)/600) 
				pygame.draw.rect(self.screen, (255, 255, 255), rectInside)

			if (n != len(jobData) -1):
				width += (jobData[n].node * jobData[n].core)/3 + 1
			else:
				width = 1		

	# Create a hex color value from a value
	def hexColor(self, x):
		hexVal = int(hashlib.md5(x).hexdigest(), 16) % 0xffffff
		return ( hexVal >> 16, hexVal >> 8  & 0xff, hexVal & 0xff)

	def flip(self):
		print("flip")