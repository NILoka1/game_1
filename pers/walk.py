import pygame
from pygame import event
from pers.player import Player

def walk_direction(event,walk_x,walk_y):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
            walk_x[0] = True
        if event.key == pygame.K_a:
            walk_x[1] = True
        if event.key == pygame.K_w:
            walk_y[0] = True
        if event.key == pygame.K_s:
            walk_y[1] = True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
            walk_x[0] = False
        if event.key == pygame.K_a:
            walk_x[1] = False
        if event.key == pygame.K_w:
            walk_y[0] = False
        if event.key == pygame.K_s:
            walk_y[1] = False

    return walk_x, walk_y


def cam_direction(event,cam_x,cam_y):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            cam_x[0] = True
        if event.key == pygame.K_LEFT:
            cam_x[1] = True
        if event.key == pygame.K_UP:
            cam_y[0] = True
        if event.key == pygame.K_DOWN:
            cam_y[1] = True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            cam_x[0] = False
        if event.key == pygame.K_LEFT:
            cam_x[1] = False
        if event.key == pygame.K_UP:
            cam_y[0] = False
        if event.key == pygame.K_DOWN:
            cam_y[1] = False

    return cam_x, cam_y
