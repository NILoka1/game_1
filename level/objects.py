import pygame

size_block = [15, 15]
speed = 2


class cam(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0, 0, 15, 15)

    def cam(self, x, y):
        if x[0]:
            self.rect[0] += speed
        if x[1]:
            self.rect[0] -= speed
        if y[1]:
            self.rect[1] += speed
        if y[0]:
            self.rect[1] -= speed


class Block(cam):
    def __init__(self, x, y, collour):
        pygame.sprite.Sprite.__init__(self)
        self.x_size = 15
        self.y_size = 15
        self.collour = collour
        self.image = pygame.Surface(size_block)
        self.image.fill(pygame.Color(collour))
        self.rect = pygame.Rect(x, y, self.x_size, self.y_size)

    #def cam(self, x, y):
        #if x[0]:
            #self.rect[0] += speed
        #if x[1]:
            #self.rect[0] -= speed
        #if y[1]:
            #self.rect[1] += speed
        #if y[0]:
            #self.rect[1] -= speed


class HP_info(cam):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x_size = 50
        self.y_size = 3
        self.image = pygame.Surface([self.x_size,self.y_size])
        self.image.fill("red")
        self.rect = pygame.Rect(x,y,self.x_size,self.y_size)


    def size(self,hp):
        if hp//2 > 0:
            hp=hp//2
            self.image = pygame.transform.scale(self.image,[hp,3])
        else:
            return 1

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def sled(self,x,y):
        self.rect[0] = x-17
        self.rect[1] = y-10


class HP_info_bg(cam):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x_size = 52
        self.y_size = 5
        self.image = pygame.Surface([self.x_size, self.y_size])
        self.image.fill("black")
        self.rect = pygame.Rect(0,0, self.x_size, self.y_size)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def sled(self,x,y):
        self.rect[0] = x-18
        self.rect[1] = y-11



class contener(pygame.sprite.Sprite):
    def __init__(self, x, y, collour):
        pygame.sprite.Sprite.__init__(self)
        self.hp = 30
        self.x_size = 15
        self.y_size = 15
        self.collour = collour
        self.image = pygame.Surface(size_block)
        self.image.fill(pygame.Color(collour))
        self.rect = pygame.Rect(x, y, self.x_size, self.y_size)



    def cam(self, x, y):
        if x[0]:
            self.rect[0] += speed
        if x[1]:
            self.rect[0] -= speed
        if y[1]:
            self.rect[1] += speed
        if y[0]:
            self.rect[1] -= speed

