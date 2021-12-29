## ========================= Happy New Year ========================= ##
## This script creates a simple fireworks for the 2022 new year
## Inspired by: https://www.youtube.com/watch?v=Yw4qIorzy-Q
## Also refered to: https://www.youtube.com/watch?v=jO6qQDNa2UY&t=16s
##
## Note:
##  This is not a serious project. I may not use pygame properly, but 
##  just somehow get pygame displays what I want
## ========================= Happy New Year ========================= ## 


import random
import numpy as np 
import pygame 
from fireworks import Spark, Fireworks



class DrawFireworks:
    """
    This class uses the pygame module, and pre-defined Spark and Firework 
    class to draw fireworks
    """

    def __init__(self, width:int, height:int, bg_path:str, fps:int, caption:str, 
                 num_sparks:int, num_fireworks:int, num_frames:int):
        """ 
        args: 
            (width, height): canvas dimension
            bg_path: path of background image
            fps: frame per second
            caption: caption of the canvas
            num_sparks: max number of sparks per frame
            num_fireworks: number of fireworks
            num_frames: number of frames
        """
        self.width, self.height = width, height
        self.bg_path = bg_path
        self.fps = fps
        self.caption = caption
        self.num_sparks = num_sparks 
        self.num_frames = num_frames 
        self.num_fireworks = num_fireworks

        ## create fireworks when init the class
        self.fireworks = list(self._create_fireworks())
        
        ## setup surface for pygame display
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load(self.bg_path).convert_alpha()
        self.bg = pygame.transform.smoothscale(self.bg, (self.width, self.height))
        pygame.display.set_caption(self.caption)
    

    def _create_fireworks(self):
        """support function to create fireworks"""
        for _ in range(self.num_fireworks):
            x_loc = random.randint(0, self.width)
            y_loc = random.randint(0, self.height/3)
            start_time = random.randint(0, self.num_frames)
            start_color = (random.randint(0, 255),
                           random.randint(0, 255),
                           random.randint(0, 255))
            yield Fireworks(x_loc, y_loc, start_time, start_color, self.num_sparks)
        #     self.fireworks.append(Fireworks(x_loc, y_loc, start_time, start_color, self.num_sparks))
        # return self.fireworks


    def _run_fireworks(self):
        self.surface.blit(self.bg, (0,0))
        for firework in self.fireworks:
            firework.tick()
            firework.draw(self.surface) 
        pygame.display.update()


    def main(self):
        ## a while loop keep pygame running
        clock = pygame.time.Clock()
        
        is_running = True 
        while is_running:
            clock.tick(self.fps)
            ## pygame tradition
            ## looping pygame event until QUIT
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
            ## run fireworks
            self._run_fireworks()

        pygame.quit()


if __name__ == "__main__":
    draw_fireworks = DrawFireworks(width=900, height=600, 
                                   bg_path='assets/lanzhou.png',
                                   fps=30, 
                                   caption='Happy New Year!', 
                                   num_sparks=200, 
                                   num_fireworks=200, 
                                   num_frames=900)
    draw_fireworks.main()