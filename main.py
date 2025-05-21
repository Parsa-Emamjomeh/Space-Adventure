# some of the game assets such as images and sounds are from open source websites which are free for non-commercial use and are copy_right free.
# some parts of the code was enhanced by AI tools.

import pygame
from os.path import join
import random
from random import randint
from operator import add, sub

pygame.init()  # Initial setup of pygame
pygame.mixer.init() #initial setup of mixer in pygame lib
pygame.font.init() # initial setup of fonts in pygame lib

window_width = 960
window_height = 540
pygame.display.set_caption("SPACE ADVENTURE")  # GAME NAME
screen = pygame.display.set_mode((window_width, window_height)) #creating the game window


font_title = pygame.font.Font(join("static", "font", "Ethnocentric Rg It.otf"), 50)
font_text = pygame.font.SysFont("sans", 30)
game_state = "menu" # variable to check game state 
score = 0
run = True
clock = pygame.time.Clock()


# Animation variables set up
current_frame = 0
animation_speed = 0.1  # Set up the animation speed (could be changed later)

# Loading images, text, rectangles and variables for game objects:

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


# Functions:
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

pygame.quit()
