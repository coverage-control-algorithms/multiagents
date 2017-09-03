import random
import pygame
import matplotlib.pyplot as pl
import drawmisc
import agents as ag
import numpy as np
import logpostpro as lp

# setup simulation
WIDTH = 1000
HEIGHT = 1000

CENTERX = WIDTH/2
CENTERY = WIDTH/2

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

size = [WIDTH, HEIGHT]
screen = pygame.display.set_mode(size)

numagents = 100
listofunis = []

for i in range(numagents):
    listofunis.append(ag.AgentUnicycle(WHITE, i, 1000*np.random.rand(2), 50*np.random.rand(2)))

for uni in listofunis:
    uni.traj_draw = False

# run simulation
pygame.init()
clock = pygame.time.Clock()
fps = 50
dt = 1.0/fps
time = 0

runsim = True
while(runsim):
    screen.fill(BLACK)

    for uni in random.sample(listofunis, 10):
        uni.neighbors = []
        for nei in listofunis:
            if(np.linalg.norm(uni.pos - nei.pos) < 50):
                uni.neighbors.append(nei)

    for uni in listofunis:
        uni.flocking(dt)
        if(uni.pos[0] < 0 or uni.pos[0] > WIDTH or uni.pos[1] < 0 or uni.pos[1] > HEIGHT):
            uni.pos = 1000*np.random.rand(2)
            uni.vel = 50*np.random.rand(2)
            uni.neighbors = []
        uni.draw(screen)

    print(clock.get_fps())
    clock.tick(fps)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endtime = pygame.time.get_ticks()
            pygame.quit()
            runsim = False

