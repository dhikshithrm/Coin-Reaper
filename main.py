import pygame
import random
import math

from pygame import mixer

# initiate the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("background.jpg")

# music
mixer.music.load('Power Bots Loop.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Coin Reaper")
icon = pygame.image.load('coin.png')
pygame.display.set_icon(icon)

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)


# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))



def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 250, 25))
    screen.blit(over_text, (200, 250))


# Player
playerImg = pygame.image.load("star.png")
playerX = random.randint(0, 776)
playerY = random.randint(0, 576)
playerX_change = 0
playerY_change = 0


def player(playerX, playerY):
    screen.blit(playerImg, (playerX, playerY))


# Coins
coinImg = pygame.image.load("coin.png")
coinX = random.randint(151, 776)
coinY = random.randint(151, 576)


def coin(coinX, coinY):
    screen.blit(coinImg, (coinX, coinY))


# Fire
fireImg = pygame.image.load("fire (1).png")
fireX = random.randint(0, 150)
fireY = random.randint(0, 150)
fireX_change = 1.1
fireY_change = 1.1


def fire(fireX, fireY):
    screen.blit(fireImg, (fireX, fireY))


# CollisionDittector
def is_collision(playerX, playerY, coinX, coinY):
    distance = math.sqrt(math.pow(playerX - coinX, 2) + math.pow(playerY - coinY, 2))
    return distance < 32


# OutDetecter
def is_out(playerX, playerY, fireX, fireY):
    dis = math.sqrt(math.pow(playerX - fireX, 2) + math.pow(playerY - fireY, 2))
    return dis < 20

# Game Loop
gamer = True
playagain = True
while playagain:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           playagain = False
    while gamer:
        screen.fill((0, 0, 0))
        # Background Image
        screen.blit(background, (0, 0))
        show_score(10, 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamer = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -2
                if event.key == pygame.K_RIGHT:
                    playerX_change = 2
                if event.key == pygame.K_UP:
                    playerY_change = -2
                if event.key == pygame.K_DOWN:
                    playerY_change = 2
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_DOWN or
                    event.key == pygame.K_UP or
                    event.key == pygame.K_LEFT or
                    event.key == pygame.K_RIGHT):
                    playerX_change = 0
                    playerY_change = 0
        collision = is_collision(playerX, playerY, coinX, coinY)
        if collision:
            knifecut = mixer.Sound('1432.wav')
            knifecut.play()
            score_value += 1
            coinX = random.randint(151, 781)
            coinY = random.randint(151, 581)
            coin(coinX, coinY)
        if 0 <= playerX <= 799 and 0 <= playerY <= 599:
            playerX += playerX_change
            playerY += playerY_change
        else:
            playerX = random.randint(0, 799)
            playerY = random.randint(0, 599)
        if score_value <= 3:
            fireX += fireX_change
            fireY += fireY_change
            if fireX <= 0 or fireX >= 799 or fireY <= 0 or fireY >= 599:
                fireX = random.randint(0, 150)
                fireY = random.randint(0, 150)
                fire(fireX, fireY)
        else:
            fireX += math.atan(0.2 * score_value) + 2
            fireY += math.atan(0.2 * score_value) + 2
            if fireX <= 0 or fireX >= 799 or fireY <= 0 or fireY >= 599:
                fireX = random.randint(0, 150)
                fireY = random.randint(0, 150)
                fire(fireX, fireY)
        # Gamer
        outbreak = is_out(playerX, playerY, fireX, fireY)
        if outbreak:
            game_over_text()
            show_score(245, 320)
            coinX = 2000
            coinY = 2000
            fireX = 2000
            fireY = 2000
            gamer = False
        player(playerX, playerY)
        coin(coinX, coinY)
        fire(fireX, fireY)
        pygame.display.update()
