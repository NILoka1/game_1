


def help_cam(objects,ships,hp_block,cam_x,cam_y,players,bullets,mobs):
    players.cam(cam_x, cam_y)
    for block in objects:
        block.cam(cam_x, cam_y)
    for block in ships:
        block.cam(cam_x, cam_y)

    for block in hp_block:
        block.cam(cam_x, cam_y)
    for bull in bullets:
        bull.cam(cam_x,cam_y)
    for mob in mobs:
        mob.cam(cam_x,cam_y)


def help_bullets(bullets,objects):
    for bull in bullets:
        bull.plane(objects)


def help_damage(bullets,hp_block,mobs,players):
    for bull in bullets:
        bull.damage(hp_block, mobs,players)
    for mob in mobs:
        mob.damage(players)

def help_mob_walk(mobs,player):
    for mob in mobs:
        mob.mob_walk(player)