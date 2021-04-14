# import packages
import numpy as np
import matplotlib.pyplot as plt
import pygame
from sklearn.cluster import KMeans
import math
from PIL import Image

# create functions
def text_render(string, color):
    return font.render(string, True, color)

# init pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((1200,600))

# set caption
pygame.display.set_caption('Resize image using K-means')

# set colors
BACKGROUND = (25,40,65)
WHITE = (255, 255, 255)
LIGHT_BLUE = (195, 214, 242)

# font & text
font = pygame.font.SysFont('sans',35)

text_open_folder = text_render('Open Folder', LIGHT_BLUE)

# image
img1 = pygame.image.load('pic1.jpg')
img1 = pygame.transform.scale(img1,(300,400))

# show screen
running = True
clock = pygame.time.Clock()

# render
while running:
    clock.tick(60)
    screen.fill(BACKGROUND)

    screen.blit(img1,(20,20))

    # Open Folder
    pygame.draw.rect(screen, WHITE, (850,150,100,50))

    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            running = False
        if even.type == pygame.MOUSEBUTTONDOWN:
            print("click")

    pygame.display.flip()

pygame.quit()