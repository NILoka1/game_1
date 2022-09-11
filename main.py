import pygame

import help
from pers.player import Player
import time
from pers.walk import walk_direction
from pers.walk import cam_direction
from level import generation
from level.objects import HP_info
from level.objects import HP_info_bg
from level.weapon import bullet
from level.weapon import direction
from help import *

x_size = 390
y_size = 300
bg_colour = (0, 255, 0)

window = [x_size, y_size]
speed = 10
color = "white"


def main():
    pygame.init()
    screen = pygame.display.set_mode(window)
    pygame.display.set_caption("My_game")
    bg = pygame.Surface(window)
    bg.fill(pygame.Color(bg_colour))
    FPS = 60

    my_list = []
    objects = pygame.sprite.Group()
    ships = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    hp_block = pygame.sprite.Group()
    players = Player(15, 15, x_size, y_size)
    hp_info = HP_info(50, 50)
    hp_info_bg = HP_info_bg()

    walk_x = [False, False]
    walk_y = [False, False]
    cam_x = [False, False]
    cam_y = [False, False]
    generation.generation_lvl(objects, my_list, ships, hp_block, mobs)

    tik = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit("QUIT")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    direct = direction(walk_x, walk_y)
                    bullets.add(bullet(players.rect[0], players.rect[1], direct))

            walk_x, walk_y = walk_direction(event, walk_x, walk_y)
            cam_x, cam_y = cam_direction(event, cam_x, cam_y)



        help.help_cam(objects,ships,hp_block,cam_x,cam_y,players,bullets)
        help.help_bullets(bullets,objects)
        help.help_damage(bullets,hp_block,mobs,players)



        players.walk(walk_x[1], walk_x[0], walk_y[1], walk_y[0])
        players.collide(my_list, walk_x, walk_y)
        screen.blit(bg, (0, 0))

        hp = hp_info.size(players.hp)
        if hp == 1:
            hp_info.kill()
            exit()


        tik = players.no_damage(tik)

        hp_info_bg.sled(players.rect[0], players.rect[1])
        hp_info.sled(players.rect[0], players.rect[1])

        tik -= 1
        hp_block.draw(screen)
        bullets.draw(screen)
        hp_info_bg.draw(screen)
        hp_info.draw(screen)
        objects.draw(screen)
        players.draw(screen)
        ships.draw(screen)
        mobs.draw(screen)
        pygame.display.update()
        time.sleep(1 / FPS)


if __name__ == '__main__':
    main()

# реализовать диоганаль *
# реализовать получение урона персу *
# сделать несколько классов для наследования
# посмотреть алгоритм поиска в глубину и ширину
# архитектура проекта
