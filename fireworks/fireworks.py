## ========================= Happy New Year ========================= ##
## This script creates a simple fireworks for the 2022 new year
## Inspired by: https://www.youtube.com/watch?v=Yw4qIorzy-Q
## Also refered to: https://www.youtube.com/watch?v=jO6qQDNa2UY&t=16s
## ========================= Happy New Year ========================= ## 


import random
import numpy as np 
import pygame 
from typing import Tuple


class Spark:
    """ Create each single spark"""

    def __init__(self, x0:int, y0:int, vx0:float, vy0:float, 
                 color0:Tuple[int], lifetime:int):
        """
        initial the spark location and speed. The idea here is to simulate the 
        status (i.e., location) of sparks in each frame
        ------
        (x0, y0): initial coordinate 
        (vx0, vy0): initial velocity 
        (color0): inital color
        lifetime: number of frames
        """
        ## init the class
        self.x0, self.y0 = x0, y0
        self.vx0, self.vy0 = vx0, vy0
        self.color0 = color0 
        self.finalcolor = (0, 0, 0) # final black color
        self.lifetime = lifetime

        ## internal veriables
        self.x, self.y = self.x0, self.y0 
        self.fx, self.fy = float(self.x), float(self.y)
        self.vx, self.vy = self.vx0, self.vy0 
        self.color = self.color0
        self.frame_spark = 0
        self.active_spark = True
        
        ## compute color fade 
        r0, g0, b0 = self.color0
        rf, gf, bf = self.finalcolor
        self.r_fade = (r0 - rf) / self.lifetime
        self.g_fade = (g0 - gf) / self.lifetime
        self.b_fade = (b0 - bf) / self.lifetime


    def tick(self):
        """
        update the spark location per frame
        """
        ## update location
        self.fx += self.vx
        self.fy += self.vy 
        self.x, self.y = int(self.fx), int(self.fy)

        ## update color 
        (r_new, g_new, b_new) = self.color 
        r_new = max(0, int(r_new - self.r_fade))
        g_new = max(0, int(g_new - self.g_fade))
        b_new = max(0, int(b_new - self.b_fade))
        self.color = (r_new, g_new, b_new)

        ## track frames
        if (self.frame_spark >= self.lifetime):
            self.active_spark=False
        self.frame_spark += 1


    def draw(self, surface):
        """draw one spark"""
        if self.active_spark:
            return pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, 4,4))
        else:
            return None 



class Fireworks:
    """ The fireworks class is a colloection of Spark class"""

    def __init__(self, x_loc:int, y_loc:int, start_time:int, 
                 start_color:Tuple[int], num_sparks:int):
        """
        init the fireworks with multiple sparks. 
        ------
        (x_loc, y_loc): start location of sparks
        start_time: at which frame to start the spart
        start_color: color of the spark
        """
        self.x_loc, self.y_loc = x_loc, y_loc 
        self.start_time = start_time 
        self.start_color = start_color 
        self.num_sparks = num_sparks

        self.frame_fireworks = 0
        self.active_fireworks = True
        self.sparks = [] ## hold all sparks 


    def tick(self):
        """
        start the spark when it is the time (start_time == frame_fireworks)
        """
        ## generate sparks
        if self.frame_fireworks == self.start_time:
            for i in range(self.num_sparks):
                ## init each spark
                rand_direction = random.uniform(0, np.pi)
                rand_velocity = random.uniform(-2,2)
                curnt_vx = rand_velocity * np.sin(rand_direction)
                curnt_vy = rand_velocity * np.cos(rand_direction)
                lifetime = random.randint(30, 120)
                ## append each spark 
                self.sparks.append(Spark(self.x_loc, self.y_loc, 
                                         curnt_vx, curnt_vy, 
                                         self.start_color, lifetime))

        ## sparks motions
        elif self.frame_fireworks > self.start_time:
            ## track the number of active sparks
            num_active = 0   
            ## compute the motion of sparks
            for spark in self.sparks:
                spark.tick()
                if spark.active_spark:
                    num_active += 1
            ## check the active of the Fireworks class 
            if num_active == 0 :
                self.active_fireworks = False

        self.frame_fireworks += 1


    def draw(self, surface):
        if self.active_fireworks and (self.frame_fireworks >= self.start_time):
            for spark in self.sparks:
                if spark.active_spark:
                    spark.draw(surface)