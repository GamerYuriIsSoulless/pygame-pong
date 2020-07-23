import pygame, sys, random
pygame.font.init()

# Variables

screenWidth = 640
screenHeight = 480
white = (255, 255, 255)

ballSpeedX = 3.5 * random.choice((1, -1))
ballSpeedY = 3.5 * random.choice((1, -1))
playerVel = 0
playerTwoVel = 0
opponentVel = 3.5

# Functions
def ballAnimation():
    global ballSpeedX, ballSpeedY, playerScore, opponentScore
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    if ball.top <= 0 or ball.bottom >= screenHeight:
        ballSpeedY *= -1
    if ball.left <= 0:
        ballRestart()
        playerScore += 1
    if ball.right >= screenWidth:
        ballRestart()
        opponentScore += 1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ballSpeedX *= -1
        
def playerAnimation():
    player.y += playerVel
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screenHeight:
        player.bottom = screenHeight

def secondPlayerAnimation():
    opponent.y += playerTwoVel
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screenHeight:
        opponent.bottom = screenHeight

def opponentAnimation():
    if opponent.top < ball.y:
        opponent.top += opponentVel
    if opponent.bottom > ball.y:
        opponent.bottom -= opponentVel
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screenHeight:
        opponent.bottom = screenHeight

def ballRestart():
    global ballSpeedX, ballSpeedY
    ball.center = (screenWidth / 2, screenHeight / 2)
    ballSpeedY *= random.choice((1 , -1))
    ballSpeedX *= random.choice((1, -1))

# Main Setup
pygame.init()
clock = pygame.time.Clock()

# Window Setup
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('Pong')

# Rects
ball = pygame.Rect(screenWidth / 2 - 7.5, screenHeight / 2 - 7.5, 15, 15)
player = pygame.Rect(screenWidth - 20, screenHeight / 2 - 35, 10, 70)
opponent = pygame.Rect(10, screenHeight / 2 - 35, 10, 70)
    
# Main Loop
mainFont = pygame.font.SysFont('Arial', 40)
playerScore = 0
opponentScore = 0
secondPlayer = False
run = True
while run:
    
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerVel += 3.5
            if event.key == pygame.K_UP:
                playerVel -= 3.5
            if event.key == pygame.K_s:
                playerTwoVel += 3.5
            if event.key == pygame.K_w:
                playerTwoVel -= 3.5
            if event.key == pygame.K_TAB:
                secondPlayer = True
            if event.key == pygame.K_r:
                playerScore = 0
                oppponentScore = 0
                ballRestart()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerVel -= 3.5
            if event.key == pygame.K_UP:
                playerVel += 3.5
            if event.key == pygame.K_s:
                playerTwoVel -= 3.5
            if event.key == pygame.K_w:
                playerTwoVel += 3.5

    ballAnimation()
    playerAnimation()

    if secondPlayer == False:
        opponentAnimation()

    if secondPlayer == True:
        secondPlayerAnimation()
    
    # Visuals
    screen.fill((0, 0, 0))

    playerScoreLabel = mainFont.render(f"{playerScore}", 1, (255,255,255))
    opponentScoreLabel = mainFont.render(f"{opponentScore}", 1, (255,255,255))
    
    pygame.draw.rect(screen, white, player)
    pygame.draw.rect(screen, white, opponent)
    pygame.draw.rect(screen, white, ball)
    screen.blit(playerScoreLabel, (480, 20))
    screen.blit(opponentScoreLabel, (160, 20))
    
    # Display Handling
    pygame.display.update()
    clock.tick(60)

# If Main Loop Is Killed
pygame.quit()
