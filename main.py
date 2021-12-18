import pygame
import random

'''
Проект выполнили Даниил Савин БИБ211 и Гусев Максим БИБ211
'''

def draw_f():
    '''
    отрисовывает 2-х игроков и шайбу
    '''
    pygame.draw.circle(sc, pygame.Color('red'), player.center, player_radius)
    pygame.draw.circle(sc, pygame.Color('white'), ball.center, ball_radius)
    pygame.draw.circle(sc, pygame.Color('blue'), player2.center, player2_radius)
def pole(colour):
    '''
    рисует линии полей на поле
    :param colour: цвет
    '''
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
def position(dx, dy,b_r,b_l,r_r,r_l,b_t,b_b,r_b,r_t):

    '''
    коэффиценты dx,dy после ударения с объектом
    :param dx: коэффицент x
    :param dy: коэффицент y
    :param b_r: координата правой стороны шайбы
    :param b_l: координата левой стороны шайбы
    :param r_r: координата правой стороны объекта
    :param r_l: координата левой стороны объекта
    :param b_t: координата верхней стороны шайбы
    :param b_b: координата нижней стороны шайбы
    :param r_b: координата нижней стороны объекта
    :param r_t: координата верхней стороны объекта
    :return: коэффицент x, коэффицент y
    '''
    if dx > 0:
        delta_x = b_r - r_l
    else:
        delta_x = r_r - b_l
    if dy > 0:
        delta_y = b_b - r_t
    else:
        delta_y = r_b - b_t
    if abs(delta_x - delta_y) < 10:
        dx = -dx
        dy = -dy
    elif delta_x>delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx

    return dx,dy

def over(k):
    '''
    если счёт одного игрока больше 6, то программа закрывается, иначе, начинается новая игра с поменявшимся счётом
    :param k: координаты шайбы
    '''
    global score_1, score_2
    while True:
        if score_2 > 6 or score_1 > 6:
            render_end = f.render('GAME OVER', 1, pygame.Color('red'))
            sc.blit(render_end, (100, 100))
            pygame.display.flip()
            exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        else:
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                if k < 100:
                    score_1 += 1
                else:
                    score_2 += 1
                return 1
def ball_koord(dx,dy):
    '''
    считает коэффиценты dX,dY после прикосновения с стенами
    :param dx: коэффицент x
    :param dy: коэффицент y
    :return: коэффиценты X,Y после прикосновения с стенами
    '''
    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        dx = -dx
    if ball.centery < ball_radius or ball.centery > HEIGHT - ball_radius:
        if ball.centerx > 230 and ball.centerx < 430:
            return over(ball.centery)
        else:
            dy = -dy
    if ball.colliderect(player):
        dx, dy = position(dx, dy, ball.right,ball.left, player.right, player.left,ball.top,ball.bottom,player.bottom,player.top)
    if ball.colliderect(player2):
        dx, dy = position(dx, dy, ball.right,ball.left, player2.right, player2.left,ball.top,ball.bottom,player2.bottom,player2.top)
    return dx,dy

class Button:
    def __init__(self,w,h):
        self.w = w
        self.h = h
        self.ina = (23,204,58)
        self.ac = (13, 162, 58)
    def draw(self,x,y,mess,display, font_size = 30):
        '''
        делает нарисованную кнопку с распознаванием нажатия на неё, и дальнейшей программой
        :param x: длина
        :param y: высота
        :param mess: Сообщение на кнопке
        :param action: функция
        :param font_size: шрифт
        :param display: дисплей
        '''
        mo = pygame.mouse.get_pos()
        cl = pygame.mouse.get_pressed()
        if x < mo[0] < x + self.w and y < mo[1] < y + self.h:
            pygame.draw.rect(display,(23,204,58), (x,y,self.w,self.h))
            if cl[0] == 1 and mess != 'Quit':
                clock.tick(60)
                start_g(1)
            elif cl[0] == 1:
                exit()
        else:
            pygame.draw.rect(display, (13, 162, 58), (x, y, self.w, self.h))
        print_text(mess,x + 10, y + 10, font_size=font_size,display=display)
def print_text(mess,x,y,font_c=(0,0,0), font_type='PingPong.ttf', font_size = 30,display=None):
    '''
    делает нарисованный текст на кнопке
    :param mess: Сообщение на кнопке
    :param x: координата
    :param y: координата
    :param font_c: цвет
    :param font_type: шрифт
    :param font_size: размер
    :param display: дисплей
    '''
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(mess, True,font_c)
    display.blit(text, (x,y))
def show_menu(display):
    '''
    при включении программы появляется окно меню, в котором можно начать игру или выйти
    '''
    menu_b = pygame.image.load('image123.png')
    show = True
    start_b = Button(100, 70)
    plae = Button(100,70)
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            display.blit(menu_b, (0,0))
            start_b.draw(WIDTH // 2,HEIGHT // 2 - 100,'Start',display)
            plae.draw(WIDTH // 2,HEIGHT // 2 + 100,'Quit',display)
            pygame.display.update()
            clock.tick(60)
def start_g(t):
    '''
    основной цикл игры
    :param t: параметр для действия игры
    '''
    global dx,dy,ball,score_1,score_2,player2,player
    colour = random.choice(['RED', 'BLUE', 'WHITE', 'YELLOW',(255,70,9)])
    while t:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        sc.fill('black')
        pole(colour)
        draw_f()
        render_s = f.render(f'SCORE{score_1}:{score_2}', 1, pygame.Color('orange'))
        sc.blit(render_s, (5, 5))
        ball.x += ball_speed * dx
        ball.y += ball_speed * dy
        pygame.display.flip()
        x = ball_koord(dx, dy)
        if x != 1:
            dx = x[0]
            dy = x[1]
        else:
            if score_2 < score_1:
                dx, dy = 1, - 1
            else:
                dx, dy = -1, 1
            ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, ball_rect, ball_rect)
            score_1, score_2 = score_1,score_2
            player2 = pygame.Rect(330, 10, player2_rect, player2_rect)
            player = pygame.Rect(330, 813, player_rect, player_rect)
            start_g(1)
        pygame.display.flip()
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and player.y > 35 and player.y + player_radius // 2 > HEIGHT // 2:
            player.y -= player_speed
        if key[pygame.K_DOWN] and player.y < HEIGHT - player_h * 2 - 10:
            player.y += player_speed
        if key[pygame.K_LEFT] and player.left > 0:
            player.left -= player_speed
        if key[pygame.K_RIGHT] and player.right < WIDTH:
            player.right += player_speed
        if key[pygame.K_w] and player2.y > 30:
            player2.y -= player2_speed
        if key[pygame.K_s] and player2.y >= 0 and player2.centery < HEIGHT // 2:
            player2.y += player2_speed
        if key[pygame.K_a] and player2.left > 0:
            player2.left -= player2_speed
        if key[pygame.K_d] and player2.right < WIDTH:
            player2.right += player2_speed
        pygame.display.flip()
        clock.tick(fps)

def main1():
    '''
    запускает функцию с кодом жизни
    '''
    f = pygame.font.SysFont('Arial', 26)
    show_menu(display)

if __name__ == '__main__':
    pygame.init()
    WIDTH, HEIGHT = 660, 883
    fps = 60
    player_w = 330
    player_h = 35
    player_speed = 15
    player_radius = 40
    player_speed = 15
    player_rect = int(player_radius * 2 ** 0.5)
    player = pygame.Rect(330, 813, player_rect, player_rect)
    player2_radius = 40
    player2_speed = 15
    player2_rect = int(player2_radius * 2 ** 0.5)
    player2 = pygame.Rect(330, 10, player2_rect, player2_rect)
    dx, dy = 1, - 1
    f = pygame.font.SysFont('Arial', 26)
    sc = pygame.display.set_mode((WIDTH, HEIGHT))
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    score_1 = 0
    score_2 = 0
    ball_radius = 20
    ball_speed = 2
    ball_rect = int(ball_radius * 2 ** 0.5)
    ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, ball_rect, ball_rect)
    main1()