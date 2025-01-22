import time
import pygame
import keyboard
import random

'''REFERERNCES
    https://www.geeksforgeeks.org/how-to-set-up-the-game-loop-in-pyggame/ FOR PYGAME GAME LOOP 
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

# region Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BETBACK = (1, 50, 32)
BETHOVER = (1, 80, 32)
ORANGE = (255, 165, 0)
BUTTON_DARK = (1, 50, 32)
BUTTON_LIGHT = (0, 128, 0)
CENTER = [WIDTH // 2, HEIGHT // 2]
# endregion

font = pygame.font.SysFont("Arial", 36)
Money = 0

#
ScoreMulti = 0
Money = 10
Bet = 10
LastWin = 0






# OTHER STUFF
gravity = 0.000985
velocity = 1
speed = [0, 1]
smallfont = pygame.font.SysFont('Corbel', 36)
text = smallfont.render("test", True, WHITE)

Running = False

y_offset = 0
# Ball That Drops

ball_obj = pygame.draw.circle(screen, RED, center=[WIDTH // 2, 100], radius=7.5)
# Game loop


while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEWHEEL:
            Money = Money + 12500
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # region Button Clicks
            if 380 <= mouse[0] <= 630 and 50 <= mouse[1] <= 110:
                ClickMoney = random.randint(1, 5)
                Money = Money + ClickMoney
            if 100 < mouse[0] < 215 and 500 < mouse[1] < 540: # 10% BET BUTTON
                Bet = Money / 10.0
            elif 250 < mouse[0] < 365 and 500 <= mouse[1] <= 540: # 25% BET BUTTON
                Bet = Money / 4.0
            elif 650 < mouse[0] < 765 and 500 <= mouse[1] <= 540: # 50% BET BUTTON
                Bet = Money / 2.0
            elif 800 < mouse[0] < 915 and 500 <= mouse[1] <= 540:
                Bet = Money - (Money // 4)
            # endregion

    mouse = pygame.mouse.get_pos()
    screen.fill(BLACK)
    # region Rectangles For Things
    pygame.draw.rect(screen, BETBACK, [WIDTH // 2 - 185, 10, 380, 40])
    pygame.draw.rect(screen, BETBACK, [WIDTH // 2 - 100, 480, 230, 40])
    pygame.draw.rect(screen, BETBACK, [WIDTH // 2 - 100, 520, 230, 40])
    pygame.draw.rect(screen, BETBACK, [WIDTH // 2 - 123, 50, 250, 60])
    # endregion
    # region Variables For Things
    RecentWin = font.render(f"Your Most Recent Win: {LastWin:.2f}", 1, (0, 255, 0))
    ClickCash = font.render("Click 4 Cash", 1 , (0, 255, 0))
    MoneyText = font.render(f"Money :  {Money:.2f}", 1, (0, 255, 0))
    BetText = font.render(f"Bet : {Bet:.2f}", 1, (0, 255, 0))
    # endregion
    # region Place Variables Into Text
    screen.blit(RecentWin, (WIDTH//2 - 185, 10))
    screen.blit(MoneyText, (WIDTH//2 - 100, 480))
    screen.blit(BetText, (WIDTH//2 - 100, 520))
    screen.blit(ClickCash, (WIDTH//2 - 80, 60))
    # endregion


    # region 10% Bet Button
    Percent10 = font.render("10% Bet", 1, (255, 255, 255))
    pygame.draw.rect(screen, BETBACK, [100, 500, 115, 40])
    if 100 < mouse[0] < 215 and 500 < mouse[1] < 540:
        pygame.draw.rect(screen, BETHOVER, [100, 500, 115, 40])
    # endregion 10% Bet Button
    # region 25% Bet Button
    Percent25 = font.render("25% Bet", 1, (255, 255, 255))
    pygame.draw.rect(screen, BETBACK, [250, 500, 115, 40])
    if 250 < mouse[0] < 365 and 500 <= mouse[1] <= 540:
        pygame.draw.rect(screen, BETHOVER, [250, 500, 115, 40])
    # endregion 25% Bet Button
    # region 50% Bet Button
    Percent50 = font.render("50% Bet", 1, (255, 255, 255))
    pygame.draw.rect(screen, BETBACK, [650, 500, 115, 40])
    if 650 < mouse[0] < 765 and 500 <= mouse[1] <= 540:
        pygame.draw.rect(screen, BETHOVER, [650, 500, 115, 40])
    # endregion 50% Bet Button
    # region 75% Bet Button
    Percent75 = font.render("75% Bet", 1, (255, 255, 255))
    pygame.draw.rect(screen, BETBACK, [800, 500, 115, 40])
    if 800 < mouse[0] < 915 and 500 <= mouse[1] <= 540:
        pygame.draw.rect(screen, BETHOVER, [800, 500, 115, 40])
    # endregion 75% Bet Button
    # region Bet Button Labels
    screen.blit(Percent10, (100, 500))
    screen.blit(Percent25, (250, 500))
    screen.blit(Percent50, (650, 500))
    screen.blit(Percent75, (800, 500))
    # endregion Bet Button Labels



    # region DESIGN CODE
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
    # endregion TEST



    # region Unnecessary Variable Called Tops To Make Code Moderately More Readable
    Tops = [first.top, second_1.top, second_2.top, third_1.top, third_2.top, third_3.top, fourth_1.top, fourth_2.top,
            fourth_3.top,
            fourth_4.top, fifth_1.top, fifth_2.top, fifth_3.top, fifth_4.top, fifth_5.top, sixth_1.top, sixth_2.top,
            sixth_3.top,
            sixth_4.top, sixth_5.top, sixth_6.top, seventh_1.top, seventh_2.top, seventh_3.top, seventh_4.top,
            seventh_5.top, seventh_6.top,
            seventh_7.top]
    # endregion
    # region Make Ball Move With Bet
    BadBet = False
    if Money >= Bet:
        ball_obj.y = ball_obj.y + 1
        pygame.draw.circle(surface=screen, color=RED, center=ball_obj.center, radius=7.5)
        pygame.draw.circle(surface=screen, color=RED, center=ball_obj.center, radius=7.5)
        RecentWin = font.render(f"Your Most Recent Win: {LastWin:.2f}", 1, (0, 255, 0))
    else:
        BadBet = True
    while BadBet:
        ball_obj = pygame.draw.circle(screen, RED, center=[WIDTH // 2, 100], radius=7.5)
        pygame.draw.rect(screen, BETBACK, [WIDTH//2 - 250, 150, 500, 50])
        test = font.render("BET MUST BE IN YOUR BUDGET", 1, (0, 255, 0))
        screen.blit(test, (WIDTH//2 - 225, 150))

        break
    # endregion Make Ball Move With Bet


    # region Ball "Randomizer"
    if ball_obj.bottom == Tops[0]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    # SECOND LAYER
    elif ball_obj.bottom == Tops[1]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[2]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    # THIRD LAYER
    elif ball_obj.bottom == Tops[3]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[4]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[5]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    # FOURTH LAYEr
    elif ball_obj.bottom == Tops[6]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[7]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[8]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[9]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    # FIFTH LAYER
    elif ball_obj.bottom == Tops[10]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[11]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[12]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[13]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[14]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    # SIXTH LAYER
    elif ball_obj.bottom == Tops[15]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[16]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[17]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[18]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[19]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[20]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    # SEVENTH LAYER
    elif ball_obj.bottom == Tops[21]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[22]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[23]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[24]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[25]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[26]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(0.5)
    elif ball_obj.bottom == Tops[27]:
        dct = random.randint(1, 2)
        if dct == 1:
            ball_obj.x = ball_obj.x - 50
            time.sleep(0.5)
        else:
            ball_obj.x = ball_obj.x + 50
            time.sleep(1)
    # endregion Ball "Randomizer"

    # region Scoreboard
    if ball_obj.y >= 460:
        ball_obj.center = (WIDTH // 2, 100)
    # SCORE SYSTEM COMPLETELY  MADE BY ME
    if ball_obj.bottom >= 100 and ball_obj.right <= 900 and ball_obj.left >= 100:
        if (ball_obj.left >= 100 and ball_obj.right <= 200 and ball_obj.bottom >= 450) \
                or (ball_obj.left >= 800 and ball_obj.right <= 900 and ball_obj.bottom >= 450):
            ScoreMulti = 5
            Money = float(round(Bet * ScoreMulti, 2)) + Money
            LastWin = float(round(Bet * ScoreMulti, 2))
            ball_obj.center = (WIDTH // 2, 100)
        elif (ball_obj.left >= 200 and ball_obj.right <= 300 and ball_obj.bottom >= 450) \
                or (ball_obj.left >= 700 and ball_obj.right <= 800 and ball_obj.bottom >= 450):
            ScoreMulti = 3
            Money = float(round(Bet * ScoreMulti, 2)) + Money
            LastWin = float(round(Bet * ScoreMulti, 2))
            ball_obj.center = (WIDTH // 2, 100)
        elif (ball_obj.left >= 300 and ball_obj.right <= 400 and ball_obj.bottom >= 450) \
                or (ball_obj.left >= 600 and ball_obj.right <= 700 and ball_obj.bottom > 450):
            ScoreMulti = 2
            Money = float(round(Bet * ScoreMulti, 2)) + Money
            LastWin = float(round(Bet * ScoreMulti, 2))
            ball_obj.center = (WIDTH // 2, 100)
        elif ball_obj.left >= 400 and ball_obj.right <= 600 and ball_obj.bottom >= 450:
            ScoreMulti = 0.5
            Money = Money - float(round(Bet * ScoreMulti, 2))
            LastWin = float(round(Bet * ScoreMulti, 2))
            ball_obj.center = (WIDTH // 2, 100)
    else:
        pass
    if Money >= 99999:
        RecentWin = font.render(f"YOU WIN! RESTART IF YOU WANT TO PLAY AGAIN", 1, (0, 255, 0))
        screen.blit(RecentWin, (WIDTH//2 - 100, 100))
    # endregion Scoreboard



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
