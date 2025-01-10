import time

import pygame
import keyboard
import random



'''REFERERNCES
    https://www.geeksforgeeks.org/stimulate-bouncing-game-using-pygame/  USED TO MAKE BALL MOVE
    https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame USED AT SOME POINT BUT NEVER GOT WORKING YET
    https://www.makeuseof.com/pygame-game-scores-displaying-updating/ USED TO DISPLAY MONEY, BUT SCOREBOARD IS MADE BY YOURS TRULY. 
    '''

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
BUTTON_DARK = (1, 50, 32)
BUTTON_LIGHT = (0, 128, 0)
CENTER = [WIDTH // 2, HEIGHT // 2]

font = pygame.font.SysFont("Arial", 36)
Money = 0

#
ScoreMulti = 0
Money = 10

# Gravity
gravity = -0.005
velocity = 0

# OTHER STUFF
gravity = 0.000985
velocity = 1
speed = [0, 1]
smallfont = pygame.font.SysFont('Corbel',36)
text = smallfont.render("test", True, WHITE)

Running = False

y_offset = 0
# Ball That Drops

ball_obj = pygame.draw.circle(screen, RED, center=[WIDTH//2, 100], radius=7.5)
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 825 <= mouse[0] <= 965 and 200 <= mouse[1] <= 240:
                ClickMoney = random.randint(1,10)
                Money = Money + ClickMoney



    mouse = pygame.mouse.get_pos()
    screen.fill(BLACK)
    MoneyText = font.render(f"Money :  {Money}", 1, (0, 255, 0))
    screen.blit(MoneyText, ((WIDTH//2)-75, 480))

    Percent10 = font.render("10% Bet", 1, (255, 255,255))
    Percent25 = font.render("25% Bet", 1, (255, 255, 255))
    Percent50 = font.render("50% Bet",1, (255, 255, 255))
    Percent75 = font.render("75% Bet", 1,(255, 255,255))
    screen.blit(Percent10, (100, 500))
    screen.blit(Percent25, (250,500))
    screen.blit(Percent50, (650,500))
    screen.blit(Percent75, (800,500))


    if 825 <= mouse[0] <= 965 and 200 <= mouse[1] <= 240:
        pygame.draw.rect(screen,BUTTON_LIGHT,[825,200,140,40])

    else:
        pygame.draw.rect(screen,BUTTON_DARK,[825,200,140,40])



    # DESIGN CODE

    first = pygame.draw.circle(screen, WHITE, center=[500, 150], radius=15)

    second_1 = pygame.draw.circle(screen, WHITE, center=[550, 200], radius=15)
    second_2 = pygame.draw.circle(screen, WHITE, center=[450, 200], radius=15)

    third_1 = pygame.draw.circle(screen, WHITE, center=[600, 250], radius=15)
    third_2 = pygame.draw.circle(screen, WHITE, center=[500, 250], radius=15)
    third_3 = pygame.draw.circle(screen, WHITE, center=[400, 250], radius=15)

    fourth_1 = pygame.draw.circle(screen, WHITE, center=[350, 300], radius=15)
    fourth_2 = pygame.draw.circle(screen, WHITE, center=[450, 300], radius=15)
    fourth_3 = pygame.draw.circle(screen, WHITE, center=[550, 300], radius=15)
    fourth_4 = pygame.draw.circle(screen, WHITE, center=[650, 300], radius=15)

    fifth_1 = pygame.draw.circle(screen, WHITE, center=[300, 350], radius=15)
    fifth_2 = pygame.draw.circle(screen, WHITE, center=[400, 350], radius=15)
    fifth_3 = pygame.draw.circle(screen, WHITE, center=[500, 350], radius=15)
    fifth_4 = pygame.draw.circle(screen, WHITE, center=[600, 350], radius=15)
    fifth_5 = pygame.draw.circle(screen, WHITE, center=[700, 350], radius=15)

    sixth_1 = pygame.draw.circle(screen, WHITE, center=[250, 400], radius=15)
    sixth_2 = pygame.draw.circle(screen, WHITE, center=[350, 400], radius=15)
    sixth_3 = pygame.draw.circle(screen, WHITE, center=[450, 400], radius=15)
    sixth_4 = pygame.draw.circle(screen, WHITE, center=[550, 400], radius=15)
    sixth_5 = pygame.draw.circle(screen, WHITE, center=[650, 400], radius=15)
    sixth_6 = pygame.draw.circle(screen, WHITE, center=[750, 400], radius=15)

    seventh_1 = pygame.draw.circle(screen, WHITE, center=[200, 450], radius=15)
    seventh_2 = pygame.draw.circle(screen, WHITE, center=[300, 450], radius=15)
    seventh_3 = pygame.draw.circle(screen, WHITE, center=[400, 450], radius=15)
    seventh_4 = pygame.draw.circle(screen, WHITE, center=[500, 450], radius=15)
    seventh_5 = pygame.draw.circle(screen, WHITE, center=[600, 450], radius=15)
    seventh_6 = pygame.draw.circle(screen, WHITE, center=[700, 450], radius=15)
    seventh_7 = pygame.draw.circle(screen, WHITE, center=[800, 450], radius=15)


    pygame.draw.aaline(screen, WHITE, start_pos=[100, 450], end_pos=[375, 175])
    pygame.draw.aaline(screen, WHITE, start_pos=[900, 450], end_pos=[625, 175])
    pygame.draw.aaline(screen, WHITE, start_pos=[375, 175], end_pos=[375, 50])
    pygame.draw.aaline(screen, WHITE, start_pos=[625, 175], end_pos=[625, 50])

    pygame.draw.rect(screen, RED, [100, 450, 100, 17.5])
    pygame.draw.rect(screen, RED, [800, 450, 100, 17.5])
    pygame.draw.rect(screen, ORANGE, [200, 450, 100, 17.5])
    pygame.draw.rect(screen, ORANGE, [700, 450, 100, 17.5])
    pygame.draw.rect(screen, YELLOW, [300, 450, 100, 17.5])
    pygame.draw.rect(screen, YELLOW, [600, 450, 100, 17.5])

    pygame.draw.rect(screen, WHITE, [400, 450, 200, 17.5])
    # END OF DESIGN CODE

    #USE THE BALL



    Tops = [first.top, second_1.top, second_2.top, third_1.top, third_2.top, third_3.top, fourth_1.top, fourth_2.top, fourth_3.top,
            fourth_4.top, fifth_1.top, fifth_2.top, fifth_3.top, fifth_4.top, fifth_5.top, sixth_1.top, sixth_2.top, sixth_3.top ,
           sixth_4.top, sixth_5.top, sixth_6.top, seventh_1.top, seventh_2.top, seventh_3.top, seventh_4.top, seventh_5.top, seventh_6.top ,
           seventh_7.top]



    # ball_obj = ball_obj.move(speed)
    ball_obj.y = ball_obj.y + float(0.5)
    pygame.draw.circle(surface=screen, color=RED, center=ball_obj.center, radius=7.5)
    # FIRST LAYER
    if ball_obj.bottom == Tops[0]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    # SECOND LAYER
    elif ball_obj.bottom == Tops[1]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[2]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    # THIRD LAYER
    elif ball_obj.bottom == Tops[3]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[4]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[5]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    # FOURTH LAYEr
    elif ball_obj.bottom == Tops[6]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[7]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[8]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[9]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    # FIFTH LAYER
    elif ball_obj.bottom == Tops[10]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[11]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[12]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[13]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[14]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    # SIXTH LAYER
    elif ball_obj.bottom == Tops[15]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[16]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[17]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[18]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[19]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[20]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    # SEVENTH LAYER
    elif ball_obj.bottom == Tops[21]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[22]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[23]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[24]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[25]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[26]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    elif ball_obj.bottom == Tops[27]:
        dct = random.randint(1,2)
        if dct == 1:
            ball_obj.x = ball_obj.x -50
            time.sleep(1)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)










    if ball_obj.y >= 460:
        ball_obj.center = (WIDTH//2, 100)
    # SCORE SYSTEM COMPLETELY  MADE BY ME
    if ball_obj.bottom >= 100 and ball_obj.right <= 900 and ball_obj.left >= 100:
        if (ball_obj.left >= 100 and ball_obj.right <= 200 and ball_obj.bottom >= 450) \
                or (ball_obj.left >= 800 and ball_obj.right <= 900 and ball_obj.bottom >= 450):
            ScoreMulti = 5
            Money = float(round(Money * ScoreMulti,2))
            ball_obj.center = (WIDTH//2, 100)
        elif (ball_obj.left >= 200 and ball_obj.right <= 300 and ball_obj.bottom >= 450) \
                or (ball_obj.left >= 700 and ball_obj.right <= 800 and ball_obj.bottom >= 450):
            ScoreMulti = 3
            Money = float(round(Money * ScoreMulti,2))
            ball_obj.center = (WIDTH//2, 100)
        elif (ball_obj.left >= 300 and ball_obj.right<= 400 and ball_obj.bottom >= 450) \
                or (ball_obj.left >= 600 and ball_obj.right<= 700 and ball_obj.bottom >450):
            ScoreMulti = 2
            Money = float(round(Money * ScoreMulti,2))
            ball_obj.center = (WIDTH//2, 100)
        elif ball_obj.left >= 400 and ball_obj.right <= 600 and ball_obj.bottom >= 450:
            ScoreMulti = 0.5
            Money = float(round(Money * ScoreMulti,2))
            ball_obj.center = (WIDTH//2, 100)
    else:
        pass













    # if ball_obj.left <= 0 or ball_obj.right >= WIDTH:
    #     speed[0] = -speed[0]
    # if ball_obj.top <= 0 or ball_obj.bottom >= HEIGHT:
    #     speed[velocity] = -speed[velocity]
    #

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


