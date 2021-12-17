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
class Ball:
    def __init__(self):
        self.ball_radius = 20
        self.ball_speed = 2
        self.ball_rect = int(self.ball_radius * 2 ** 0.5)
        self.ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, self.ball_rect, self.ball_rect)
dx, dy = 1, - 1
def draw_f():
    pygame.draw.circle(sc, pygame.Color('red'), paddle.center, paddle_radius)
    pygame.draw.circle(sc, pygame.Color('white'), ball.center, ball_radius)
    pygame.draw.circle(sc, pygame.Color('blue'), paddle2.center, paddle2_radius)


def pole():
    colour = "WHITE"
    pygame.draw.lines(sc, colour, True,
                      [[0, 0],
                       [0, 883]], 5)
    pygame.draw.lines(sc, colour, True,
                      [[660, 0],
                       [660, 883]], 5)
    pygame.draw.lines(sc, colour, True,
                      [[0, 0],
                       [230, 0]], 5)
    pygame.draw.lines(sc, colour, True,
                      [[430, 0],
                       [660, 0]], 5)
    pygame.draw.lines(sc, colour, True,
                      [[0, 883],
                       [230, 883]], 5)
    pygame.draw.lines(sc, colour, True,
                      [[430, 883],
                       [660, 883]], 5)
    pygame.draw.lines(sc, colour, True,
                      [[0, 442],
                       [660, 442]], 5)
    pygame.draw.circle(sc, colour, [330, 442], 50, 5)

def position(dx, dy,ball,rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top
    if abs(delta_x - delta_y) < 10:
        dx,dy = -dx,-dy
    elif delta_x>delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx,dy

ball_radius = 20
ball_speed = 2
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, ball_rect, ball_rect)
def over():
    ball_speed = 0
    while True:
        render_end = f.render('GAME OVER', 1, pygame.Color('red'))
        sc.blit(render_end, (100, 100))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            else:
                key = pygame.key.get_pressed()
                if key[pygame.K_e]:
                    return 1


def ball_koord(dx,dy):
    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        dx = -dx
    if ball.centery < ball_radius or ball.centery > HEIGHT - ball_radius:
        if ball.centerx > 230 and ball.centerx < 430:
            return over()
        else:
            dy = -dy
    if ball.colliderect(paddle):
        dx, dy = position(dx, dy, ball, paddle)
    if ball.colliderect(paddle2):
        dx, dy = position(dx, dy, ball, paddle2)
    return dx,dy

def b_s(ball_speed):
    import time
    timing = time.time()
    while True:
        if time.time() - timing > 10.0:
            timing = time.time()
            ball_speed *= 1.1
        else:
            ball_speed /= 1.1
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
f = pygame.font.SysFont('Arial', 26)


class Button:
    def __init__(self,w,h):
        self.w = w
        self.h = h
        self.ina = (23,204,58)
        self.ac = (13, 162, 58)
    def draw(self,x,y,mess,action = None, font_size = 30):
        mo = pygame.mouse.get_pos()
        cl = pygame.mouse.get_pressed()
        if x < mo[0] < x + self.w and y < mo[1] < y + self.h:
            pygame.draw.rect(display,(23,204,58), (x,y,self.w,self.h))
            if cl [0] == 1:
                clock.tick(60)
                start_g(1)
        else:
            pygame.draw.rect(display, (13, 162, 58), (x, y, self.w, self.h))
        print_text(mess,x + 10, y + 10, font_size=font_size)


def print_text(mess,x,y,font_c=(0,0,0), font_type='PingPong.ttf', font_size = 30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(mess, True,font_c)
    display.blit(text, (x,y))

def show_menu():
    menu_b = pygame.image.load('depositphotos_151759188-stock-illustration-north-american-ice-hockey-rink.jpg')
    show = True
    start_b = Button(300, 70)
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            display.blit(menu_b, (0,0))
            start_b.draw(300,200,'Start')
            pygame.display.update()
            clock.tick(60)
def start_g(t):
    global dx,dy,ball
    while t:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        sc.fill('black')
        pole()
        draw_f()
        ball.x += ball_speed * dx
        ball.y += ball_speed * dy
        pygame.display.flip()
        x = ball_koord(dx, dy)
        if x != 1:
            dx = x[0]
            dy = x[1]
        else:
            dx, dy = 1, - 1
            ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, ball_rect, ball_rect)
            start_g(1)
        pygame.display.flip()
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and paddle.y > 35 and paddle.y + paddle_radius // 2 > HEIGHT // 2:
            paddle.y -= paddle_speed
        if key[pygame.K_DOWN] and paddle.y < HEIGHT - paddle_h * 2:
            paddle.y += paddle_speed
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddle_speed
        if key[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.right += paddle_speed

        if key[pygame.K_w] and paddle2.y > 35:
            paddle2.y -= paddle2_speed
        if key[pygame.K_s] and paddle2.y >= 0 and paddle2.centery < HEIGHT // 2:
            paddle2.y += paddle2_speed
        if key[pygame.K_a] and paddle2.left > 0:
            paddle2.left -= paddle2_speed
        if key[pygame.K_d] and paddle2.right < WIDTH:
            paddle2.right += paddle2_speed

        pygame.display.flip()
        clock.tick(fps)

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
f = pygame.font.SysFont('Arial', 26)
score_1 = 0
score_2 = 0
show_menu()


