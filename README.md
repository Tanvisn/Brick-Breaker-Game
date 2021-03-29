To start the game use the command (in the directory where all codes are present) -
python3 main.py

Description:
This is a terminal-based version of the old classic brick breaker game.
The player has to destroy the brick structure using a paddle and a ball. The paddle can be moved in the horizontal direction and is used as a bouncing platform for the ball.
A life is lost when the ball misses the paddle and touches the floor. The score is earned by breaking the bricks. The bricks are of different strengths which are represented by the colour variation.
Various powerups are hidden behind the bricks, which can be accessed by breaking the brick and catching the powerup using the paddle. The powerup will remain active for 10 seconds.
The upgraded version has 3 different levels with 3 different layouts. There is a new kind of brick called 'Rainbow brick' is added to the game. 
The Rainbow brick keeps on changing its color in each frame and the brick gets a fixed color once hit by the wall.
Another feature added to the game is Falling Bricks. After 30 seconds this feature gets activated. In this feature, for every ball and paddle collision the grid of bricks shifts 
one position downwards. Once the lowermost layer of the grid reaches the paddle's level the game is over.
The game also contains an additional paddle shooting powerup. In this powerup the paddle is able to shoot bullets towards the brick grid, each bullet on colliding with 
a brick decreases the strength of brick by 1. Also added the boss level.

In the new version special sound effects are added for different actions like ball and wall collision, ball and brick collision, powerup and paddle collision etc.
Rules:
1. Press the A key to move the paddle towards the left
2. Press the D key to move the paddle towards the right
3. Press the B key to release the ball from the paddle
4. The powerups deactivate after 10 seconds
5. If a life is lost, the active powerup becomes inactive
6. There are a total of 10 lives if all are exhausted then the game ends.
7. The powerups are as follows -
   	a.E denotes the Extend Paddle powerup which extends the length of the paddle
	b.S denotes the Shrink Paddle powerup which reduces the length of the paddle
	c.F denotes the Fast Ball powerup which increases the speed of the ball
	d.T denotes the Thru Ball powerup which allows the ball to cross any brick
	e.P denotes the Paddle Grab powerup which allows us to hold the ball on the paddle and release it later on.
8. The falling brick feature activates after 30 seconds
9. For changing the level of the game, press the key N.
10. Pressing the N key in the last level ends the game
11. For the shoot bullet powerup, shoot the bullet using the Space bar.

Game guide:
1. Move the paddle using the keys A and D, A moves the paddle towards the left and D moves it towards the right.
2. The ball bounces on the paddle and the velocity of the ball varies depending on at what distance from the centre of the paddle the ball has hit the paddle
3. The Red coloured bricks require 3 hits for breaking, Green bricks require 2 and Blue bricks require 1 hit to break.
4. The Black bricks are unbreakable.
5. The collision with the sidewalls and roof are elastic in nature, a life is lost when the ball touches the floor.
6. 5 points are rewarded for each brick broken.
7. The time of each play is displayed on the top left corner
8. Change the level using N key, pressing the key in last level ends the game.
9. After 30 seconds in game, the brick grid shifts downward by 1 coordinate for every paddle-ball collision.
  The game gets over when the lowest layer of the brick grid touches the paddle.
10. For the shooting paddle powerup, use spacebar to shoot bullets
11. The sounds added for different actions make the game more interesting
