import pygame


speed = 3
size_player = [15, 15]

color = "black"


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, x_size, y_size):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.last_hp = 100
        self.hp = 100
        self.x_size = x_size
        self.y_size = y_size
        self.image = pygame.Surface(size_player)
        self.image.fill(pygame.Color(color))
        self.rect = pygame.Rect(x, y, size_player[0], size_player[1])

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def walk(self, left, right, down, up):
        if right and not up and not down:
            self.rect.x += speed
            if self.rect.x > self.x_size - size_player[0]:
                self.rect.x = self.x_size - size_player[0]
        if left and not up and not down:
            self.rect.x -= speed
            if self.rect.x < 0:
                self.rect.x = 0

        if down and not right and not left:
            self.rect.y += speed
            if self.rect.y < 0:
                self.rect.y = 0
        if up and not right and not left:
            self.rect.y -= speed
            if self.rect.y > self.y_size - size_player[0]:
                self.rect.y = self.y_size - size_player[0]

        if up and right:
            self.rect.y -= 2
            self.rect.x += 2

        if down and right:
            self.rect.y += 2
            self.rect.x += 2

        if down and left:
            self.rect.y += 2
            self.rect.x -= 2

        if up and left:
            self.rect.y -= 2
            self.rect.x -= 2



    def no_damage(self,tik):
        if tik <= 0:
            tik = 30
            self.last_hp = self.hp
        else:
            self.hp = self.last_hp
        tik-=1
        return tik

    def collide(self, my_list,walk_x,walk_y):
        walk = ""
        if walk_x[0] and not (walk_y[1] or walk_y[0]):
            walk = "r"
        if walk_x[1] and not (walk_y[1] or walk_y[0]):
            walk = "l"
        if walk_y[0] and not (walk_x[1] or walk_x[0]):
            walk = "u"
        if walk_y[1] and not (walk_x[1] or walk_x[0]):
            walk = "d"

        if walk_x[0] and walk_y[0]:
            walk = "ru"
        if walk_x[0] and walk_y[1]:
            walk = "rd"
        if walk_x[1] and walk_y[0]:
            walk = "lu"
        if walk_x[1] and walk_y[1]:
            walk = "ld"

        for block in my_list:
            if pygame.sprite.collide_rect(block, self):
                if block.collour == "blue":
                        self.hp -= 5



                if walk == "r":
                    self.rect.x = block.rect[0] - self.rect[2]
                if walk == "l":
                    self.rect.x = block.rect[0] + block.rect[2]
                if walk == "u":
                    self.rect.y = block.rect[1] + block.rect[3]
                if walk == "d":
                    self.rect.y = block.rect[1] - self.rect[3]

                if walk == "ru":
                    if (self.rect.x + self.rect[2]) - block.rect[0] < block.rect[1]+block.rect[3] - self.rect.y:
                        self.rect.x = block.rect[0] - self.rect[2]
                    elif (self.rect.x + self.rect[2]) - block.rect[0] == block.rect[1]+block.rect[3] - self.rect.y:
                        self.rect.x = block.rect[0] - self.rect[2]
                        self.rect.y = block.rect[1] + block.rect[3]
                    else:
                        self.rect.y = block.rect[1] + block.rect[3]
                if walk == "rd":
                    if (self.rect.x + self.rect[2]) - block.rect[0] < self.rect[1]+self.rect[3] - block.rect[1]:
                        self.rect.x = block.rect[0] - self.rect[2]
                    elif (self.rect.x + self.rect[2]) - block.rect[0] == self.rect[1]+self.rect[3] - block.rect[1]:
                        self.rect.x = block.rect[0] - self.rect[2]
                        self.rect.y = block.rect[1] - self.rect[3]
                    else:
                        self.rect.y = block.rect[1] - self.rect[3]
                if walk == "lu":
                    if block.rect[0]+block.rect[2] - self.rect[0] < block.rect[1]+block.rect[3] - self.rect[1]:
                        self.rect[0] = block.rect[0]+block.rect[2]
                    elif block.rect[0]+block.rect[2] - self.rect[0] == block.rect[1]+block.rect[3] - self.rect[1]:
                        self.rect[0] = block.rect[0] + block.rect[2]
                        self.rect[1] = block.rect[1] + block.rect[3]
                    else:
                        self.rect[1] = block.rect[1] + block.rect[3]
                if walk == "ld":
                    if self.rect[1]+self.rect[3] - block.rect[1] < block.rect[0]+block.rect[2]-self.rect[0]:
                        self.rect[1] = block.rect[1] - block.rect[3]
                    elif self.rect[1]+self.rect[3] - block.rect[1] == block.rect[0]+block.rect[2]-self.rect[0]:
                        self.rect[1] = block.rect[1] - block.rect[3]
                        self.rect[0] = block.rect[0] + block.rect[2]
                    else:
                        self.rect[0] = block.rect[0] + block.rect[2]


    def cam(self, x, y):
        if x[0]:
            self.rect[0] += 2
        if x[1]:
            self.rect[0] -= 2
        if y[1]:
            self.rect[1] += 2
        if y[0]:
            self.rect[1] -= 2

