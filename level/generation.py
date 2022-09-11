import pygame

import mobs.mobs
from level.objects import Block
from level.objects import contener
from mobs.mobs import *

level = [
    "--------------------------"
    , "                          "
    , "                          "
    , "                          "
    , "                          "
    , "           111            "
    , "                          "
    , "                          "
    , "            +++           "
    , "                          "
    , "                          "
    , "                          "
    , "                          "
    , "                          "
    , "                          "
    , "                          "
    , "                          "
    , "     z                    "
    , "                          "
    , "--------------------------"]

size = [15, 15]


def generation_lvl(objects, my_list: list,ships_m,hp_block,zombies):
    x_pf = y_pf = 0
    for row in level:
        for col in row:
            if col == "-":
                block = Block(x_pf, y_pf,"red")
                objects.add(block)
                my_list.append(block)
            if col == "+":
                ships = Block(x_pf, y_pf,"blue")
                objects.add(ships)
                my_list.append(ships)
            if col == "1":
                cont = contener(x_pf,y_pf,"brown")
                hp_block.add(cont)
                my_list.append(cont)
            if col == "z":
                zombie = mobs.mobs.zombie(x_pf,y_pf)
                zombies.add(zombie)
            x_pf += size[0]
        y_pf += size[1]
        x_pf = 0
