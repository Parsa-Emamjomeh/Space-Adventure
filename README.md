# SPACE DVENTURE
#### Video Demo: [URL](https://youtu.be/FC6XkM39ZeM?si=ZCDP7UU-Su1n2P4z) 


## Project Description:

### *What is this game?*
#### its a space shooter game called `"SPACE ADVENTURE"`. it has a player which can move in 4 directions and the movement has animation. there are cup/coins which the player collects for points. there are space rocks which come from different directions and can eliminate the player if the player hits one. the are enemies with 2 different appearances that come down and try to hit the player to eliminate the player. as the speed of the rock and enemies increase as the game goes on so does the difficulty. the game has a main menu and a game over screen with the ability to to restart the game if game_over happens. it has sound effects for different interactions and it has music in the menu screen. the main goal of the player is to get points without dying, which he can do by blowing up rocks or enemies or collecting cups. all of this is implemented using `python` and `pygame-ce`.

### *Importing libraries*:
```python
import pygame
from os.path import join
import random
from random import randint
from operator import add, sub
```
 becuase this game is a `pygame` game, we need to `import pygame`.

 we need `join` from os to avoid mistakes in writing the paths when loading images/sound files.

 we need the random library several times, as randomness is needed for generating objects in our game. 

 we need the `add` and `sub` operatrs in order to rendomly ADD or SUBTRACT from a value later on.

### *Pygame Initialization :*
 ``` python
pygame.init()  
pygame.mixer.init()
pygame.font.init()
```
 these two lines are neede in order to initialize pygame and other features inside the pygame library.
 examples: mixer(for music), font 



### *Setup the game window/screen:*
```python
window_width = 960
window_height = 540
pygame.display.set_caption("SPACE ADVENTURE")
screen = pygame.display.set_mode((window_width, window_height))
```
 we first need to set variables for our screen, and then change the title of the pygame window which should be the game's name. 

 then we creat the game window and call it `screen`.

### *Variable Setup:*

```python
font_title = pygame.font.Font(join("static", "font", "Ethnocentric Rg It.otf"), 50)
font_text = pygame.font.SysFont("sans", 30)

game_state = "menu" 
score = 0
run = True

# animation variables 
current_frame = 0
animation_speed = 0.1

clock = pygame.time.Clock()
```
 first, we set up the two types of fonts we want to use, each one with different font and size.

 then we have an important variable for controling the game flow, `game_state`, which takes 3 values throughout the game: "menu", "playing", "game_over".

 we also define `score` which is crucial for counting and storing the player's score count.

 setting up `run = True` is important to make sure the main game loop is going to run. this variable is later used to control the main game loop.

 animation variables are defined to make sure we can have smooth movement animations. 

 and lastly in this section, we define `clock` which is going to be used to control the game.

### *Loading and setup of game objects:*

```python
#loading the background image 
background = pygame.image.load(join("static", "background", "background.png")).convert()

#loading the player's surfaces and rect
player_surf = pygame.image.load(join("static", "player", "spaceship1.png")).convert_alpha()
player_rect = player_surf.get_rect(center=(window_width / 2, (window_height / 2) + 150))
player_move = pygame.image.load(join("static", "player", "player_move.png")).convert_alpha()

#loading title + its rect
title = font_title.render("SPACE ADVENTURE", True, (0, 0, 255))
title_rect = title.get_rect(center=(window_width // 2, window_height // 2 - 90))

#loading play button + its rect
play_button_text = font_text.render("Press SPACE to Play", True, (255, 0, 0))
play_button_rect = play_button_text.get_rect(center=(window_width // 2, window_height // 2 + 20))

#loading the instructions + its rect 
instructions = font_text.render("press ARROW KEYS for movement and SPACE for shooting", True, (255, 255, 255))
instructions_rect = instructions.get_rect(center = (window_width / 2, window_height / 2 + 200))

#creating a variable and an empty list for stars 
star = pygame.image.load(join("static", "background", "star.png"))
star_pos = []

# creating and loading everything related to cup
cup = pygame.image.load(join("static", "objects", "cup.png")).convert_alpha()
cup_rect = cup.get_rect(center=(window_width // 2, 0))
cup_spawn_interval = randint(60, 1000)  # Random spawn interval between 60 and 1000 frames
cup_spawn_timer = 0  # Initialize the spawn timer
cup_exists = False
cup_speed = 1

# loading and creating everything related to rock
rock = pygame.image.load(join("static", "objects", "rock.png")).convert_alpha()
rock_rect = rock.get_rect(center=(window_width // 2, 0))
rock_spawn_interval = randint(30, 300)
rock_spawn_timer = 0
rock_exists = False
rock_speed = 1
rock_x_add = True

# loding and creating everything about enemy 
enemy_1 = pygame.image.load(join("static", "objects", "enemy1.png")).convert_alpha()
enemy_2 = pygame.image.load(join("static", "objects", "enemy2.png")).convert_alpha()
enemies = []  # List to store active enemies
enemy_spawn_interval = 60  # Spawn enemy every 120 frames
enemy_speed = 1

# craeting lists where we load the surfaces ralated to movement for animation
player_left_anim = [
    pygame.image.load(join("static", "player", "Turn_left.png")).convert_alpha(),
    pygame.image.load(join("static", "player", "Turn_left2.png")).convert_alpha()
]  
player_right_anim = [
    pygame.image.load(join("static", "player", "Turn_right.png")).convert_alpha(),
    pygame.image.load(join("static", "player", "Turn_right2.png")).convert_alpha()
]

#loading and defining everything related to the player when attacking 
player_attack = pygame.image.load(join("static", "player", "attack_player.png")).convert_alpha()
player_laser = pygame.image.load(join("static", "player", "laser.png")).convert_alpha()
laser_speed = 10
lasers = []  # List to store active lasers
```

In the first part we `load` (using pygame functionalities) the background image from the `background` directory which is inside another directory called `static`. 

we use the `.convert_alpha()` function on every `load` so all the transparent pixels in the `png` file is not rendered in our game.

then we load the `player_surf` which is the main look of our player. We also define `player_move` which is another look for our player when it's moving forwords. `player_rect` is also define here which is needed for moving or displaying our player later on.

Next, we render the `title` variable which is going to be our text displaying the game's title. the color and the text value itself is inside the `.render()` function. Right after that, we define `title_rect` which is needed for displaying our `title`.

 
On the next section, we do the same processes as for `title` but this time for the texts below it named `play_button_text` and `instructions`. These two describe what the player should do to start the game and what he should do to control the game. They both also have `rect` as they are neede to diaplay the text later on.

Next up, is the setup of `star` and `star_pos`. the variable `star` is just used to load the image of the star. And `star_pos` is a list to store the position values that is going to be generated randomly later.

In the next section we go through the process of defining some variables related to generating and controling `cup`. We also `load` the image of cup as well as giving it a `rect`.
`cup_spawn_timer` and `cup_spawn_nterval` is used to control the rate of cup generation and randomness of the time cup gets generated. Some other variables are also defined here which will be used later to control `cup` further.

Just like the last section, this section is going to initialize most of the variables realated to an object, in this case `rock`. becuase `cup` and `rock` are very similar objects, they mostly have the same set of variables defined for both of them. Both here, and in the last section , the use of `randint` is seen to choose a random integer between a set of values to define `spawn_interval`.
`rock_add_x` is different last section; this variable is used to track if we should add or subtract a value from rock's psition. which in turn makes it more random.

After that, we are creating all the variables for `enemy`. there are 2 types of enemy so `enemy_1` and `enemy_2` is used. then we have a list to store all of the active enemies in, which we could later remove if the player blows them up. Similar to last objects, enemy also has a `enemy_speed` and `enemy_spawn_interval` variable.

Next, we have 2 lists to store the surfaces of the turnning player. this helps us make all of animation work when the player is turnning right or left. 

Right after that, we have the variables for when the player is attacking with a laser. we load both the `player_attack` (player's surface when it's attacking) and `player_laser` (the image of the laser). we set a speed for the laser and initialize the list for storing all of lasers currently on the screen.

_we used the `.get_rect()` and `.get_frect()` functions many times to creat a rectangle for a given varibale. the value inside is often called `center` in this code, but it isn't always the center of the screen but sometimes has a distance from the center in order to keep all of the objects and text seperate._

_different directories were used to load the images above. the main directories in `static` are : `player`, `background`, `objects` and `sound`_.


### *Functions:*
```python
def generate_stars(): # generating stars with random location
    star_x = randint(-window_width, 0)
    star_y = randint(0, window_height)
    star_pos.append([star_x, star_y])

def draw_menu():  # Drawing the main menu screen with a play button and game title + stars
    screen.blit(background, (0, 0))
    
    for pos in star_pos:
        screen.blit(star, pos)

    screen.blit(title, title_rect)
    screen.blit(play_button_text, play_button_rect)
    screen.blit(instructions, instructions_rect)

def generate_cup(): # generates cups based on if a cup exists
    global cup_spawn_timer, cup_spawn_interval, cup_rect, cup_exists, cup_speed

    cup_spawn_timer += 1
    if cup_spawn_timer >= cup_spawn_interval and not cup_exists:
        cup_speed += 0.1
        cup_spawn_timer = 0
        cup_spawn_interval = randint(60, 1000)  # Reset spawn interval
        cup_exists = True
        cup_rect.midtop = (randint(0, window_width), 0)  # Respawn at random top location

def shoot_laser(): # creates laser
    global lasers

    laser_sound = pygame.mixer.music.load(join("static", "sound", "laser.mp3"))
    pygame.mixer.music.play()
    laser_rect = player_laser.get_rect(midbottom=player_rect.midtop)
    lasers.append(laser_rect)

def generate_rock(): #generating rock based on if rock exists
    global rock_spawn_interval, rock_spawn_timer, rock_rect, rock_exists, rock_x_add, rock_speed

    rock_spawn_timer += 1
    if rock_spawn_timer >= rock_spawn_interval and not rock_exists:
        rock_speed += 0.5
        rock_spawn_timer = 0
        rock_spawn_interval = randint(60, 1000)
        rock_exists = True
        rock_rect.midtop = (randint(0, window_width), 0)
        if  randint(1, 2) == 1 :
            rock_x_add = False
        else:
            rock_x_add = True

def generate_enemy(): #generates enemies on a random location close to player 
    global enemies, enemy_speed

    options = [add, sub]
    op = random.choice(options)
    space = randint(-150, 150)
    point = op(player_rect.x, space)
    enemy_speed += 0.001
    if randint(0, enemy_spawn_interval) == 0:
        enemy_type = randint(1, 2)
        if enemy_type == 1:
            enemy_rect = enemy_1.get_rect(midtop=(point, 0))
        else:
            enemy_rect = enemy_2.get_rect(midtop=(point, 0))
        enemies.append((enemy_rect, enemy_speed, enemy_type))  # Store enemy_type with the enemy

def reset_game(): # resets all the game variables for a restart 
    global score, player_rect, cup_exists, rock_exists, enemies, lasers, cup_speed, rock_speed, star_pos, enemy_speed

    score = 0
    player_rect.center = (window_width / 2, (window_height / 2) + 150)
    cup_exists = False
    rock_exists = False
    enemies.clear()
    cup_speed = 1
    rock_speed = 1
    enemy_speed = 1
    star_pos = []

def game_over(): # displays and handles game overs
    global game_state, run
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state = "menu"
                    reset_game()
                    return
                
        screen.blit(background, (0,0))
        game_over_text = font_title.render("GAME OVER", True, (255, 0, 0))
        score_display = font_text.render(f"YOUR SCORE: {score}", True, (255, 255, 255))
        restart_text = font_text.render("Press ESCAPE to restart", True, (255, 255, 255))
        quit_text = font_text.render("Close the window to Quit", True, (255, 255, 255))

        screen.blit(game_over_text, game_over_text.get_rect(center=(window_width // 2, window_height // 2 - 50)))
        screen.blit(score_display, score_display.get_rect(center=(window_width // 2, window_height // 2)))
        screen.blit(restart_text, restart_text.get_rect(center=(window_width // 2, window_height // 2 + 50)))
        screen.blit(quit_text, quit_text.get_rect(center=(window_width // 2, window_height // 2 + 100)))
        pygame.display.update()
        clock.tick(60)
```
First we have the `generate_stars()` fuction, which generated all of the stars in the background of the menu screen, at a random location. adn then it `.append()` the location into the list that we made earlier.

Next is the `draw_menu()` function. This function uses `.blit()` to display the background image which we loaded earlier onto the screen. Then it acsesses the items inside `star_pos` which was populated in the `generate_stars()` function to display all of those stars onto the screen. Additionally, this fuction displays the `title`, `play_button_text` and `instructions` on the screen to complete the looks of the menu.

Following that, we have the `generate_cup()` function. first it gets acsess to some global variables which we defined earlier, such as `cup_spawn_timer` and many more of the variables related to `cup`. Then, it increments the `cup_spawn_timer` by one and then it checks to see if has reached the value of `cup_spawn_interval` which determines if a cup should be generated or do we have to wait more. In the same _if statement_, the function checks to see if there is a cup currently on the screen. if there is not a cup on the screen and the time for spawning a cup is right, the fuction will generate one by first increasing the speed of the cup that is about to be generated slightly (to make everything harder as the game goes by) and then reseting all of the values for variables such as `cup_spawn_timer` and `cup_spawn_interval`. It also sets the value for `cup_exists` to `True`. Finally, it places the cup on a random point on the upper side of the screen. It does that by acsessing the `cup_rect` 's `midtop` and setting that value to that random value.

Up next we have the `shoot_laser()` function. it acsesses only one `global` variable which is the  list we defined earlier `lasers`. As the laser is shooted, the sound effect for it shold also be played. we first load the sound using the `mixer.music.load()` functionality of `pygame`. Then we play it once using the `mixer.music.play()` functionality. After the sound effect is done, the function creates a `rect` for the laser, and then it adds it to the `lasers` list, using the `.append()` function. 

Next is the `generate_rock()` function. this one is very similar to the `generate_cup()` function, as rock and cup are very similar objects. The function basically checks to see if the time is for creating a rock is in the prefered range, and it also checks to see if there is no rocks on the screen. if both of these conditions are met, then it increases rock_speed to make everything harder as time goes by, resets the time related rock variables, and moves rock to a random location on the top of the screen. but it randomly sets `rock_x_add` to `True` or `False`. this is becuase later we will use this variable to decide to add or subtract from the _x_ value (position's x) of the rock. this is becuase we want the rock to move in a diagonal line instead of a vertical line going straight down.

Moving on, is the `generate_enemy()` function. the role of this function is to generate an enemy with a random type (there are two types of enemies) at a random location near the player.
this function acsesses 2 global variables which we defined earlier, `enemies` which is an empty list and `enemy_speed` to make each enemy slightly faster to make the game harder with time. the first few lines are there to randomly generate a point 150 pixels to the right or to the left of the player's x position.  the use of `options` as a list of `operations` such as `add` and `sub` is a way of enabling the `op` varible to be a random choice between addition and subtraction. this is possible thanks to the `random` library which has the function `.choice()`. Finally for getting the point of spawn of the enemy, we have `op(player_rect.x, space)` which gives us the random point 150 pixels either side of the players x position.
Next the function checks to see if a random int between 0 and `enemy_spawn_interval` is equal to 0. this just narrows the chances of spawning an enemy. if that codition was met, then `enemy_type` is chosen randomly between 1 and 2, and a `enemy_rect` is created with that enemy type. Finally, all of `enemy_rect` , `enemy_speed` and `enemy_type` is added to the list `enemies` using `.append()`.

the next function is `reset_game()`. it resets all of the game variables that change during playing to the innitial ones so a new game could start. and also puts the player where it was at the start.

python
next we have `game_over()`. this function has a loop wich will run forever. inside this function, the user can close the game entirely by the use of:
 ```python 
 if event.type == pygame.QUIT:
                run= False
                return
```
and it can also set the `game_state` to "menu" which can restart the game when the "escape" key is pressed. Additionally, it displays the game over text and some other text. it also updates the screen and sets the clock to 60 frames.

### *Main Loop:*
```python
while run:
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            run = False        
        elif event.type == pygame.KEYDOWN:
            if game_state == "menu" and event.key == pygame.K_SPACE:
                game_state = "playing"
                pygame.mixer.music.stop() 
            elif game_state == "playing" and event.key == pygame.K_SPACE:
                shoot_laser()
        
    if game_state == "menu":
        if not pygame.mixer.music.get_busy():  # Check if music is not already playing
            background_music_menu = pygame.mixer.music.load(join("static", "sound", "background_title.mp3"))
            pygame.mixer.music.play(-1)  # Play music indefinitely

    if game_state == "menu":
        if randint(0, 100) < 10:  # 10% chance of spawning a new star
            generate_stars()

        # Move stars
        for i in range(len(star_pos)):
            star_pos[i][0] += 1  # Move star to the right

        draw_menu()

    elif game_state == "playing":
        screen.blit(background, (0, 0))

        # Update cup spawn
        if not cup_exists:
            generate_cup()

        # Move the cup down if it exists
        if cup_exists:
            cup_rect.y += cup_speed
            if cup_rect.top > window_height:
                cup_exists = False

            # Check for collision with player
            if player_rect.colliderect(cup_rect):
                score += 3
                cup_sound = pygame.mixer.music.load(join("static", "sound", "cup.mp3"))
                pygame.mixer.music.play()
                score_text = font_text.render(f"Score: {score}", True, (255, 255, 255))
                cup_exists = False

            # Draw cup
            screen.blit(cup, cup_rect)

        # Generate rock
        if not rock_exists:
            generate_rock()

        # Move rock
        if rock_exists:
            rock_rect.y += rock_speed
            if rock_x_add :
                rock_rect.x += 1
            else :
                rock_rect.x -= 1

            if rock_rect.top > window_height:
                rock_exists = False

            if player_rect.colliderect(rock_rect):
                loser_sound = pygame.mixer.music.load(join("static", "sound", "lose.mp3"))
                pygame.mixer.music.play()
                game_state = "game_over"
                game_over()


            screen.blit(rock, rock_rect)

        # Generate enemy
        generate_enemy()

        # Move enemies
        for enemy in enemies[:]:
            enemy_rect, speed, enemy_type = enemy
            enemy_rect.y += speed
            if enemy_rect.top > window_height:
                enemies.remove(enemy)

            if player_rect.colliderect(enemy_rect):
                loser_sound = pygame.mixer.music.load(join("static", "sound", "lose.mp3"))
                pygame.mixer.music.play()
                game_state = "game_over"
                game_over()


            screen.blit(enemy_1 if enemy_type == 1 else enemy_2, enemy_rect)

            # Check for collision with lasers
            for laser in lasers[:]:
                if laser.colliderect(enemy_rect):
                    score += 1

                    explosion_sound = pygame.mixer.music.load(join("static", "sound", "explosion.mp3"))
                    pygame.mixer.music.play()

                    score_text = font_text.render(f"Score: {score}", True, (255, 255, 255))
                    enemies.remove(enemy)
                    lasers.remove(laser)         
                                       

        # Move lasers
        for laser in lasers[:]:
            laser.y -= laser_speed
            if laser.bottom < 0:
                lasers.remove(laser)

            # Check for collision with rock
            if rock_exists and laser.colliderect(rock_rect):
                score += 1
                score_text = font_text.render(f"Score: {score}", True, (255, 255, 255))
                rock_exists = False
                lasers.remove(laser)

        # Draw lasers
        for laser in lasers:
            screen.blit(player_laser, laser)

        # Set up key presses
        keys = pygame.key.get_pressed()
        left_pressed = keys[pygame.K_LEFT]
        right_pressed = keys[pygame.K_RIGHT]
        up_pressed = keys[pygame.K_UP]
        down_pressed = keys[pygame.K_DOWN]
        space_pressed = keys[pygame.K_SPACE]

        # Move the player based on key presses
        if left_pressed and player_rect.left > 0:
            player_rect.left -= 5  # Increase movement speed
        elif right_pressed and player_rect.right < window_width:
            player_rect.left += 5  # Increase movement speed
        elif up_pressed and player_rect.top > 0:
            player_rect.top -= 5  # Increase movement speed
        elif down_pressed and player_rect.bottom < window_height:
            player_rect.top += 5  # Increase movement speed

        # Draw the player based on the key presses
        if left_pressed:
            current_frame += animation_speed
            if current_frame >= len(player_left_anim):
                current_frame = 0
            screen.blit(player_left_anim[int(current_frame)], player_rect)

        elif right_pressed:
            current_frame += animation_speed
            if current_frame >= len(player_right_anim):
                current_frame = 0
            screen.blit(player_right_anim[int(current_frame)], player_rect)

        elif up_pressed:
            screen.blit(player_move, player_rect)

        elif space_pressed:
            screen.blit(player_attack, player_rect)

        else:
            screen.blit(player_surf, player_rect)


    score_text = font_text.render(f"Score: {score}", True, (255, 255, 255))

    screen.blit(score_text, (10, 10))

    # Updating the display
    pygame.display.update()

    # Set the frame rate to 60
    clock.tick(60)
```

the main loop of the game is always runing, as long as `rin = True`. inside the main loop we have the `event loop` which checks for events such as the game being closed, or checking when SPACE is pressed so the `game_state` could change. It also has some music for when the menu is open.

further down, we see some of the logic behinde stars where `generate_stars()` function is called and we can also see how the stars are moved.

the `draw_menu()` function is also called here.

then we get into the logic of `cup`. the main loop checks to see if there is a cup, then it moves it down constantly, while its inside the boundries of the screen.

then collisions between cup and player is happening where if true, could play the sound effect, add the points and update the `score` variable.

after all of this we see when the cup is actually displayed using `.blit()`.

moing on, we see where `generate_rock()` is being called. most of the logic of rock and cup is similar as seen in the code.
but based on the `rock_x_add` a value is either added or subtracted from the rock's x position, which combined with the changing y position of the rock, make it move diagonaly.

then collisions are checked, and the player losses if the rock  touches him. so the sound effect is played and `game_over()` function is called. Shortly after these lines, the rock is displayed on the screen.

after this, the `generate_enemy()` function is called. and a loop goes through all the enemies in the list `enemies`. the enemies are moved until they go out of bounds.

then the collision of enemies with player is checked. if it is met, then a sound effect will be played and the `game_over()` function is called.

then the enemy is displayed on the screen based on the `enemy_type`.

below that, the collision with laser is check. if any of the enemies or the rocks touch the laser, the should be removed.

so the loop goes through each laser in `lasers` list and checks the collision. 
if the collision has happened, both the object(enemy , rock) and the laser should be removed, and points must be  added to `score`. also, a sound effect is played.

finnaly, each laser in the `lasers` list is drawn to the screen.

after this, some varibales are set to facilitate the use of keys in pur code. they use the `.K_KEY` fuctionality of `pygame`.

afterwords, the player movements are implemented, using the `current_frame` and `animation_speed` to smooth out the animation. and then the corresponding player image will be displayed from either of `player_left_anim` or `player_right_anim`.

this is repeated for all 4 directions of movement and with the `player_attack` when space is pressed.

finally, the score is updated for the last time  and displayed. 

the display is updated at the end of the loop using `.display.update()` functionality of `pygame`. and the frame rate of the clock is set to 60 for the last time.

### *The end:*
the last line of the code just makes sure we are closing out the pygame library, as we dont need it any more 
``` python
pygame.quit()
```