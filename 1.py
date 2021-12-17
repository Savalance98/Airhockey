import pygame

WIDTH, HEIGHT = 660, 883

fps = 60

paddle_w = 330
paddle_h = 35
paddle_speed = 15
paddle_radius = 40
paddle_speed = 15
paddle_rect = int(paddle_radius * 2 ** 0.5)
paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_rect, paddle_rect)

paddle2_radius = 40
paddle2_speed = 15
paddle2_rect = int(paddle2_radius * 2 ** 0.5)
paddle2 = pygame.Rect(330, 10, paddle2_rect, paddle2_rect)

ball_radius = 20
ball_speed = 2
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, ball_rect, ball_rect)
dx, dy = 1, - 1

def pole():
    pygame.draw.lines(sc, 'WHITE', True,
                      [[10, 10], [140, 70],
                       [280, 20]], 2)




pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

img = pygame.image.load('image_2021-12-17_17-50-53.png').convert()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # sc.blit(img, (0,0))
    sc.fill('black')
    pole()

    pygame.draw.circle(sc, pygame.Color('red'),  paddle.center, paddle_radius)
    pygame.draw.circle(sc, pygame.Color('white'), ball.center, ball_radius)
    pygame.draw.circle(sc, pygame.Color('blue'), paddle2.center,paddle2_radius)
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy
    pygame.display.flip()

    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        dx = -dx
    if ball.centery < ball_radius or ball.centery > HEIGHT - ball_radius:
        dy = -dy
    if ball.colliderect(paddle) and dy > 0:
        dy = -dy
        print(paddle.x, paddle.y,ball.x,ball.y)
    if ball.colliderect(paddle2) and dy < 0:
        dy = -dy



    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and paddle.y > 35:

        paddle.y -= paddle_speed
    if key[pygame.K_DOWN] and paddle.y < HEIGHT - paddle_h * 2:
        paddle.y += paddle_speed
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += paddle_speed

    if key[pygame.K_w] and paddle2.y > 35:
        paddle2.y -= paddle2_speed
    if key[pygame.K_s] and paddle2.y >= 0:
        paddle2.y += paddle2_speed
    if key[pygame.K_a] and paddle2.left > 0:
        paddle2.left -= paddle2_speed
    if key[pygame.K_d] and paddle2.right < WIDTH:
        paddle2.right += paddle2_speed

    pygame.display.flip()
    clock.tick(fps)
