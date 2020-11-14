"""
Le module asteroid permet de représenter un astéroïde.
"""

import random
import pygame


class Asteroid(pygame.sprite.Sprite):
    """
    La classe Asteroid permet de représenter un astéroïde.
    """

    def __init__(self, game):
        """
        Constructeur de la classe
        """
        super().__init__()
        self.game = game
        self.atk = 1
        self.image = pygame.image.load('img/asteroid.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = random.randint(0, 380 - self.rect.width)
        self.velocity = random.randint(1, 10)

    def avancer(self):
        """
        Méthode permettant à l'astéroïde d'avancer dans la fenêtre.
        """
        if not self.rect.x < -self.rect.width:
            if self.game.detect_collision(self, self.game.all_player):
                self.game.player.damage(self.atk)

            self.rect.x -= self.velocity
        else:
            self.reaparition()

    def reaparition(self):
        """
        Méthode gérant la réaparition de l'astéroïde
        (permet d'éviter la création de multiples objets).
        """
        self.rect.x = 697 + random.randint(0, 300)
        self.rect.y = random.randint(0, 380 - self.rect.width)
        self.velocity = random.randint(1, 3)
