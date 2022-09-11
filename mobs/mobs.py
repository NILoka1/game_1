import pygame


class zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.hp = 40
        self.x_size = 15
        self.y_size = 15
        self.image = pygame.Surface([self.x_size, self.y_size])
        self.image.fill(pygame.Color((1, 50, 32)))
        self.rect = pygame.Rect(x, y, self.x_size, self.y_size)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


    def damage(self,players):
        if pygame.sprite.collide_rect(self,players):
            players.hp -= 10
            if players.hp <= 0:
                players.kill()


