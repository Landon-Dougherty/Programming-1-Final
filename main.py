import pygame
import turtle

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
CENTER = [WIDTH // 2, HEIGHT // 2]

#
scoremult = 0

# Gravity
gravity = -0.005
velocity = 0

# OTHER STUFF
gravity = 0.000985
velocity = int(1)
speed = [0,1]

y_offset = 0
# Ball That Drops

ball_obj = pygame.draw.circle(screen, RED, center=[WIDTH // 2, 100], radius=7.5)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill(BLACK)
    ball_obj = ball_obj.move(speed)

    if ball_obj.left <= 0 or ball_obj.right >= WIDTH:
        speed[0] = -speed[0]
    if ball_obj.top <= 0 or ball_obj.bottom >= HEIGHT:
        speed[1] = -speed[1]



    # DESIGN CODE BELOW
    # First "Layer"
    first = pygame.draw.circle(screen, WHITE, center=[500, 150], radius=15)
    # Second Layer
    second_1 = pygame.draw.circle(screen, WHITE, center=[550, 200], radius=15)
    second_2 =pygame.draw.circle(screen, WHITE, center=[450, 200], radius=15)
    # Third Layer
    third_1 = pygame.draw.circle(screen, WHITE, center=[600, 250], radius=15)
    third_2 = pygame.draw.circle(screen, WHITE, center=[500, 250], radius=15)
    third_3 = pygame.draw.circle(screen, WHITE, center=[400, 250], radius=15)
    # Fourth Layer
    fourth_1 = pygame.draw.circle(screen, WHITE, center=[350, 300], radius=15)
    fourth_2 = pygame.draw.circle(screen, WHITE, center=[450, 300], radius=15)
    fourth_3 = pygame.draw.circle(screen, WHITE, center=[550, 300], radius=15)
    fourth_4 =pygame.draw.circle(screen, WHITE, center=[650, 300], radius=15)
    # Fifth Layer
    fifth_1 = pygame.draw.circle(screen, WHITE, center=[300, 350], radius=15)
    fifth_2 = pygame.draw.circle(screen, WHITE, center=[400, 350], radius=15)
    fifth_3 = pygame.draw.circle(screen, WHITE, center=[500, 350], radius=15)
    fifth_4 = pygame.draw.circle(screen, WHITE, center=[600, 350], radius=15)
    fifth_5 =pygame.draw.circle(screen, WHITE, center=[700, 350], radius=15)
    # Sixth Layer
    sixth_1 = pygame.draw.circle(screen, WHITE, center=[250, 400], radius=15)
    sixth_2 = pygame.draw.circle(screen, WHITE, center=[350, 400], radius=15)
    sixth_3 = pygame.draw.circle(screen, WHITE, center=[450, 400], radius=15)
    sixth_4 = pygame.draw.circle(screen, WHITE, center=[550, 400], radius=15)
    sixth_5 = pygame.draw.circle(screen, WHITE, center=[650, 400], radius=15)
    sixth_6 = pygame.draw.circle(screen, WHITE, center=[750, 400], radius=15)
    # LAST LAYER!!!
    seventh_1 = pygame.draw.circle(screen, WHITE, center=[200, 450], radius=15)
    seventh_2 = pygame.draw.circle(screen, WHITE, center=[300, 450], radius=15)
    seventh_3 = pygame.draw.circle(screen, WHITE, center=[400, 450], radius=15)
    seventh_4 = pygame.draw.circle(screen, WHITE, center=[500, 450], radius=15)
    seventh_5 = pygame.draw.circle(screen, WHITE, center=[600, 450], radius=15)
    seventh_6 = pygame.draw.circle(screen, WHITE, center=[700, 450], radius=15)
    seventh_7 = pygame.draw.circle(screen, WHITE, center=[800, 450], radius=15)

    # Barrier Lines
    pygame.draw.aaline(screen, WHITE, start_pos=[100, 450], end_pos=[375, 175])
    pygame.draw.aaline(screen, WHITE, start_pos=[900, 450], end_pos=[625, 175])
    pygame.draw.aaline(screen, WHITE, start_pos=[375, 175], end_pos=[375, 50])
    pygame.draw.aaline(screen, WHITE, start_pos=[625, 175], end_pos=[625, 50])
    # Boxes To Catch Things
    # (X,Y,WIDTH,HEIGHT)
    # Outer 2 ENDS
    pygame.draw.rect(screen, RED, [100, 450, 100, 17.5])
    pygame.draw.rect(screen, RED, [800, 450, 100, 17.5])
    pygame.draw.rect(screen, ORANGE, [200, 450, 100, 17.5])
    pygame.draw.rect(screen, ORANGE, [700, 450, 100, 17.5])
    pygame.draw.rect(screen, YELLOW, [300, 450, 100, 17.5])
    pygame.draw.rect(screen, YELLOW, [600, 450, 100, 17.5])
    # MIDDLE WHITE ONE BELOW
    pygame.draw.rect(screen, WHITE, [400, 450, 200, 17.5])

    pygame.draw.circle(surface=screen, color=RED, center=ball_obj.center, radius=7.5)

    # SCORE SYSTEM
    if ball_obj.bottom >= 100 and ball_obj.right <= 800 and ball_obj.left >= 100:
        if ball_obj.left >= 100 and ball_obj.right <= 200 and ball_obj.left >= 800 and ball_obj.right <= 900 and ball_obj.bottom <= 450:
            scoremult = 5
        elif ball_obj.left >= 200 and ball_obj.right <= 300 and ball_obj.left >= 700 and ball_obj.right <= 800 and ball_obj.bottom <= 450:
            scoremult = 3
        elif ball_obj.left >= 300 and ball_obj.right <= 400 and ball_obj.left >= 600 and ball_obj.right <= 700 and ball_obj.bottom <= 450:
            scoremult = 2
        elif ball_obj.left >= 400 and ball_obj.right <= 600 and ball_obj.bottom <= 450:
            scoremult = 0.5

        #Attempt at Velocity



    pygame.display.flip()

    '''import turtle

test = turtle.Screen()
test.bgcolor("black")
test.title("Plinko Tester")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("Green")
ball.speed(0)
ball.goto(0, 200)
ball.dy = -2

gravity = 0.2

while True:
    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() < -300:
        ball.dy *= -1'''
