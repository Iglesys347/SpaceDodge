import pygame
import random

class Asteroid(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.atk = 1
        self.image = pygame.image.load('img/asteroid.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = random.randint(0, 380 - self.rect.width)
        self.velocity = random.randint(1, 10)


    def avancer(self):
        if not self.rect.x < -self.rect.width:
            if self.game.detect_collision(self, self.game.all_player):
                self.game.player.damage(self.atk)

            self.rect.x -= self.velocity
        else:
            self.reaparition()

    def reaparition(self):
        self.rect.x = 697 + random.randint(0, 300)
        self.rect.y = random.randint(0, 380 - self.rect.width)
        self.velocity = random.randint(1, 3)


