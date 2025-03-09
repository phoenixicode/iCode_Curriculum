from PIL.ImageChops import screen
from easytello import tello
import pygame

drone=tello.Tello()
window=pygame.display.set_mode([346, 425])
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                drone.forward(20)
            if event.key == pygame.K_DOWN:
                drone.back(20)
            if event.key == pygame.K_LEFT:
                drone.left(20)
            if event.key == pygame.K_RIGHT:
                drone.right(20)
            if event.key == pygame.K_SPACE:
                drone.takeoff()
            if event.key == pygame.K_w:
                drone.up(20)
            if event.key == pygame.K_s:
                drone.down(20)
            if event.key == pygame.K_l:
                drone.land()
    pygame.display.update()
