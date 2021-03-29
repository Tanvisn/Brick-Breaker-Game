from headers import *
class PowerUp:
    def __init__(self, width, height, x, y):
        self.x = x
        self.y = y
        self.vel = 1
        self.width = width
        self.height = height
        self.active = 0
        self.fl = 0
        self.type = 0
        self.life = 0
        self.color = ''
        self.symb = ''
        self.pow_velx = 0
        self.pow_vely = 0
        self.start_time = 0
        self.level=0

    def power_active():
        pass

    def power_deactive():
        pass

    def fall(self, paddle):
        if(self.y < 43):
            self.y = self.y + self.vel
        elif(self.active == 0 and self.y >=43):
            self.active = -1

        if(self.y == paddle.y - 1 and self.x >= paddle.x and self.x <= paddle.x + paddle.width):
            self.active = 1

    def show_powerup(self, color, symbol, arr):
        y = self.y
        h = self.height
        w = self.width
        x = self.x
        for i in range(y, y+h):
            arr[i] = arr[i][:x] + color + symbol*w + Fore.RESET + Back.RESET + arr[i][x+w:]
        return arr

class ExpandPaddle(PowerUp):
    def __init__(self, width, height, x, y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        PowerUp.__init__(self, width, height, x, y)

    def power_active(self, ball, paddle, start_time, lives):
        self.active = 1
        self.life = lives.value
        paddle.width = paddle.width + 5
        self.start_time = start_time
        self.fl = 1

    def power_deactive(self, ball, paddle, brick):
        self.active = -1
        paddle.width = paddle.width - 5
        brick.pow = -1


class ShrinkPaddle(PowerUp):
    def __init__(self, width, height, x, y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        PowerUp.__init__(self, width, height, x, y)

    def power_active(self, ball, paddle, start_time, lives):
        self.active = 1
        self.life = lives.value
        paddle.width = paddle.width - 5
        self.start_time = start_time
        self.fl = 1

    def power_deactive(self, ball, paddle, brick):
        self.active = 0
        paddle.width = paddle.width + 5
        brick.pow = -1

class FastBall(PowerUp):
    def __init__(self, width, height, x, y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        PowerUp.__init__(self, width, height, x, y)

    def power_active(self, ball, paddle, start_time, lives):
        self.active = 1

        if(ball.vel_y < 0):
            ball.vel_y = ball.vel_y - 1
        else:
            ball.vel_y = ball.vel_y + 1

        self.life = lives.value
        self.start_time = start_time
        self.fl = 1

    def power_deactive(self, ball, paddle, brick):
        self.active = 0

        if(ball.vel_y < 0):
            ball.vel_y = ball.vel_y + 1
        else:
            ball.vel_y = ball.vel_y - 1

        brick.pow = -1

class ThruBall(PowerUp):
    def __init__(self, width, height, x, y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        PowerUp.__init__(self, width, height, x, y)

    def power_active(self, ball, paddle, start_time, lives):
        self.active = 1
        self.life = lives.value
        ball.through = 1
        self.start_time = start_time
        self.fl = 1

    def power_deactive(self, ball, paddle, brick):
        self.active = 0
        ball.through = 0
        brick.pow = -1

class PaddleGrab(PowerUp):
    def __init__(self, width, height, x, y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        PowerUp.__init__(self, width, height, x, y)

    def power_active(self, ball, paddle, start_time, lives):
        self.active = 1
        self.life = lives.value
        ball.grab = 1
        self.start_time = start_time
        self.fl = 1

    def power_deactive(self, ball, paddle, brick):
        self.active = 0
        ball.grab = 0
        brick.pow = -1

class BulletShoot(PowerUp):
    def __init__(self, width, height, x, y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        PowerUp.__init__(self, width, height, x, y)

    def power_active(self, ball, paddle, start_time, lives):
        self.active = 1
        self.life = lives.value
        paddle.gun_display = 1
        self.start_time = start_time
        self.fl = 1

    def power_deactive(self, ball, paddle, brick):
        self.active = 0
        paddle.gun_display = 0
        brick.pow = -1

        
