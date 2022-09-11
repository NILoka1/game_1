import pygame
from level.objects import cam


def direction(walk_x,walk_y):
    if walk_y[0] and not walk_x[1] and not walk_x[0] and not walk_y[1]:
        return 1
    if walk_y[1] and not walk_x[1] and not walk_x[0] and not walk_y[0]:
        return 5
    if walk_x[0] and not walk_y[0] and not walk_y[1] and not walk_x[1]:
        return 3
    if walk_x[1] and not walk_y[0] and not walk_y[1] and not walk_x[0]:
        return 7
    if walk_y[0] and walk_x[0] and not walk_y[1] and not walk_x[1]:
        return 2
    if walk_y[1] and walk_x[0] and not walk_y[0] and not walk_x[1]:
        return 4
    if walk_y[1] and walk_x[1] and not walk_y[0] and not walk_x[0]:
        return 6
    if walk_y[0] and walk_x[1] and not walk_y[1] and not walk_x[0]:
        return 8
    else:
        return 0



class bullet(pygame.sprite.Sprite):
    def __init__(self, n_x, n_y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.x = n_x
        self.rect = pygame.Rect(n_x, n_y, 5, 5)
        self.image = pygame.Surface([5, 5])
        self.image.fill(pygame.Color("black"))
        self.direction = direction


    def damage(self,hp_block,mobs):
        for i in (hp_block,mobs):
            for block in i:
                if pygame.sprite.collide_rect(block,self):
                    block.hp -=10
                    self.kill()
                    if block.hp == 0:
                        block.kill()


    def plane(self, obj):
        for block in obj:

            if pygame.sprite.collide_rect(block, self):
                self.kill()
        if self.direction == 0:
            self.kill()
        if self.direction == 1:
            self.rect[1] -= 4
            self.rect[0] += 0
        if self.direction == 2:
            self.rect[1] -= 4
            self.rect[0] += 4
        if self.direction == 3:
            self.rect[1] -= 0
            self.rect[0] += 4
        if self.direction == 4:
            self.rect[1] += 4
            self.rect[0] += 4
        if self.direction == 5:
            self.rect[1] += 4
            self.rect[0] += 0
        if self.direction == 6:
            self.rect[1] += 4
            self.rect[0] -= 4
        if self.direction == 7:
            self.rect[1] -= 0
            self.rect[0] -= 4
        if self.direction == 8:
            self.rect[1] -= 4
            self.rect[0] -= 4

    def cam(self, x, y):
        if x[0]:
            self.rect[0] += 2
        if x[1]:
            self.rect[0] -= 2
        if y[1]:
            self.rect[1] += 2
        if y[0]:
            self.rect[1] -= 2
