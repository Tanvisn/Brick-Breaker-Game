from headers import *

class Brick:
	def __init__(self, width, height, y, x,strength):
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.strength = strength
		self.pow = 0
		self.ufo = 0
		self.brick_velx = 0
		self.brick_vely = 0
		self.powerup = None

	def display(self, color, symbol, arr):
		y = self.y
		h = self.height
		w = self.width
		x = self.x
		for i in range(y, y+h):
			arr[i] = arr[i][:x] + color + symbol*w + Fore.RESET + Back.RESET + arr[i][x+w:]
		return arr

# Brick that changes color every frame, added hit attribute
class RainbowBrick:
	def __init__(self, width, height, y, x,strength, hit):
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.strength = strength
		self.pow = 0
		self.hit = hit
		self.powerup = None

	def display(self, color, symbol, arr):
		y = self.y
		h = self.height
		w = self.width
		x = self.x
		for i in range(y, y+h):
			arr[i] = arr[i][:x] + color + symbol*w + Fore.RESET + Back.RESET + arr[i][x+w:]
		return arr

