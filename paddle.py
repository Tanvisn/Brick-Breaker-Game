from headers import *

class Paddle:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.x = 30
		self.y = 35
		self.v = 1
		self.st_time = 0
		self.gun_display = 0
		self.score = 0

	def move(self, move_pos):
		if(self.x > 18 and self.x < 132):
			self.x = self.x + move_pos
		if(self.x <= 20):
			self.x = 21
		elif(self.x >= 132):
			self.x =  131

	def paddle_movement(self,char):
		if char == 'd':
			self.move(1)
		elif char == 'a':
			self.move(-1)


	def display(self, color, symbol, arr):
		y = self.y
		h = self.height
		w = self.width
		x = self.x
		for i in range(y, y+h):
			arr[i] = arr[i][:x] + color + symbol*w + Fore.RESET + Back.RESET + arr[i][x+w:]
		return arr

class Shooter:
	def __init__(self, width, height, x, y):
		self.width = width
		self.height = height
		self.x = x
		self.y = y

	def display(self, color, symbol, arr):
		y = self.y
		h = self.height
		w = self.width
		x = self.x
		for i in range(y, y+h):
			arr[i] = arr[i][:x] + color + symbol*w + Fore.RESET + Back.RESET + arr[i][x+w:]
		return arr

class Bullet:
	def __init__(self, width, height, x, y):
		self.width = width
		self.height = height
		self.vel = -1
		self.x = x
		self.y = y
		self.disappear = 0

	def display(self, color, symbol, arr):
		y = self.y
		h = self.height
		w = self.width
		x = self.x
		for i in range(y, y+h):
			arr[i] = arr[i][:x] + color + symbol*w + Fore.RESET + Back.RESET + arr[i][x+w:]
		return arr

	def shoot(self, paddle, level):
		x = self.x
		y = self.y

		if self.y <= 7:
			self.disappear = 1

		# Handling bullet and brick collision
		# For level 1
		if level.value == 1:
			for i in range(len(arr_brick)):
				if(arr_brick[i].strength != 0):
					if(self.x >= arr_brick[i].x and self.x <= (arr_brick[i].x + arr_brick[i].width)):
	                    # Collides on upper surface of the brick
						if(self.y + self.height == arr_brick[i].y):
							self.disappear = 1
							# First hit for Rainbow brick
							if (i==4 or i==8 or i==10) and arr_brick[i].hit == 0:
								arr_brick[i].hit = 1
	                        # Second hit onwards strength can decrease for Rainbow brick
							if (i==4 or i==8 or i==10) and arr_brick[i].hit == 1:
							    arr_brick[i].hit = 2

							if(arr_brick[i].strength != 0 and arr_brick[i].strength != 5):
							    if (i==4 or i==8 or i==10) and arr_brick[i].hit == 2:
							        arr_brick[i].strength = arr_brick[i].strength - 1
							    elif (i!=4 and i!=8 and i!=10):
							        arr_brick[i].strength = arr_brick[i].strength - 1

							if(arr_brick[i].strength == 0):
								paddle.score = paddle.score + 5

						# Collides on lower surface of the brick
						elif(self.y == (arr_brick[i].y + arr_brick[i].height)):
							self.disappear = 1
							# First hit for Rainbow brick
							if (i==4 or i==8 or i==10) and arr_brick[i].hit == 0:
							    arr_brick[i].hit = 1
							# Second hit onwards strength can decrease for Rainbow brick
							if (i==4 or i==8 or i==10) and arr_brick[i].hit == 1:
							    arr_brick[i].hit = 2

							if(arr_brick[i].strength != 0 and arr_brick[i].strength != 5):
							    if (i==4 or i==8 or i==10) and arr_brick[i].hit == 2:
							        arr_brick[i].strength = arr_brick[i].strength - 1
							    elif (i!=4 and i!=8 and i!=10):
							        arr_brick[i].strength = arr_brick[i].strength - 1

							if(arr_brick[i].strength == 0):
								paddle.score = paddle.score + 5

						# Collision on side surface of the brick
						elif(self.y >= arr_brick[i].y and self.y <= (arr_brick[i].y + arr_brick[i].height)):
							self.disappear = 1
							# First hit for Rainbow brick
							if (i==4 or i==8 or i==10) and arr_brick[i].hit == 0:
							    arr_brick[i].hit = 1
							# Second hit onwards strength can decrease for Rainbow brick
							if (i==4 or i==8 or i==10) and arr_brick[i].hit == 1:
							    arr_brick[i].hit = 2

							if(arr_brick[i].strength != 0 and arr_brick[i].strength != 5):
							    if (i==4 or i==8 or i==10) and arr_brick[i].hit == 2:
							        arr_brick[i].strength = arr_brick[i].strength - 1
							    elif (i!=4 and i!=8 and i!=10):
							        arr_brick[i].strength = arr_brick[i].strength - 1

							if(arr_brick[i].strength == 0):
								paddle.score = paddle.score + 5

		# For level 2
		if level.value==2:
		    for i in range(13,len(arr_brick)):
		        if(arr_brick[i].strength != 0):
		            if(self.x >= arr_brick[i].x and self.x <= (arr_brick[i].x + arr_brick[i].width)):
		                
		                # Collides on upper surface of the brick
		                if(self.y + self.height == arr_brick[i].y):
		                	self.disappear = 1
		                	os.system('aplay -q ./sound/shoot.wav&')
		                	if (i==14 or i==25 or i==26 or i==29 or i==31) and arr_brick[i].hit == 0:
		                		arr_brick[i].hit = 1
		                	if (i==14 or i==25 or i==26 or i==29 or i==31) and arr_brick[i].hit == 1:
		                		arr_brick[i].hit = 2

		                	if(arr_brick[i].strength != 0 and arr_brick[i].strength != 5):
		                		if (i==14 or i==25 or i==26 or i==29 or i==31) and arr_brick[i].hit == 2:
		                			arr_brick[i].strength = arr_brick[i].strength - 1
		                		elif (i!=14 and i!=25 and i!=26 and i!=29 and i!=31):
		                			arr_brick[i].strength = arr_brick[i].strength - 1
		                	if(arr_brick[i].strength == 0):
		                		paddle.score = paddle.score + 5

		                # Collides on lower surface of the brick
		                elif(self.y == (arr_brick[i].y + arr_brick[i].height)):
		                	self.disappear = 1
		                	os.system('aplay -q ./sound/shoot.wav&')
		                	if (i==14 or i==25 or i==26 or i==29 or i==31) and arr_brick[i].hit == 0:
		                		arr_brick[i].hit = 1
		                	if (i==14 or i==25 or i==26 or i==29 or i==31) and arr_brick[i].hit == 1:
		                		arr_brick[i].hit = 2

		                	if(arr_brick[i].strength != 0 and arr_brick[i].strength != 5):
		                		if (i==14 or i==25 or i==26 or i==29 or i==31) and arr_brick[i].hit == 2:
		                			arr_brick[i].strength = arr_brick[i].strength - 1
		                		elif (i!=14 and i!=25 and i!=26 and i!=29 and i!=31):
		                			arr_brick[i].strength = arr_brick[i].strength - 1
		                	if(arr_brick[i].strength == 0):
		                		paddle.score = paddle.score + 5

		                # Collision on side surface of the brick
		                elif(self.y >= arr_brick[i].y and self.y <= (arr_brick[i].y + arr_brick[i].height)):
		                	self.disappear = 1
		                	os.system('aplay -q ./sound/shoot.wav&')
		                	if (i==14 or i==25 or i==26 or i==29 or i==31) and arr_brick[i].hit == 0:
		                		arr_brick[i].hit = 1
		                	if (i==14 or i==25 or i==26 or i==29 or i==31) and arr_brick[i].hit == 1:
		                		arr_brick[i].hit = 2

		                	if(arr_brick[i].strength != 0 and arr_brick[i].strength != 5):
		                		if (i==14 or i==25 or i==26 or i==29 or i==31) and arr_brick[i].hit == 2:
		                			arr_brick[i].strength = arr_brick[i].strength - 1
		                		elif (i!=14 and i!=25 and i!=26 and i!=29 and i!=31):
		                			arr_brick[i].strength = arr_brick[i].strength - 1
		                	if(arr_brick[i].strength == 0):
		                		paddle.score = paddle.score + 5

		# For level 3
		if level.value==3:
			for i in range(39,len(arr_brick)):
			    if(arr_brick[i].strength != 0):
			        if(self.x >= arr_brick[i].x and self.x <= (arr_brick[i].x + arr_brick[i].width)):
			            
			            # Collides on upper surface of the brick
			            if(self.y + self.height == arr_brick[i].y):
			            	self.disappear = 1
			            	os.system('aplay -q ./sound/shoot.wav&')
			            	if (i in rainbow_idx) and arr_brick[i].hit == 0:
			            		arr_brick[i].hit = 1
			            	if (i in rainbow_idx) and arr_brick[i].hit == 1:
			            		arr_brick[i].hit = 2

			            	if(arr_brick[i].strength != 0 and arr_brick[i].strength != 5):
			            		if (i in rainbow_idx) and arr_brick[i].hit == 2:
			            			arr_brick[i].strength = arr_brick[i].strength - 1
			            		elif (i not in rainbow_idx):
			            			arr_brick[i].strength = arr_brick[i].strength - 1
			            	if(arr_brick[i].strength == 0):
			            		paddle.score = paddle.score + 5

			                
			            # Collides on lower surface of the brick
			            elif(self.y == (arr_brick[i].y + arr_brick[i].height)):
			            	self.disappear = 1
			            	os.system('aplay -q ./sound/shoot.wav&')
			            	if (i in rainbow_idx) and arr_brick[i].hit == 0:
			            		arr_brick[i].hit = 1
			            	if (i in rainbow_idx) and arr_brick[i].hit == 1:
			            		arr_brick[i].hit = 2

			            	if(arr_brick[i].strength != 0 and arr_brick[i].strength != 5):
			            		if (i in rainbow_idx) and arr_brick[i].hit == 2:
			            			arr_brick[i].strength = arr_brick[i].strength - 1
			            		elif (i not in rainbow_idx):
			            			arr_brick[i].strength = arr_brick[i].strength - 1
			            	if(arr_brick[i].strength == 0):
			            		paddle.score = paddle.score + 5


			            # Collision on side surface of the brick
			            elif(self.y >= arr_brick[i].y and self.y <= (arr_brick[i].y + arr_brick[i].height)):
			            	self.disappear = 1
			            	os.system('aplay -q ./sound/shoot.wav&')
			            	if (i in rainbow_idx) and arr_brick[i].hit == 0:
			            		arr_brick[i].hit = 1
			            	if (i in rainbow_idx) and arr_brick[i].hit == 1:
			            		arr_brick[i].hit = 2

			            	if(arr_brick[i].strength != 0 and arr_brick[i].strength != 5):
			            		if (i in rainbow_idx) and arr_brick[i].hit == 2:
			            			arr_brick[i].strength = arr_brick[i].strength - 1
			            		elif (i not in rainbow_idx):
			            			arr_brick[i].strength = arr_brick[i].strength - 1
			            	if(arr_brick[i].strength == 0):
			            		paddle.score = paddle.score + 5

		if self.disappear == 0:
			self.y += self.vel




