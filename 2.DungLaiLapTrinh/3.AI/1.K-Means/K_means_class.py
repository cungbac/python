
import pygame
from random import randint
import math

# Create function
def create_text_render(string):
    return font.render(string, True, WHITE)

class create_point:
    def __init__(self,x = None, y = None):
        self.x = x
        self.y = y

# def distance(p1,p2):
#     '''Calculate distance between 2 points'''
#     return math.sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)

def distance(p1,p2):
    '''Calculate distance between 2 points'''
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

# init pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((1200,700))

# set caption
pygame.display.set_caption("Kmeans visualization")

# Show screen
running = True
clock = pygame.time.Clock()

# Color creation
BACKGROUND = (214,214,214)
BLACK = (0,0,0)
BACKGROUND_PANEL = (249,255,230)
WHITE = (255, 255, 255)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (147,153,35)
PURPLE = (255,0,255)
SKY = (0,255,255)
ORANGE = (255,125,25)
GRAPE = (100,25,125)
GRASS = (55,155,65)

COLORS = [RED,GREEN,BLUE,YELLOW,PURPLE,SKY,ORANGE,GRAPE,GRASS]

# font creation
font = pygame.font.SysFont('sans', 40)
font_mouse = pygame.font.SysFont('sans', 20)

text_plus = create_text_render('+')
text_minus = create_text_render('-')
text_run = create_text_render('Run')
text_random = create_text_render('Random')
text_algorithm = create_text_render('Algorithm')
text_reset = create_text_render('Reset')

K = 0
error = 0
points = []
clusters = []
labels = []
distances = []

while running:
    clock.tick(60)
    screen.fill(BACKGROUND)

    # Draw interface
    # Draw panel
    pygame.draw.rect(screen, BLACK, (50,50,700,500))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (55,55,690,490))

    # K button +
    pygame.draw.rect(screen, BLACK, (850,50,50,50))
    screen.blit(text_plus, (865,50))

    # K button -
    pygame.draw.rect(screen, BLACK, (950,50, 50, 50))
    screen.blit(text_minus, (965,50))

    # K value
    text_k = font.render('K = ' + str(K), True, BLACK)
    screen.blit(text_k, (1050,50))

    # Run button
    pygame.draw.rect(screen, BLACK, (850,150,150,50))
    screen.blit(text_run,(900,150))

    # Random button
    pygame.draw.rect(screen, BLACK, (850,250,150,50))
    screen.blit(text_random, (850,250))

    # Reset button
    pygame.draw.rect(screen, BLACK, (850,550,150,50))
    screen.blit(text_reset, (850, 550))

    # Algorithm button
    pygame.draw.rect(screen, BLACK, (850,450,150,50))
    screen.blit(text_algorithm, (850, 450))

    # End draw interface
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Draw mouse position when mouse is in panel
    if 50 < mouse_x < 750 and 50 < mouse_y < 550:
        text_mouse = font_mouse.render('(' + str(mouse_x - 50) + ',' + str(mouse_y - 50) + ')', True, BLACK)
        screen.blit(text_mouse, (mouse_x + 10, mouse_y))

    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            running = False
        if even.type == pygame.MOUSEBUTTONDOWN:
            # Create points on panel
            if 50 < mouse_x < 750 and 50 < mouse_y < 550:
                labels = []
                point = create_point(mouse_x - 50, mouse_y - 50)
                points.append(point)
                print(points)
                print('in panel')
            # Change K button +
            if 850 < mouse_x < 900 and 50 < mouse_y < 100:
                K += 1
                print('Press K +')

            # Change K button - 
            if 950 < mouse_x < 1000 and 50 < mouse_y < 100:
                if K > 0:
                    K -= 1
                print('Press K -')

            # Random button
            if 850 < mouse_x < 1000 and 250 < mouse_y < 300:
                clusters = []
                labels = []
                error = 0
                for i in range(K):
                    random_point = create_point(randint(0, 700),randint(0, 500))
                    clusters.append(random_point)
                print('Press Random ...')
            
            # Run button
            if 850 < mouse_x < 1000 and 150 < mouse_y < 200:
                # Assign points to closet clusters
                labels = []
                for p in points:
                    distances_to_clusters = []
                    for c in clusters:
                        dis = (distance(p,c))
                        distances_to_clusters.append(dis)
                    min_distance = min(distances_to_clusters)
                    label = distances_to_clusters.index(min_distance)
                    labels.append(label)
                print(labels)
                print('Press Run ...')

                for i in range(len(clusters)):
                    sum_x = 0
                    sum_y = 0
                    count = 0
                    for j in range(len(points)):
                        if labels[j] == i:
                            sum_x = sum_x + points[j].x
                            sum_y = sum_y + points[j].y
                            count += 1
                    if count != 0:
                        new_cluster_x = sum_x / count
                        new_cluster_y = sum_y / count
                        new_cluster = create_point(new_cluster_x, new_cluster_y)
                        clusters[i] = new_cluster
                        print(clusters[i])
            
                for i in range(len(clusters)):
                    error_new = 0
                    for j in range(len(points)):
                        if labels[j] == i:
                            error_new = error_new + distance(clusters[i], points[j])
                    error = error + error_new

                # k_list = []
                # for k in range(len(clusters)):
                #     c_list = []
                #     for i in range(len(points)):
                #         if labels[i] == k:
                #             c_list.append(points[i])
                #     k_list.append(c_list)
                
                # print(k_list)

                # for i in range(len(k_list)):
                #     print(clusters[i])
                #     x_max = 0
                #     y_max = 0
                #     count = 0
                #     for j in range(len(k_list[i])):
                #         x_max = x_max + k_list[i][j][0]
                #         y_max = y_max + k_list[i][j][1]
                #         count += 1
                #     x_mean = x_max / len(k_list[i])
                #     y_mean = y_max / len(k_list[i])
                #     clusters[i][0] = x_mean
                #     clusters[i][1] = y_mean 
                #     print(clusters[i])


                # Update clusters

            # Reset button
            if 850 < mouse_x < 1000 and 550 < mouse_y < 600:
                print('Press Reset')

            # Algorithm button
            if 850 < mouse_x < 1000 and 450 < mouse_y < 500:
                print('Press Algorithm')

    # Error text
    text_error = font.render('Error = ' + str(error), True, BLACK)
    screen.blit(text_error, (850,350))

    # Draw clusters
    for i in range(len(clusters)):
        pygame.draw.circle(screen, COLORS[i], (clusters[i].x + 50, clusters[i].y + 50), 10)

    # Draw points
    for i in range(len(points)):
        pygame.draw.circle(screen, BLACK, (points[i].x + 50, points[i].y + 50), 6)
        if labels == []:
            pygame.draw.circle(screen, WHITE, (points[i].x + 50, points[i].y + 50), 5)
        else:
            pygame.draw.circle(screen, COLORS[labels[i]], (points[i].x + 50, points[i].y + 50), 5)

    pygame.display.flip()

pygame.quit()

