## ========================= Happy New Year ========================= ##
## This script creates a simple fireworks for the 2022 new year
## Inspired by: https://www.youtube.com/watch?v=Yw4qIorzy-Q
## Also refered to: https://www.youtube.com/watch?v=jO6qQDNa2UY&t=16s
## ========================= Happy New Year ========================= ## 


import random
import numpy as np 
import pygame 
from fireworks import Spark, Fireworks



## draw canvas
WIDTH, HEIGHT = 900, 600
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
IMG_PATH = 'skyline.png'
BG = pygame.image.load(IMG_PATH).convert_alpha()
BG = pygame.transform.smoothscale(BG, (WIDTH, HEIGHT))
pygame.display.set_caption("Happy New Year")

## init frames
FPS = 60
NUM_SPARKS = 300
NUM_FRAMES = 900
NUM_FRIEWORKS = 200



def create_fireworks():
    fireworks = []
    for i in range(NUM_FRIEWORKS):
        x_loc = random.randint(0, WIDTH)
        y_loc = random.randint(0, HEIGHT/3)
        start_time = random.randint(0, NUM_FRAMES)
        start_color = (random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255))
        fireworks.append(Fireworks(x_loc, y_loc, start_time, start_color, NUM_SPARKS))
    
    return fireworks


def run(fireworks):
    SURFACE.blit(BG, (0, 0))
    for firework in fireworks:
        firework.tick()
        firework.draw(SURFACE)
    pygame.display.update() ## update to display



def main(fireworks):
    ## a while loop keep pygame running
    clock = pygame.time.Clock()
    is_running = True 
    while run:
        clock.tick(FPS)
        ## pygame tradition
        ## looping pygame event until QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        ## run fireworks
        run(fireworks)

    pygame.quit()




if __name__ == "__main__":
    fireworks = create_fireworks()
    main(fireworks)