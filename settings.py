import pygame

WHITE = (255, 255, 255)
BLACK = (0,0,0)

WIDTH = 1000
HEIGHT = 800
screen_res = (WIDTH, HEIGHT)

pygame.display.set_caption("Programming 1 Plinko")
screen = pygame.display.set_mode(screen_res)

fps = 60
timer = pygame.time.Clock()
# OTHER STUFF
gravity = 0.000985
velocity = 1
speed = [0, 1]
def DrawGame():
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

def Ball(x_pos, y_pos)
    ball_obj = pygame.draw.circle(screen, WHITE, center = [WIDTH//2, 100], radius = 15)
    for x in range(1, WIDTH+1):
        if x >= ball_obj.x:

run = True
while run:
    timer.tick(fps)
    screen.fill(BLACK)
    game = DrawGame()


    pygame.display.flip()
    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False

