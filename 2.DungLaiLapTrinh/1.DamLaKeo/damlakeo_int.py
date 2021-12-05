import pygame
from random import randint

# Initial
pygame.init()

pygame.display.set_caption('Rock - Paper - Scissors')

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

square = 50

GREY = (224,224,224)
BLACK = (0,0,0)
WHITE = (255, 255, 255)
BLUE = (0, 102, 204)
RED = (255, 51, 51 )

font = pygame.font.SysFont('sans',25)
text1 = font.render('Hay chon: ', True, BLACK)
text2 = font.render('Ban chon: ', True, BLACK)
text3 = font.render('Computer chon: ', True, BLACK)
text4 = font.render('Ket qua :', True, BLACK)
text5 = font.render('Ban thang', True, BLACK)
text6 = font.render('Hai ben hoa nhau', True, BLACK)
text7 = font.render('Ban thua cmnr', True, BLACK)
text8 = font.render('Tong so luot choi :', True, BLACK)
text9 = font.render('Ty so :', True, BLACK)
text10 = font.render('Nhan xet :', True, BLACK)
text11 = font.render('Ban deo biet choi', True, BLUE)
text12 = font.render('Dm, lai hoa', True, BLUE)
text13 = font.render('Ban choi gioi vai loz', True, BLUE)

dam_image = pygame.image.load('dam.png')
dam_image = pygame.transform.scale(dam_image,(square,square))
la_image = pygame.image.load('la.png')
la_image = pygame.transform.scale(la_image,(square,square))
keo_image = pygame.image.load('keo.png')
keo_image = pygame.transform.scale(keo_image, (square,square))

appear_dam_y = False
appear_la_y = False
appear_keo_y = False

appear_dam_c = False
appear_la_c = False
appear_keo_c = False

appear_thang = False
appear_hoa = False
appear_thua = False

playing_time = 0
score_y = 0
score_c = 0

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    computer = randint(0,2)

    # Fill the screen
    screen.fill(GREY)

    # Get mouse_x, mouse_y
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Insert option text
    screen.blit(text1, (30,80))
    screen.blit(text2,(30,155))
    screen.blit(text3, (30,230))
    screen.blit(text4, (30,305))
    screen.blit(text8, (30,380))
    screen.blit(text9, (30,455))
    screen.blit(text10, (30,530))

    # Draw Rock, Paper, Scissors
    # pygame.draw.rect(screen, BLUE, (150, 60, square, square))
    screen.blit(dam_image, (150,60))
    # pygame.draw.rect(screen, BLUE, (230, 60, square, square))
    screen.blit(la_image, (230,60))
    # pygame.draw.rect(screen, BLUE, (310, 60, square, square))
    screen.blit(keo_image, (310,60))
    
    # Show your choice
    #pygame.draw.rect(screen, BLUE, (230, 140, square, square))
    if appear_dam_y:
        screen.blit(dam_image, (230,140))
    if appear_la_y:
        screen.blit(la_image, (230,140))
    if appear_keo_y:
        screen.blit(keo_image, (230,140))

    # Show computer choice
    # pygame.draw.rect(screen, BLUE, (230, 220, square, square))
    if appear_dam_c:
        screen.blit(dam_image, (230,220))
    if appear_la_c:
        screen.blit(la_image, (230,220))
    if appear_keo_c:
        screen.blit(keo_image, (230,220))

    # Show result
    if appear_thang:
        screen.blit(text5, (180,305))
    if appear_hoa:
        screen.blit(text6, (180,305))
    if appear_thua:
        screen.blit(text7, (180,305))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if (150 < mouse_x < 200) and (60 < mouse_y < 110):
                    appear_dam_y = True
                    appear_keo_y = False
                    appear_la_y = False
                    if computer == 0:
                        appear_dam_c = True
                        appear_la_c = False
                        appear_keo_c = False
                        appear_thang = False
                        appear_hoa = True
                        appear_thua = False
                        playing_time += 1
                    elif computer == 1:
                        appear_dam_c = False
                        appear_la_c = True
                        appear_keo_c = False
                        appear_thang = False
                        appear_hoa = False
                        appear_thua = True
                        playing_time += 1
                        score_c += 1
                    else:
                        appear_dam_c = False
                        appear_la_c = False
                        appear_keo_c = True
                        appear_thang = True
                        appear_hoa = False
                        appear_thua = False
                        playing_time += 1
                        score_y += 1
                    print(computer)
                if (230 < mouse_x < 280) and (60 < mouse_y < 110):
                    appear_dam_y = False
                    appear_la_y = True
                    appear_keo_y = False
                    if computer == 0:
                        appear_dam_c = True
                        appear_la_c = False
                        appear_keo_c = False
                        appear_thang = True
                        appear_hoa = False
                        appear_thua = False
                        playing_time += 1
                        score_y += 1
                    elif computer == 1:
                        appear_dam_c = False
                        appear_la_c = True
                        appear_keo_c = False
                        appear_thang = False
                        appear_hoa = True
                        appear_thua = False
                        playing_time += 1
                    else:
                        appear_dam_c = False
                        appear_la_c = False
                        appear_keo_c = True
                        appear_thang = False
                        appear_hoa = False
                        appear_thua = True
                        playing_time += 1
                        score_c += 1
                    print(computer)
                if (310 < mouse_x < 360) and (60 < mouse_y < 110):
                    appear_dam_y = False
                    appear_la_y = False
                    appear_keo_y = True
                    if computer == 0:
                        appear_dam_c = True
                        appear_la_c = False
                        appear_keo_c = False
                        appear_thang = False
                        appear_hoa = False
                        appear_thua = True
                        playing_time += 1
                        score_c += 1
                    elif computer == 1:
                        appear_dam_c = False
                        appear_la_c = True
                        appear_keo_c = False
                        appear_thang = True
                        appear_hoa = False  
                        appear_thua = False
                        playing_time += 1
                        score_y += 1
                    else:
                        appear_dam_c = False
                        appear_la_c = False
                        appear_keo_c = True
                        appear_thang = False
                        appear_hoa = True
                        appear_thua = False
                        playing_time += 1
                    print(computer)
    # Show score
    text_time = str(playing_time)
    text_time_render = font.render(text_time,True,BLACK)
    screen.blit(text_time_render, (230, 380))

    text_score = str(score_y) + '    -    ' + str(score_c)
    text_score_render = font.render(text_score,True, RED)
    screen.blit(text_score_render, (200, 455))

    # Show comment
    if score_y < score_c:
        screen.blit(text11, (180, 530))
    elif score_y == score_c:
        if score_y != 0 and score_c != 0:
            screen.blit(text12, (180,530))
        pass
    else:
        screen.blit(text13, (180, 530))

    pygame.display.flip()

pygame.quit()
    