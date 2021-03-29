from headers import *
from brick import *
from powerup import *
from paddle import *

class ShootTime:
    def __init__(self,x,y,start_time):
        self.x = x
        self.y = y
        self.start_time = start_time

    def display(self, color, symbol, arr):
        y = self.y
        # h = self.height
        x = self.x
        mytime = str(10 - (int(time.time() - self.start_time)))
        
        arr[y] = arr[i][:x] + color + symbol + ' ' + mytime + ' seconds' + Fore.RESET + Back.RESET + arr[i][x+18:]
        return arr

class Time:
    def __init__(self,x,y,start_time):
        self.x = x
        self.y = y
        self.start_time = start_time

    def display(self, color, symbol, arr):
        y = self.y
        # h = self.height
        x = self.x
        mytime = str(int(time.time() - self.start_time))
        
        arr[y] = arr[i][:x] + color + symbol + ' ' + mytime + ' seconds' + Fore.RESET + Back.RESET + arr[i][x+18:]
        return arr
        
class Wall:
    def __init__(self, width, height,x,y):
        super().__init__()
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

class Lives:
    def __init__(self,value,x,y):
        self.x = x
        self.y = y
        # self.height = height
        self.value = value

    def display(self, color, symbol, arr):
        y = self.y
        x = self.x
        val = str(self.value)
        arr[y] = arr[i][:x] + color + symbol + ' ' + val + Fore.RESET + Back.RESET + arr[i][x+8:]
        return arr

class UFOHealth:
    def __init__(self,value,x,y):
        self.x = x
        self.y = y
        self.value = value

    def display(self, color, symbol, arr):
        y = self.y
        x = self.x
        val = str(arr_brick[len(arr_brick)-1].strength)
        arr[y] = arr[i][:x] + color + symbol + ' ' + val + Fore.RESET + Back.RESET + arr[i][x+8:]
        return arr

class Level:
    def __init__(self,value,x,y):
        self.x = x
        self.y = y
        self.value = value

    def display(self, color, symbol, arr):
        y = self.y
        x = self.x
        val = str(self.value)
        arr[y] = arr[i][:x] + color + symbol + ' ' + val + Fore.RESET + Back.RESET + arr[i][x+8:]
        return arr

class Score:
    def __init__(self,paddle,x,y):
        self.x = x
        self.y = y
        self.value = paddle.score

    def display(self, color, symbol, arr, paddle):
        y = self.y
        x = self.x
        val = str(paddle.score)
        arr[y] = arr[i][:x] + color + symbol + ' ' + val + Fore.RESET + Back.RESET + arr[i][x+8:]
        return arr


class MyBricks:
    # Strength:- LIGHTBLUE = 1, LIGHTGREEN=2, LIGHTRED=3, LIGHTBLACK = 5
    # Brick(width, height, y, x, strength)
    # Index 0 to 12
    # Bricks for level 1
    def create_bricks1(self):
        self.bA35 = Brick(5, 1, 14, 104, 5)
        arr_brick.append(self.bA35)
        self.bA23 = Brick(5, 1, 12, 98, 2)
        arr_brick.append(self.bA23)
        self.bA34 = Brick(5, 1, 14, 98, 1)
        arr_brick.append(self.bA34)
        self.bA43 = Brick(5, 1, 16, 98, 5)
        arr_brick.append(self.bA43)
        self.bA11 = RainbowBrick(5, 1, 10, 92, 1, 0)
        arr_brick.append(self.bA11)
        self.bA22 = Brick(5, 1, 12, 92, 3)
        arr_brick.append(self.bA22)
        self.bA33 = Brick(5, 1, 14, 92, 2)
        arr_brick.append(self.bA33)
        self.bA42 = Brick(5, 1, 16, 92, 3)
        arr_brick.append(self.bA42)
        self.bA51 = RainbowBrick(5, 1, 18, 92, 1, 0)
        arr_brick.append(self.bA51)
        self.bA21 = Brick(5, 1, 12, 86, 5)
        arr_brick.append(self.bA21)
        self.bA32 = RainbowBrick(5, 1, 14, 86, 1, 0)
        arr_brick.append(self.bA32)
        self.bA41 = Brick(5, 1, 16, 86, 2)
        arr_brick.append(self.bA41)
        self.bA31 = Brick(5, 1, 14, 80, 3)
        arr_brick.append(self.bA31)

    # Index 13 to 38
    # Bricks for level 2
    def create_bricks2(self):
        self.bB35 = Brick(5, 1, 14, 134, 5)
        arr_brick.append(self.bB35)
        self.bB23 = RainbowBrick(5, 1, 12, 128, 2, 0)
        arr_brick.append(self.bB23)
        self.bB34 = Brick(5, 1, 14, 128, 1)
        arr_brick.append(self.bB34)
        self.bB43 = Brick(5, 1, 16, 128, 5)
        arr_brick.append(self.bB43)
        self.bB11 = Brick(5, 1, 10, 122, 1)
        arr_brick.append(self.bB11)
        self.bB22 = Brick(5, 1, 12, 122, 3)
        arr_brick.append(self.bB22)
        self.bB33 = Brick(5, 1, 14, 122, 2)
        arr_brick.append(self.bB33)
        self.bB42 = Brick(5, 1, 16, 122, 3)
        arr_brick.append(self.bB42)
        self.bB51 = Brick(5, 1, 18, 122, 1)
        arr_brick.append(self.bB51)
        self.bB21 = Brick(5, 1, 12, 116, 5)
        arr_brick.append(self.bB21)
        self.bB32 = Brick(5, 1, 14, 116, 1)
        arr_brick.append(self.bB32)
        self.bB41 = Brick(5, 1, 16, 116, 2)
        arr_brick.append(self.bB41)
        self.bB31 = RainbowBrick(5, 1, 14, 110, 3, 0)
        arr_brick.append(self.bB31)


        self.bA35 = RainbowBrick(5, 1, 14, 84, 5, 0)
        arr_brick.append(self.bA35)
        self.bA23 = Brick(5, 1, 12, 78, 2)
        arr_brick.append(self.bA23)
        self.bA34 = Brick(5, 1, 14, 78, 1)
        arr_brick.append(self.bA34)
        self.bA43 = RainbowBrick(5, 1, 16, 78, 5, 0)
        arr_brick.append(self.bA43)
        self.bA11 = Brick(5, 1, 10, 72, 1)
        arr_brick.append(self.bA11)
        self.bA22 = RainbowBrick(5, 1, 12, 72, 3, 0)
        arr_brick.append(self.bA22)
        self.bA33 = Brick(5, 1, 14, 72, 2)
        arr_brick.append(self.bA33)
        self.bA42 = Brick(5, 1, 16, 72, 3)
        arr_brick.append(self.bA42)
        self.bA51 = Brick(5, 1, 18, 72, 1)
        arr_brick.append(self.bA51)
        self.bA21 = Brick(5, 1, 12, 66, 5)
        arr_brick.append(self.bA21)
        self.bA32 = Brick(5, 1, 14, 66, 1)
        arr_brick.append(self.bA32)
        self.bA41 = Brick(5, 1, 16, 66, 2)
        arr_brick.append(self.bA41)
        self.bA31 = Brick(5, 1, 14, 60, 3)
        arr_brick.append(self.bA31)

    # Index 39 onwards
    # Bricks for level 3
    def create_bricks3(self,paddle):
        self.bB35 = Brick(5, 1, 14, 154, 5)
        arr_brick.append(self.bB35)
        # self.bB23 = RainbowBrick(5, 1, 12, 148, 2, 0)
        # arr_brick.append(self.bB23)
        # self.bB34 = Brick(5, 1, 14, 148, 1)
        # arr_brick.append(self.bB34)
        # self.bB43 = Brick(5, 1, 16, 148, 5)
        # arr_brick.append(self.bB43)
        # self.bB11 = Brick(5, 1, 10, 142, 1)
        # arr_brick.append(self.bB11)
        # self.bB22 = Brick(5, 1, 12, 142, 3)
        # arr_brick.append(self.bB22)
        # self.bB33 = Brick(5, 1, 14, 142, 2)
        # arr_brick.append(self.bB33)
        # self.bB42 = Brick(5, 1, 16, 142, 3)
        # arr_brick.append(self.bB42)
        # self.bB51 = Brick(5, 1, 18, 142, 1)
        # arr_brick.append(self.bB51)
        # self.bB21 = RainbowBrick(5, 1, 12, 136, 5, 0)
        # arr_brick.append(self.bB21)
        self.bB32 = Brick(5, 1, 14, 136, 5)
        arr_brick.append(self.bB32)
        # self.bB41 = Brick(5, 1, 16, 136, 2)
        # arr_brick.append(self.bB41)
        self.bB31 = Brick(5, 1, 14, 130, 5)
        arr_brick.append(self.bB31)

        # self.bA35 = Brick(5, 1, 14, 104, 5)
        # arr_brick.append(self.bA35)
        self.bA23 = Brick(5, 1, 12, 98, 5)
        arr_brick.append(self.bA23)
        # self.bA34 = Brick(5, 1, 14, 98, 1)
        # arr_brick.append(self.bA34)
        # self.bA43 = RainbowBrick(5, 1, 16, 98, 5, 0)
        # arr_brick.append(self.bA43)
        # self.bA11 = Brick(5, 1, 10, 92, 1)
        # arr_brick.append(self.bA11)
        self.bA22 = Brick(5, 1, 12, 92, 5)
        arr_brick.append(self.bA22)
        # self.bA33 = Brick(5, 1, 14, 92, 2)
        # arr_brick.append(self.bA33)
        # self.bA42 = Brick(5, 1, 16, 92, 3)
        # arr_brick.append(self.bA42)
        # self.bA51 = Brick(5, 1, 18, 92, 1)
        # arr_brick.append(self.bA51)
        # self.bA21 = Brick(5, 1, 12, 86, 5)
        # arr_brick.append(self.bA21)
        # self.bA32 = Brick(5, 1, 14, 86, 1)
        # arr_brick.append(self.bA32)
        # self.bA41 = RainbowBrick(5, 1, 16, 86, 2, 0)
        # arr_brick.append(self.bA41)
        # self.bA31 = Brick(5, 1, 14, 80, 3)
        # arr_brick.append(self.bA31)

        # self.b35 = Brick(5, 1, 14, 54, 5)
        # arr_brick.append(self.b35)
        # self.b23 = Brick(5, 1, 12, 48, 2)
        # arr_brick.append(self.b23)
        # self.b34 = Brick(5, 1, 14, 48, 1)
        # arr_brick.append(self.b34)
        self.b43 = Brick(5, 1, 16, 48, 5)
        arr_brick.append(self.b43)
        # self.b11 = RainbowBrick(5, 1, 10, 42, 1, 0)
        # arr_brick.append(self.b11)
        # self.b22 = Brick(5, 1, 12, 42, 3)
        # arr_brick.append(self.b22)
        # self.b33 = RainbowBrick(5, 1, 14, 42, 2, 0)
        # arr_brick.append(self.b33)
        # self.b42 = Brick(5, 1, 16, 42, 3)
        # arr_brick.append(self.b42)
        # self.b51 = Brick(5, 1, 18, 42, 1)
        # arr_brick.append(self.b51)
        # self.b21 = Brick(5, 1, 12, 36, 5)
        # arr_brick.append(self.b21)
        # self.b32 = Brick(5, 1, 14, 36, 1)
        # arr_brick.append(self.b32)
        self.b41 = Brick(5, 1, 16, 36, 5)
        arr_brick.append(self.b41)
        # self.b31 = Brick(5, 1, 14, 30, 3)
        # arr_brick.append(self.b31)

        # UFO
        self.UFO = Brick(10,3,7,paddle.x,10)
        arr_brick.append(self.UFO)
        arr_brick[len(arr_brick)-1].ufo = 1

    # Display function for level 1
    def display_bricks1(self, arr, newPaddle,ball,lives,flag):
        for i in range(len(arr_brick)):
            if(arr_brick[i].strength == 5):
                arr = arr_brick[i].display(Back.LIGHTBLACK_EX, ' ', arr)
            elif(arr_brick[i].strength == 3):
                arr = arr_brick[i].display(Back.LIGHTRED_EX, ' ', arr)
            elif(arr_brick[i].strength == 2):
                arr = arr_brick[i].display(Back.LIGHTGREEN_EX, ' ', arr)
            elif(arr_brick[i].strength == 1):
                arr = arr_brick[i].display(Back.LIGHTBLUE_EX, ' ', arr)
            
            # Display powerups
            elif(arr_brick[i].strength == 0):
                
                num = i%8
                if(arr_brick[i].pow==1 and num!=0 and num <= 5):
                    if(num==1):
                        if(arr_brick[i].powerup == None):
                            arr_brick[i].powerup = ExpandPaddle(1, 1, arr_brick[i].x, arr_brick[i].y)
                    elif(num==2):
                        if(arr_brick[i].powerup == None):
                            arr_brick[i].powerup = ShrinkPaddle(1, 1, arr_brick[i].x, arr_brick[i].y)
                    elif(num==3):
                        if(arr_brick[i].powerup == None):
                            arr_brick[i].powerup = FastBall(1, 1, arr_brick[i].x, arr_brick[i].y)
                    elif(num==4):
                        if(arr_brick[i].powerup == None):
                            arr_brick[i].powerup = ThruBall(1, 1, arr_brick[i].x, arr_brick[i].y)
                    elif(num==5):
                        if(arr_brick[i].powerup == None):
                            arr_brick[i].powerup = PaddleGrab(1, 1, arr_brick[i].x, arr_brick[i].y)

                    elif(num==6):
                        if(arr_brick[i].powerup == None):
                            arr_brick[i].powerup = BulletShoot(1, 1, arr_brick[i].x, arr_brick[i].y)
                    
                    my_pow = arr_brick[i].powerup
                    my_pow.pow_velx = arr_brick[i].brick_velx
                    my_pow.pow_vely = arr_brick[i].brick_vely
                    my_pow.level = 1
                    
                    if(my_pow.type == 0):
                        if(my_pow.active == 0 and num==1):
                            my_pow.color = Back.RED
                            my_pow.symb = 'E'
                        
                        elif(my_pow.active == 0 and num==2):
                            my_pow.color = Back.CYAN
                            my_pow.symb = 'S'

                        elif(my_pow.active == 0 and num==3):
                            my_pow.color = Back.MAGENTA
                            my_pow.symb = 'F'

                        elif(my_pow.active == 0 and num==4):
                            my_pow.color = Back.GREEN
                            my_pow.symb = 'T'

                        elif(my_pow.active == 0 and num==5):
                            my_pow.color = Back.BLUE
                            my_pow.symb = 'P'

                        elif(my_pow.active == 0 and num==6):
                            my_pow.color = Back.BLUE
                            my_pow.symb = 'B'

                        my_pow.type = 1
                    
                    my_pow.fall(newPaddle)
                        
                    if(my_pow.active == 0):
                        my_pow.show_powerup(my_pow.color, my_pow.symb, arr)

                    if(my_pow.active == 1 and my_pow.fl == 0):
                        my_pow.power_active(ball, newPaddle, time.time(), lives)
                        newPaddle.st_time = my_pow.start_time                        

                    if(my_pow.active == 1):
                        if(lives.value != my_pow.life):
                            my_pow.power_deactive(ball, newPaddle, arr_brick[i])  
                        if(int(time.time()) - int(my_pow.start_time) >= 10):
                            my_pow.power_deactive(ball, newPaddle, arr_brick[i])


    # Display function for level 2
    def display_bricks2(self, arr, newPaddle,ball,lives, flag):
        for i in range(13, len(arr_brick)):
            if(arr_brick[i].strength == 5):
                arr = arr_brick[i].display(Back.LIGHTBLACK_EX, ' ', arr)
            elif(arr_brick[i].strength == 3):
                arr = arr_brick[i].display(Back.LIGHTRED_EX, ' ', arr)
            elif(arr_brick[i].strength == 2):
                arr = arr_brick[i].display(Back.LIGHTGREEN_EX, ' ', arr)
            elif(arr_brick[i].strength == 1):
                arr = arr_brick[i].display(Back.LIGHTBLUE_EX, ' ', arr)
            
            elif(arr_brick[i].strength == 0):
                
                num = i%17
                if(arr_brick[i].pow==1 and num!=0 and num <= 5):
                    if(num==1):
                        if(arr_brick[i].powerup == None):
                            arr_brick[i].powerup = ExpandPaddle(1, 1, arr_brick[i].x, arr_brick[i].y)
                            # arr_brick[i].powerup = BulletShoot(1, 1, arr_brick[i].x, arr_brick[i].y)
                    elif(num==2):
                        if(arr_brick[i].powerup == None):
                            arr_brick[i].powerup = ShrinkPaddle(1, 1, arr_brick[i].x, arr_brick[i].y)
                            # arr_brick[i].powerup = BulletShoot(1, 1, arr_brick[i].x, arr_brick[i].y)
                    elif(num==3):
                        if(arr_brick[i].powerup == None):
                            arr_brick[i].powerup = FastBall(1, 1, arr_brick[i].x, arr_brick[i].y)
                            # arr_brick[i].powerup = BulletShoot(1, 1, arr_brick[i].x, arr_brick[i].y)
                    elif(num==4):
                        if(arr_brick[i].powerup == None):
                            arr_brick[i].powerup = ThruBall(1, 1, arr_brick[i].x, arr_brick[i].y)
                            # arr_brick[i].powerup = BulletShoot(1, 1, arr_brick[i].x, arr_brick[i].y)
                    elif(num==5):
                        if(arr_brick[i].powerup == None):
                            arr_brick[i].powerup = PaddleGrab(1, 1, arr_brick[i].x, arr_brick[i].y)
                            # arr_brick[i].powerup = BulletShoot(1, 1, arr_brick[i].x, arr_brick[i].y)
                    elif(num==6):
                        if(arr_brick[i].powerup == None):
                            arr_brick[i].powerup = BulletShoot(1, 1, arr_brick[i].x, arr_brick[i].y)

                    
                    my_pow = arr_brick[i].powerup
                    my_pow.pow_velx = arr_brick[i].brick_velx
                    my_pow.pow_vely = arr_brick[i].brick_vely
                    my_pow.level = 2
                    
                    if(my_pow.type == 0):
                        if(my_pow.active == 0 and num==1):
                            my_pow.color = Back.RED
                            my_pow.symb = 'E'
                        
                        elif(my_pow.active == 0 and num==2):
                            my_pow.color = Back.CYAN
                            my_pow.symb = 'S'

                        elif(my_pow.active == 0 and num==3):
                            my_pow.color = Back.MAGENTA
                            my_pow.symb = 'F'

                        elif(my_pow.active == 0 and num==4):
                            my_pow.color = Back.GREEN
                            my_pow.symb = 'T'

                        elif(my_pow.active == 0 and num==5):
                            my_pow.color = Back.BLUE
                            my_pow.symb = 'P'

                        elif(my_pow.active == 0 and num==6):
                            my_pow.color = Back.BLUE
                            my_pow.symb = 'B'

                        my_pow.type = 1

                    
                    my_pow.fall(newPaddle)
                        
                    if(my_pow.active == 0):
                        my_pow.show_powerup(my_pow.color, my_pow.symb, arr)

                    if(my_pow.active == 1 and my_pow.fl == 0):
                        my_pow.power_active(ball, newPaddle, time.time(), lives)
                        newPaddle.st_time = my_pow.start_time                            

                    if(my_pow.active == 1):
                        if(lives.value != my_pow.life):
                            my_pow.power_deactive(ball, newPaddle, arr_brick[i])  
                        if(int(time.time()) - int(my_pow.start_time) >= 10):
                            my_pow.power_deactive(ball, newPaddle, arr_brick[i])
                        # Deactivate powerup on changing level
                        # if arr_brick[i].powerup.level != 2:
                        #     print('*************************************************')
                        #     arr_brick[i].powerup.power_deactive(ball, newPaddle, arr_brick[i])
                    
    
    def display_bricks3(self, arr, newPaddle,ball,lives, flag):
        for i in range(39,len(arr_brick)):
            # if arr_brick[i].powerup != None:
            #     if arr_brick[i].powerup.level != 3:
            #         arr_brick[i].powerup.power_deactive(ball, newPaddle, arr_brick[i])
            if(arr_brick[i].strength == 5 and arr_brick[i].ufo==0):
                arr = arr_brick[i].display(Back.LIGHTBLACK_EX, ' ', arr)
            elif(arr_brick[i].strength == 3 and arr_brick[i].ufo==0):
                arr = arr_brick[i].display(Back.LIGHTRED_EX, ' ', arr)
            elif(arr_brick[i].strength == 2 and arr_brick[i].ufo==0):
                arr = arr_brick[i].display(Back.LIGHTGREEN_EX, ' ', arr)
            elif(arr_brick[i].strength == 1 and arr_brick[i].ufo==0):
                arr = arr_brick[i].display(Back.LIGHTBLUE_EX, ' ', arr)
            elif(arr_brick[i].ufo==1):
                arr = arr_brick[i].display(Back.RED, ' ', arr)  
            
            elif(arr_brick[i].strength == 0):
                
                num = i%15
                if(arr_brick[i].pow==1 and num!=0 and num <= 5):
                    if(num==1):
                        if(arr_brick[i].powerup == None):
                            arr_brick[i].powerup = ExpandPaddle(1, 1, arr_brick[i].x, arr_brick[i].y)
                    elif(num==2):
                        if(arr_brick[i].powerup == None):
                            arr_brick[i].powerup = ShrinkPaddle(1, 1, arr_brick[i].x, arr_brick[i].y)
                    elif(num==3):
                        if(arr_brick[i].powerup == None):
                            arr_brick[i].powerup = FastBall(1, 1, arr_brick[i].x, arr_brick[i].y)
                    elif(num==4):
                        if(arr_brick[i].powerup == None):
                            arr_brick[i].powerup = ThruBall(1, 1, arr_brick[i].x, arr_brick[i].y)
                    elif(num==5):
                        if(arr_brick[i].powerup == None):
                            arr_brick[i].powerup = PaddleGrab(1, 1, arr_brick[i].x, arr_brick[i].y)
                    elif(num==6):
                        if(arr_brick[i].powerup == None):
                            arr_brick[i].powerup = BulletShoot(1, 1, arr_brick[i].x, arr_brick[i].y)


                    my_pow = arr_brick[i].powerup
                    my_pow.pow_velx = arr_brick[i].brick_velx
                    my_pow.pow_vely = arr_brick[i].brick_vely
                    my_pow.level = 3
                    
                    if(my_pow.type == 0):
                        if(my_pow.active == 0 and num==1):
                            my_pow.color = Back.RED
                            my_pow.symb = 'E'
                        
                        elif(my_pow.active == 0 and num==2):
                            my_pow.color = Back.CYAN
                            my_pow.symb = 'S'

                        elif(my_pow.active == 0 and num==3):
                            my_pow.color = Back.MAGENTA
                            my_pow.symb = 'F'

                        elif(my_pow.active == 0 and num==4):
                            my_pow.color = Back.GREEN
                            my_pow.symb = 'T'

                        elif(my_pow.active == 0 and num==5):
                            my_pow.color = Back.BLUE
                            my_pow.symb = 'P'
                        elif(my_pow.active == 0 and num==6):
                            my_pow.color = Back.BLUE
                            my_pow.symb = 'B'

                        my_pow.type = 1

                    
                    my_pow.fall(newPaddle)
                        
                    if(my_pow.active == 0):
                        my_pow.show_powerup(my_pow.color, my_pow.symb, arr)

                    if(my_pow.active == 1 and my_pow.fl == 0):
                        my_pow.power_active(ball, newPaddle, time.time(), lives)  
                        newPaddle.st_time = my_pow.start_time                      

                    if(my_pow.active == 1):
                        if(lives.value != my_pow.life):
                            my_pow.power_deactive(ball, newPaddle, arr_brick[i])  
                        if(int(time.time()) - int(my_pow.start_time) >= 10):
                            my_pow.power_deactive(ball, newPaddle, arr_brick[i])

                    
def component_display1(right_wall, newPaddle, myTime, myLives, myScore, myLevel, arr):
    arr = right_wall.display(Back.WHITE, ' ', arr)
    arr = newPaddle.display(Back.CYAN, ' ', arr)
    
    if newPaddle.gun_display == 1:

        myShooter2 = Shooter(1, 1, newPaddle.x + 30, 34)
        myShooter1 = Shooter(1, 1, newPaddle.x - 1, 34)
        
        arr = myShooter2.display(Back.MAGENTA, ' ', arr)
        arr = myShooter1.display(Back.MAGENTA, ' ', arr)
        
    
    arr = myLives.display(Back.GREEN, 'Lives:', arr)
    arr = myTime.display(Back.RED, 'Time:', arr)
    arr = myScore.display(Back.BLUE, 'Score:', arr, newPaddle)
    arr = myLevel.display(Back.BLACK, 'Level:', arr)    

def component_display2(myBall, upper_wall, left_wall, lower_wall, arr):
    arr = myBall.display(Back.YELLOW, ' ', arr)
    arr = upper_wall.display(Back.WHITE, ' ', arr)
    arr = left_wall.display(Back.WHITE, ' ', arr)
    arr = lower_wall.display(Back.WHITE, ' ', arr)

def change_color(rainbow_idx, flag, strength,str_idx):
    if flag!=0:
        if flag == 1:
            for i in range(3):
                if arr_brick[rainbow_idx[i]].hit==0:
                    arr_brick[rainbow_idx[i]].strength = strength[str_idx]

        if flag == 2:
            for i in range(3,8):
                if arr_brick[rainbow_idx[i]].hit==0:
                    arr_brick[rainbow_idx[i]].strength = strength[str_idx]
        
        # if flag == 3:
        #     for i in range(8,14):
        #         if arr_brick[rainbow_idx[i]].hit==0:
        #             arr_brick[rainbow_idx[i]].strength = strength[str_idx]

        
        

