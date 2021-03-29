from headers import *
from powerup import *

class Ball:
    def __init__(self,width,height,vel_x,vel_y,cord_x,cord_y,firstMove, rand_pos, fb):
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.width = width
        self.height = height
        self.through = 0
        self.grab = 0
        self.fb = fb
        self.collide = 0
        self.game_over = 0
        self.init_x = 0
        self.init_y = 0
        self.ufo = 0
        self.firstMove = firstMove
        self.rand_pos = rand_pos
    
    def move(self, paddle, brick_arr, lives, level, flag):
        # For the first move placing the ball at random position on paddle
        if self.firstMove == 0:
            self.cord_x = paddle.x + self.rand_pos
            self.cord_y = 34
            return

        if(self.vel_y == 0):
            self.vel_y = 1

        # Sideways collission
        if(self.cord_x>=163):
            os.system('aplay -q ./sound/collide.wav&')
            self.vel_x = -self.vel_x
        elif(self.cord_x<=20):
            os.system('aplay -q ./sound/collide.wav&')
            self.vel_x = -self.vel_x
        
        # Collission with floor
        k1 = self.vel_y
        if(self.cord_y>=44 - k1):
            os.system('aplay -q ./sound/loose_life.wav&')
            self.cord_x = 15
            self.cord_y = 35
            self.vel_y = 1
            self.vel_x = 0
            paddle.x = 30
            paddle.y = 35
            self.firstMove = 0
            lives.value = lives.value - 1
            self.rand_pos = np.random.randint(low=0, high=29)
            return

        # Collission with roof
        if(self.cord_y<=7):
            os.system('aplay -q ./sound/collide.wav&')
            self.vel_y = -self.vel_y

        # Collission with paddle
        k = self.vel_y
        if(self.cord_y == paddle.y - k):
            
            # Grab powerup not active
            if(self.grab == 0):
                # Assigning the velocity based on where the ball collides from the center
                if(self.cord_x <= paddle.x + 5 and self.cord_x >= paddle.x):
                    if(self.fb==1):
                        self.falling_bricks(flag)
                    os.system('aplay -q ./sound/collide.wav&')
                    self.vel_x = self.vel_x - 2
                    self.vel_y = -self.vel_y
                elif(self.cord_x <= paddle.x + 10 and self.cord_x > paddle.x + 5):
                    if(self.fb==1):
                        self.falling_bricks(flag)
                    os.system('aplay -q ./sound/collide.wav&')
                    self.vel_x = self.vel_x - 1
                    self.vel_y = -self.vel_y
                elif(self.cord_x <= paddle.x + 20 and self.cord_x > paddle.x + 10):
                    if(self.fb==1):
                        self.falling_bricks(flag)
                    os.system('aplay -q ./sound/collide.wav&')
                    self.vel_x = self.vel_x 
                    self.vel_y = -self.vel_y
                elif(self.cord_x <= paddle.x + 25 and self.cord_x > paddle.x + 20):
                    if(self.fb==1):
                        self.falling_bricks(flag)
                    os.system('aplay -q ./sound/collide.wav&')
                    self.vel_x = self.vel_x + 1
                    self.vel_y = -self.vel_y
                elif(self.cord_x <= paddle.x + (paddle.width) and self.cord_x > paddle.x + 25):
                    if(self.fb==1):
                        self.falling_bricks(flag)
                    os.system('aplay -q ./sound/collide.wav&')
                    self.vel_x = self.vel_x + 2
                    self.vel_y = -self.vel_y

            # If Paddle grab powerup becomes active
            elif(self.grab == 1):
                if(self.cord_x >= paddle.x and self.cord_x <= paddle.x + 30):
                    os.system('aplay -q ./sound/collide.wav&')
                    self.vel_x = 0
                    self.vel_y = 0
                    self.firstMove = 0
                    self.grab = 0


        # Collission with Brick
        else:
            self.collide = 0
            self.init_x = 0
            self.init_y = 0
            # For level 1
            if level.value==1:
                for i in range(len(arr_brick)):
                    if(arr_brick[i].strength != 0):
                        if(self.cord_x >= arr_brick[i].x and self.cord_x <= (arr_brick[i].x + arr_brick[i].width)):
                            
                            # Collides on upper surface of the brick
                            if(self.cord_y + self.height == arr_brick[i].y):
                                self.collide = 1
                                self.init_x = self.cord_x
                                self.init_y = self.cord_y
                                # First hit for Rainbow brick
                                if (i==4 or i==8 or i==10) and arr_brick[i].hit == 0:
                                    arr_brick[i].hit = 1
                                # Second hit onwards strength can decrease for Rainbow brick
                                if (i==4 or i==8 or i==10) and arr_brick[i].hit == 1:
                                    arr_brick[i].hit = 2
                                os.system('aplay -q ./sound/shoot.wav&')
                                if(self.through == 0):
                                    self.vel_y = -self.vel_y
                                
                                if(self.through == 1):
                                    if(arr_brick[i].strength != 0):
                                        arr_brick[i].strength = 0
                                        arr_brick[i].pow = 1
                                        f = 0
                                        if f==0:
                                            arr_brick[i].brick_velx = self.vel_x
                                            arr_brick[i].brick_vely = self.vel_y
                                            f=1
                                else:
                                    if(arr_brick[i].strength != 0 and arr_brick[i].strength != 5 ):
                                        if (i==4 or i==8 or i==10) and arr_brick[i].hit == 2:
                                            arr_brick[i].strength = arr_brick[i].strength - 1
                                        elif (i!=4 and i!=8 and i!=10):
                                            arr_brick[i].strength = arr_brick[i].strength - 1
                                        # arr_brick[i].strength = arr_brick[i].strength - 1
                                    if(arr_brick[i].strength == 0):
                                        arr_brick[i].pow = 1
                                        f = 0
                                        if f==0:
                                            arr_brick[i].brick_velx = self.vel_x
                                            arr_brick[i].brick_vely = self.vel_y
                                            f=1
                                        paddle.score = paddle.score + 5
                                        print(paddle.score)

                            # Collides on lower surface of the brick
                            elif(self.cord_y == (arr_brick[i].y + arr_brick[i].height)):
                                self.collide = 1
                                self.init_x = self.cord_x
                                self.init_y = self.cord_y
                                # First hit for Rainbow brick
                                if (i==4 or i==8 or i==10) and arr_brick[i].hit == 0:
                                    arr_brick[i].hit = 1
                                # Second hit onwards strength can decrease for Rainbow brick
                                if (i==4 or i==8 or i==10) and arr_brick[i].hit == 1:
                                    arr_brick[i].hit = 2
                                os.system('aplay -q ./sound/shoot.wav&')
                                if(self.through == 0):
                                    self.vel_y = -self.vel_y
                                
                                if(self.through == 1):
                                    if(arr_brick[i].strength != 0):
                                        arr_brick[i].strength = 0
                                        arr_brick[i].pow = 1
                                        f = 0
                                        if f==0:
                                            arr_brick[i].brick_velx = self.vel_x
                                            arr_brick[i].brick_vely = self.vel_y
                                            f=1
                                else:
                                    if(arr_brick[i].strength != 0 and arr_brick[i].strength != 5 ):
                                        if (i==4 or i==8 or i==10) and arr_brick[i].hit == 2:
                                            arr_brick[i].strength = arr_brick[i].strength - 1
                                        elif (i!=4 and i!=8 and i!=10):
                                            arr_brick[i].strength = arr_brick[i].strength - 1
                                    if(arr_brick[i].strength == 0):
                                        arr_brick[i].pow = 1
                                        f = 0
                                        if f==0:
                                            arr_brick[i].brick_velx = self.vel_x
                                            arr_brick[i].brick_vely = self.vel_y
                                            f=1
                                        paddle.score = paddle.score + 5

                            # Collision on side surface of the brick
                            elif(self.cord_y >= arr_brick[i].y and self.cord_y <= (arr_brick[i].y + arr_brick[i].height)):
                                self.collide = 1
                                self.init_x = self.cord_x
                                self.init_y = self.cord_y
                                # First hit for Rainbow brick
                                if (i==4 or i==8 or i==10) and arr_brick[i].hit == 0:
                                    arr_brick[i].hit = 1
                                # Second hit onwards strength can decrease for Rainbow brick
                                if (i==4 or i==8 or i==10) and arr_brick[i].hit == 1:
                                    arr_brick[i].hit = 2
                                os.system('aplay -q ./sound/shoot.wav&')
                                if(self.through == 0):
                                    self.vel_x = -self.vel_x
                                
                                if(self.through == 1):
                                    if(arr_brick[i].strength != 0):
                                        arr_brick[i].strength = 0
                                        arr_brick[i].pow = 1
                                        f = 0
                                        if f==0:
                                            arr_brick[i].brick_velx = self.vel_x
                                            arr_brick[i].brick_vely = self.vel_y
                                            f=1
                                else:
                                    if(arr_brick[i].strength != 0 and arr_brick[i].strength != 5 ):
                                        if (i==4 or i==8 or i==10) and arr_brick[i].hit == 2:
                                            arr_brick[i].strength = arr_brick[i].strength - 1
                                        elif (i!=4 and i!=8 and i!=10):
                                            arr_brick[i].strength = arr_brick[i].strength - 1
                                        # arr_brick[i].strength = arr_brick[i].strength - 1
                                    if(arr_brick[i].strength == 0):
                                        arr_brick[i].pow = 1
                                        f = 0
                                        if f==0:
                                            arr_brick[i].brick_velx = self.vel_x
                                            arr_brick[i].brick_vely = self.vel_y
                                            f=1
                                        paddle.score = paddle.score + 5
                
               
            # For level 2 
            if level.value==2:
                for i in range(13,len(arr_brick)):
                    if(arr_brick[i].strength != 0):
                        if(self.cord_x >= arr_brick[i].x and self.cord_x <= (arr_brick[i].x + arr_brick[i].width)):
                            
                            # Collides on upper surface of the brick
                            if(self.cord_y + self.height == arr_brick[i].y):
                                os.system('aplay -q ./sound/shoot.wav&')
                                self.collide = 1
                                self.init_x = self.cord_x
                                self.init_y = self.cord_y
                                # First hit for Rainbow brick
                                if (i==14 or i==25 or i==26 or i==29 or i==31) and arr_brick[i].hit == 0:
                                    arr_brick[i].hit = 1
                                # Second hit onwards strength can decrease for Rainbow brick
                                if (i==14 or i==25 or i==26 or i==29 or i==31) and arr_brick[i].hit == 1:
                                    arr_brick[i].hit = 2
                                
                                if(self.through == 0):
                                    self.vel_y = -self.vel_y
                                
                                if(self.through == 1):
                                    if(arr_brick[i].strength != 0):
                                        arr_brick[i].strength = 0
                                        arr_brick[i].pow = 1
                                        f = 0
                                        if f==0:
                                            arr_brick[i].brick_velx = self.vel_x
                                            arr_brick[i].brick_vely = self.vel_y
                                            f=1
                                else:
                                    if(arr_brick[i].strength != 0 and arr_brick[i].strength != 5 ):
                                        if (i==14 or i==25 or i==26 or i==29 or i==31) and arr_brick[i].hit == 2:
                                            arr_brick[i].strength = arr_brick[i].strength - 1
                                        elif (i!=14 and i!=25 and i!=26 and i!=29 and i!=31):
                                            arr_brick[i].strength = arr_brick[i].strength - 1
                                        # arr_brick[i].strength = arr_brick[i].strength - 1
                                    if(arr_brick[i].strength == 0):
                                        arr_brick[i].pow = 1
                                        f = 0
                                        if f==0:
                                            arr_brick[i].brick_velx = self.vel_x
                                            arr_brick[i].brick_vely = self.vel_y
                                            f=1
                                        paddle.score = paddle.score + 5
                                        print(paddle.score)

                                
                            # Collides on lower surface of the brick
                            elif(self.cord_y == (arr_brick[i].y + arr_brick[i].height)):
                                os.system('aplay -q ./sound/shoot.wav&')
                                self.collide = 1
                                self.init_x = self.cord_x
                                self.init_y = self.cord_y
                                # First hit for Rainbow brick
                                if (i==14 or i==25 or i==26 or i==29 or i==31) and arr_brick[i].hit == 0:
                                    arr_brick[i].hit = 1
                                # Second hit onwards strength can decrease for Rainbow brick
                                if (i==14 or i==25 or i==26 or i==29 or i==31) and arr_brick[i].hit == 1:
                                    arr_brick[i].hit = 2
                                
                                if(self.through == 0):
                                    self.vel_y = -self.vel_y
                                
                                if(self.through == 1):
                                    if(arr_brick[i].strength != 0):
                                        arr_brick[i].strength = 0
                                        arr_brick[i].pow = 1
                                        f = 0
                                        if f==0:
                                            arr_brick[i].brick_velx = self.vel_x
                                            arr_brick[i].brick_vely = self.vel_y
                                            f=1
                                else:
                                    if(arr_brick[i].strength != 0 and arr_brick[i].strength != 5 ):
                                        if (i==14 or i==25 or i==26 or i==29 or i==31) and arr_brick[i].hit == 2:
                                            arr_brick[i].strength = arr_brick[i].strength - 1
                                        elif (i!=14 and i!=25 and i!=26 and i!=29 and i!=31):
                                            arr_brick[i].strength = arr_brick[i].strength - 1
                                    if(arr_brick[i].strength == 0):
                                        arr_brick[i].pow = 1
                                        f = 0
                                        if f==0:
                                            arr_brick[i].brick_velx = self.vel_x
                                            arr_brick[i].brick_vely = self.vel_y
                                            f=1
                                        paddle.score = paddle.score + 5

                            # Collision on side surface of the brick
                            elif(self.cord_y >= arr_brick[i].y and self.cord_y <= (arr_brick[i].y + arr_brick[i].height)):
                                os.system('aplay -q ./sound/shoot.wav&')
                                self.collide = 1
                                self.init_x = self.cord_x
                                self.init_y = self.cord_y
                                # First hit for Rainbow brick
                                if (i==14 or i==25 or i==26 or i==29 or i==31) and arr_brick[i].hit == 0:
                                    arr_brick[i].hit = 1
                                # Second hit onwards strength can decrease for Rainbow brick
                                if (i==14 or i==25 or i==26 or i==29 or i==31) and arr_brick[i].hit == 1:
                                    arr_brick[i].hit = 2
                                
                                if(self.through == 0):
                                    self.vel_x = -self.vel_x
                                
                                if(self.through == 1):
                                    if(arr_brick[i].strength != 0):
                                        arr_brick[i].strength = 0
                                        arr_brick[i].pow = 1
                                        f = 0
                                        if f==0:
                                            arr_brick[i].brick_velx = self.vel_x
                                            arr_brick[i].brick_vely = self.vel_y
                                            f=1
                                else:
                                    if(arr_brick[i].strength != 0 and arr_brick[i].strength != 5 ):
                                        if (i==14 or i==25 or i==26 or i==29 or i==31) and arr_brick[i].hit == 2:
                                            arr_brick[i].strength = arr_brick[i].strength - 1
                                        elif (i!=14 and i!=25 and i!=26 and i!=29 and i!=31):
                                            arr_brick[i].strength = arr_brick[i].strength - 1
                                        # arr_brick[i].strength = arr_brick[i].strength - 1
                                    if(arr_brick[i].strength == 0):
                                        arr_brick[i].pow = 1
                                        f = 0
                                        if f==0:
                                            arr_brick[i].brick_velx = self.vel_x
                                            arr_brick[i].brick_vely = self.vel_y
                                            f=1
                                        paddle.score = paddle.score + 5

            # For level 3 - Boss level
            if level.value==3:
                for i in range(39,len(arr_brick)):
                    if(arr_brick[i].strength != 0):
                        if(self.cord_x >= arr_brick[i].x and self.cord_x <= (arr_brick[i].x + arr_brick[i].width)):
                            
                            # Collides on upper surface of the brick
                            if(self.cord_y + self.height == arr_brick[i].y):
                                os.system('aplay -q ./sound/shoot.wav&')
                                self.collide = 1
                                self.init_x = self.cord_x
                                self.init_y = self.cord_y
                                # # First hit for Rainbow brick
                                # if (i in rainbow_idx) and arr_brick[i].hit == 0:
                                #     arr_brick[i].hit = 1
                                # # Second hit onwards strength can decrease for Rainbow brick
                                # if (i in rainbow_idx) and arr_brick[i].hit == 1:
                                #     arr_brick[i].hit = 2
                                
                                if(self.through == 0):
                                    self.vel_y = -self.vel_y
                                
                                if(self.through == 1):
                                    if(arr_brick[i].strength != 0):
                                        arr_brick[i].strength = 0
                                        arr_brick[i].pow = 1
                                        arr_brick[i].brick_velx = self.vel_x
                                        arr_brick[i].brick_vely = self.vel_y
                                else:
                                    if(arr_brick[i].strength != 0 and arr_brick[i].strength != 5 ):
                                        # if (i in rainbow_idx) and arr_brick[i].hit == 2:
                                        #     arr_brick[i].strength = arr_brick[i].strength - 1
                                        # elif (i not in rainbow_idx):
                                        #     arr_brick[i].strength = arr_brick[i].strength - 1
                                        arr_brick[i].strength = arr_brick[i].strength - 1
                                    if(arr_brick[i].strength == 0):
                                        arr_brick[i].pow = 1
                                        arr_brick[i].brick_velx = self.vel_x
                                        arr_brick[i].brick_vely = self.vel_y
                                        paddle.score = paddle.score + 5
                                        print(paddle.score)

                                
                            # Collides on lower surface of the brick
                            elif(self.cord_y == (arr_brick[i].y + arr_brick[i].height)):
                                os.system('aplay -q ./sound/shoot.wav&')
                                self.collide = 1
                                self.init_x = self.cord_x
                                self.init_y = self.cord_y
                                # # First hit for Rainbow brick
                                # if (i in rainbow_idx) and arr_brick[i].hit == 0:
                                #     arr_brick[i].hit = 1
                                # # Second hit onwards strength can decrease for Rainbow brick
                                # if (i in rainbow_idx) and arr_brick[i].hit == 1:
                                #     arr_brick[i].hit = 2
                                
                                if(self.through == 0):
                                    self.vel_y = -self.vel_y
                                
                                if(self.through == 1):
                                    if(arr_brick[i].strength != 0):
                                        arr_brick[i].strength = 0
                                        arr_brick[i].pow = 1
                                        arr_brick[i].brick_velx = self.vel_x
                                        arr_brick[i].brick_vely = self.vel_y
                                else:
                                    if(arr_brick[i].strength != 0 and arr_brick[i].strength != 5 ):
                                        # if (i in rainbow_idx) and arr_brick[i].hit == 2:
                                        #     arr_brick[i].strength = arr_brick[i].strength - 1
                                        # elif (i not in rainbow_idx):
                                        #     arr_brick[i].strength = arr_brick[i].strength - 1
                                        arr_brick[i].strength = arr_brick[i].strength - 1
                                    if(arr_brick[i].strength == 0):
                                        arr_brick[i].pow = 1
                                        arr_brick[i].brick_velx = self.vel_x
                                        arr_brick[i].brick_vely = self.vel_y
                                        paddle.score = paddle.score + 5


                            # Collision on side surface of the brick
                            elif(self.cord_y >= arr_brick[i].y and self.cord_y <= (arr_brick[i].y + arr_brick[i].height)):
                                os.system('aplay -q ./sound/shoot.wav&')
                                self.collide = 1
                                self.init_x = self.cord_x
                                self.init_y = self.cord_y
                                # # First hit for Rainbow brick
                                # if (i in rainbow_idx) and arr_brick[i].hit == 0:
                                #     arr_brick[i].hit = 1
                                # # Second hit onwards strength can decrease for Rainbow brick
                                # if (i in rainbow_idx) and arr_brick[i].hit == 1:
                                #     arr_brick[i].hit = 2
                                
                                if(self.through == 0):
                                    self.vel_x = -self.vel_x
                                
                                if(self.through == 1):
                                    if(arr_brick[i].strength != 0):
                                        arr_brick[i].strength = 0
                                        arr_brick[i].pow = 1
                                        arr_brick[i].brick_velx = self.vel_x
                                        arr_brick[i].brick_vely = self.vel_y
                                else:
                                    if(arr_brick[i].strength != 0 and arr_brick[i].strength != 5 ):
                                        # if (i in rainbow_idx) and arr_brick[i].hit == 2:
                                        #     arr_brick[i].strength = arr_brick[i].strength - 1
                                        # elif (i not in rainbow_idx):
                                        #     arr_brick[i].strength = arr_brick[i].strength - 1
                                        arr_brick[i].strength = arr_brick[i].strength - 1
                                    if(arr_brick[i].strength == 0):
                                        arr_brick[i].pow = 1
                                        arr_brick[i].brick_velx = self.vel_x
                                        arr_brick[i].brick_vely = self.vel_y
                                        paddle.score = paddle.score + 5

        self.cord_y += self.vel_y
        self.cord_x += self.vel_x


    def ball_movement(self, char, paddle, array, lives, level, flag):
        # function call for setting the position of bal, on paddle
        if self.firstMove == 0:
            self.move(paddle, array, lives, level, flag)
    
        # To release the ball on pressing b
        if self.firstMove == 0 and char == 'b':
            self.move(paddle, array, lives, level, flag)
            self.firstMove = 1

        # function call after each ball paddle collision
        if self.firstMove == 1:
            self.move(paddle, array, lives, level, flag)
        
    def display(self, color, symbol, arr):
        y = self.cord_y
        h = self.height
        w = self.width
        x = self.cord_x
        for i in range(y, y+h):
            arr[i] = arr[i][:x] + color + symbol*w + Fore.RESET + Back.RESET + arr[i][x+w:]
        return arr    

    # For each brick paddle collision after 30 sec, brick grid shifts down by 1 unit
    def falling_bricks(self, flag):
        if flag == 1:
            for i in range(len(arr_brick)):
                arr_brick[i].y += 1
                if arr_brick[i].y == 34 and arr_brick[i].strength!=0:
                    self.game_over = 1

        if flag == 2:
            for i in range(13, len(arr_brick)):
                arr_brick[i].y += 1
                if arr_brick[i].y == 34 and arr_brick[i].strength!=0:
                    self.game_over = 1

        if flag == 3:
            for i in range(39, len(arr_brick)-1):
                arr_brick[i].y += 1
                if arr_brick[i].y == 34 and arr_brick[i].strength!=0:
                    self.game_over = 1