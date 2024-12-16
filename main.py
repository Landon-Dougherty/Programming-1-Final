import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 600

screen_res = (WIDTH, HEIGHT)
 
pygame.display.set_caption("Programming 1 Plinko")
screen = pygame.display.set_mode(screen_res)
 

RED = (255, 0, 0)
BLACK = (0, 0, 0)\

 

ball_obj = pygame.draw.circle(
    surface=screen, color=red, center=[100, 100], radius=40)

speed = [1, 1]
 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill(black)
    ball_obj = ball_obj.move(speed)

    if ball_obj.left <= 0 or ball_obj.right >= WIDTH:
        speed[0] = -speed[0]
    if ball_obj.top <= 0 or ball_obj.bottom >= HEIGHT:
        speed[1] = -speed[1]

    pygame.draw.circle(surface=screen, color=red, center=ball_obj.center, radius=5)

    pygame.display.flip()
