from pygame import *
from random import randint
from time import time as timer
tanki = ["tanki.png", "tanki_right.png","tanki_left.png", "tank_down.png",]
bullet = ["bullet.png", "bullet_down.png", "bullet_left.png", "bullet_right.png"]


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, speed_x, speed_y, player_higth, player_width):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_higth, player_width))
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, speed_x, speed_y, player_higth, player_width):
        super().__init__(player_image, player_x, player_y, speed_x, speed_y, player_higth, player_width)
        self.direction = "UP"

    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5 and not sprite.spritecollide(self, blocks, False):
            self.rect.y -= self.speed_y
            self.image = transform.scale(image.load(tanki[0]), (100, 100))
            self.direction = "UP"
        elif keys[K_s] and self.rect.y < 980 and not sprite.spritecollide(self, blocks, False):
            self.rect.y += self.speed_y
            self.image = transform.scale(image.load(tanki[3]), (100, 100))
            self.direction = "DOWN"
        elif keys[K_a] and self.rect.x > 5 and not sprite.spritecollide(self, blocks, False):
            self.rect.x -= self.speed_x
            self.image = transform.scale(image.load(tanki[2]), (100, 100))
            self.direction = "LEFT"
        elif keys[K_d] and self.rect.x < 1820 and not sprite.spritecollide(self, blocks, False):
            self.rect.x += self.speed_x
            self.image = transform.scale(image.load(tanki[1]), (100, 100))
            self.direction = "RIGHT"
        if sprite.spritecollide(self, blocks, False):
            self.rect.y -= 1
    def fire(self):
        bullets.add(Bullet("bullet.png", self.rect.centerx, self.rect.centery, self.speed_x, 5, 20, 30))
class Bullet(GameSprite):
    def update(self):
        if player.direction == "UP":
            self.image = transform.scale(image.load(bullet[0]), (20, 30))
            self.rect.y -= self.speed_x
            if self.rect.y < 0:
                self.kill()    
        elif player.direction == "DOWN":
            self.image = transform.scale(image.load(bullet[1]), (20, 30))
            self.rect.y += self.speed_x
            if self.rect.y > 1080:
                self.kill()
        elif player.direction == "LEFT":
            self.image = transform.scale(image.load(bullet[2]), (20, 30))
            self.rect.x -= self.speed_x
            if self.rect.x < 0:
                self.kill()
        elif player.direction == "RIGHT":
            self.image = transform.scale(image.load(bullet[3]), (20, 30))
            self.rect.x += self.speed_x
            if self.rect.x > 1920:
                self.kill()
class Blokc(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_higth, player_width):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_higth, player_width))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
player = Player(tanki[0], 350, 500, 5, 5, 100, 100)
bullets = sprite.Group()
blocks = sprite.Group()
blocks.add(Blokc("metal_wall.png", 500, 500, 110, 110))
blocks.add(Blokc("metal_wall.png", 500, 610, 110, 110))
blocks.add(Blokc("metal_wall.png", 500, 390, 110, 110))
blocks.add(Blokc("metal_wall.png", 500, 830, 110, 110))
blocks.add(Blokc("metal_wall.png", 500, 170, 110, 110))
blocks.add(Blokc("metal_wall.png", 1250, 500, 110, 110))
blocks.add(Blokc("metal_wall.png", 1250, 610, 110, 110))
blocks.add(Blokc("metal_wall.png", 1250, 390, 110, 110))
blocks.add(Blokc("metal_wall.png", 1250, 830, 110, 110))
blocks.add(Blokc("metal_wall.png", 1250, 170, 110, 110))
blocks.add(Blokc("metal_wall.png", 850, 830, 110, 110))
blocks.add(Blokc("metal_wall.png", 850, 170, 110, 110))
blocks.add(Blokc("metal_wall.png", 960, 830, 110, 110))
blocks.add(Blokc("metal_wall.png", 960, 170, 110, 110))

window = display.set_mode((0, 0), FULLSCREEN)
display.set_caption("pixel-tanki")
FPS = 60
clock = time.Clock()
background = transform.scale(image.load("desert.png"), (1920, 1080))
run = True
game = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
    if game != True:
        window.blit(background, (0, 0))
        player.reset()
        player.update()
        bullets.draw(window)
        bullets.update()
        blocks.draw(window)
    display.update()
    clock.tick(FPS)