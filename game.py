import pygame

from player import Player
from asteroid import Asteroid

class Game:

    def __init__(self):
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)

        self.all_asteroid = pygame.sprite.Group()

        # Dictionnaire contenant les touches pressees
        self.pressed = {}

        self.spawn_asteroid()
        self.spawn_asteroid()
        self.spawn_asteroid()
        self.spawn_asteroid()
        self.spawn_asteroid()
        self.spawn_asteroid()

        self.is_playing = False

    def maj(self, window):
        window.blit(self.player.image, self.player.rect)

        self.player.maj_hp(window)

        if self.player.hp <= 0:
            self.is_playing = False
            self.reset()
        else:

            for asteroids in self.all_asteroid:
                asteroids.avancer()
            self.all_asteroid.draw(window)

            if self.pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.rect.width < 380:
                self.player.mv_down()
            elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 0:
                self.player.mv_up()

    def detect_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_asteroid(self):
        self.all_asteroid.add(Asteroid(self))

    def maj_game_state(self):
        self.is_playing = not self.is_playing

    def reset(self):
        self.player.hp = self.player.max_hp
        self.player.rect.y = 200
        for asteroids in self.all_asteroid:
            asteroids.reaparition()