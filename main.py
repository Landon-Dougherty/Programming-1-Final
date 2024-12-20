import turtle

test = turtle.Screen()
test.bgcolor("black")
test.title("Plinko Tester")

ball = turtle.Turtle()





'''import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 600

screen_res = (WIDTH, HEIGHT)
 
pygame.display.set_caption("Programming 1 Plinko")
screen = pygame.display.set_mode(screen_res)
 
# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
CENTER = [WIDTH//2, HEIGHT//2]

 
#Make A Circle
test = pygame.draw.circle(screen, WHITE, radius = 15, center = [0,0])

plinko_1 = pygame.draw.circle(screen, WHITE, center = [500, 100], radius = 100)


speed = [1, 1]
 
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill(BLACK)

    #Ball That Drops
    pygame.draw.circle(screen, RED, center=[WIDTH//2, 100], radius=7.5)
    # First "Layer"
    pygame.draw.circle(screen, WHITE, center=[500,150],radius = 15)
    #Second Layer
    pygame.draw.circle(screen, WHITE, center=[550,200],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[450,200],radius = 15)
    #Third Layer
    pygame.draw.circle(screen, WHITE, center=[600,250],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[500,250],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[400,250],radius = 15)
    # Fourth Layer
    pygame.draw.circle(screen, WHITE, center=[350,300],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[450,300],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[550,300],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[650,300],radius = 15)
    # Fifth Layer
    pygame.draw.circle(screen, WHITE, center=[300,350],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[400,350],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[500,350],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[600,350],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[700,350],radius = 15)
    # Sixth Layer
    pygame.draw.circle(screen, WHITE, center=[250,400],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[350,400],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[450,400],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[550,400],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[650,400],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[750,400],radius = 15)
    # LAST LAYER!!!
    pygame.draw.circle(screen, WHITE, center=[200,450],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[300,450],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[400,450],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[500,450],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[600,450],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[700,450],radius = 15)
    pygame.draw.circle(screen, WHITE, center=[800,450],radius = 15)
    # Barrier Lines
    pygame.draw.aaline( screen,  WHITE, start_pos = [100,450] , end_pos = [375,175])
    pygame.draw.aaline(screen,  WHITE, start_pos=[900,450], end_pos=[625, 175])
    pygame.draw.aaline(screen, WHITE, start_pos=[375,175], end_pos=[375,50])
    pygame.draw.aaline(screen, WHITE, start_pos=[625,175], end_pos=[625,50])
    # Boxes To Catch Things
    #(X,Y,WIDTH,HEIGHT)
    #Outer 2 ENDS
    pygame.draw.rect(screen, RED, [100, 450, 100, 17.5])
    pygame.draw.rect(screen, RED, [800, 450, 100, 17.5])
    pygame.draw.rect(screen, ORANGE, [200,450,100, 17.5])
    pygame.draw.rect(screen, ORANGE, [700,450,100, 17.5])
    pygame.draw.rect(screen, YELLOW, [300, 450, 100, 17.5])
    pygame.draw.rect(screen, YELLOW, [600, 450, 100, 17.5])
    # MIDDLE WHITE ONE BELOW
    pygame.draw.rect(screen, WHITE, [400, 450, 200, 17.5])

    pygame.display.flip()'''


