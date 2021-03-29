from headers import *
from paddle import *
from brick import *
from ball import *
from utility import *
from powerup import *

myPaddle = Paddle(30, 1)

myBall = Ball(1,1,0,1,15,34,0,np.random.randint(low=0, high=29),0)
myLives = Lives(10,2,1)
myLevel = Level(1,2,4)
myScore = Score(myPaddle,2,3)
myTime = Time(2,2,time.time())
myHealth = UFOHealth(10,2,5)
upper_wall = Wall(os.get_terminal_size().columns,1,0,6)
lower_wall = Wall(os.get_terminal_size().columns,1,0,43)
left_wall = Wall(2,37,18,7)
right_wall = Wall(2,37,165,7)

bricks = MyBricks()
# bricks.create_bricks()
flag = 0
construct_flag = 0
strength_flag = 0
strength = [1,2,3,5]
i = 0
s = 0
count = 0

while True:
    arr = copy.deepcopy(blank_arr)
    print("\033[H\033[J", end="")
    # Taking input from keyboard
    char = input_to()
    myPaddle.paddle_movement(char)
    myBall.ball_movement(char, myPaddle, arr, myLives, myLevel, flag)
    component_display1(right_wall, myPaddle, myTime, myLives, myScore, myLevel, arr)
    # change_levels(char, construct_flag, flag, myScore, bricks, myPaddle, myBall, myLives, myLevel)
    # Level 1
    if construct_flag == 0:
        bricks.create_bricks1()
        construct_flag = 1
        myLevel.value = 1
        flag = 1

    # Level 2
    if char == 'n' and flag==1:
        if construct_flag == 1:
            bricks.create_bricks2()
            construct_flag = 2
            myLevel.value = 2
            flag = 2

    # Level 3
    elif char == 'n' and flag==2:
        if construct_flag == 2:
            bricks.create_bricks3(myPaddle)
            construct_flag = 3
            myLevel.value = 3
            flag = 3
    
    # Changing the color of rainbow bricks
    change_color(rainbow_idx, flag, strength, i)
    i += 1
    if i == 4:
        i = 0
    
    # Pressing n in the last level ends the game
    if char == 'n' and flag==3:
        count += 1
        if count == 2:
            break

    # Rendering the bricks according to the levels
    if flag == 1:
        bricks.display_bricks1(arr,myPaddle,myBall,myLives,myLevel)
    elif flag == 2:
        bricks.display_bricks2(arr,myPaddle,myBall,myLives,myLevel)
    elif flag == 3:
        bricks.display_bricks3(arr,myPaddle,myBall,myLives,myLevel)
        arr_brick[len(arr_brick)-1].x = myPaddle.x
        arr = myHealth.display(Back.GREEN, 'Health:', arr)
        # myUFO = BossUFO(10,3,8,myPaddle.x,10)
        # myUFO.display(Back.MAGENTA, ' ', arr)

    # Activating fall brick
    if(time.time() - myTime.start_time) >= 30:
        myBall.fb = 1

    # If shooting paddle powerup is active, display shoot time and Nozels
    if myPaddle.gun_display == 1:
        myShootTime = ShootTime(2, 5, int(myPaddle.st_time))
        arr = myShootTime.display(Back.GREEN, 'Shoot:', arr)

    # Shooting Bullets
    if(myPaddle.gun_display==1 and char==' '):
        if int(time.time() - s) >= 1:
            myBullet = Bullet(1,1,myPaddle.x+30,34)
            bullet_arr.append(myBullet)
            myBullet = Bullet(1,1,myPaddle.x-1,34)
            bullet_arr.append(myBullet)
            s = int(time.time())        

    # Calling the shoot function for bullets stored in the array
    for j in range(len(bullet_arr)):
        if bullet_arr[j].disappear == 0:
            bullet_arr[j].display(Back.CYAN, ' ', arr)
            bullet_arr[j].shoot(myPaddle, myLevel)

    component_display2(myBall, upper_wall, left_wall, lower_wall, arr)
    arr = ''.join(arr)
    
    # Quitting the game
    if(myLives.value == 0):
        break
    if myBall.game_over == 1:
        break
    print(arr)
    time.sleep(t)


print('*************************************//GAME OVER//***********************************')

