"""
Le module game qui gère une partie de jeu.
"""

import pygame

from player import Player
from asteroid import Asteroid


class Game:
    """
    La classe game qui va gérer le bon déroulement d'une partie.
    """

    def __init__(self):
        """
        Le constructeur de la classe.
        """
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
        """
        Fonction permettant de mettre à jour l'affichage de la fenêtre.
        """
        window.blit(self.player.image, self.player.rect)

        self.player.maj_hp(window)

        if self.player.health <= 0:
            self.is_playing = False
            self.reset()
        else:

            for asteroids in self.all_asteroid:
                asteroids.avancer()
            self.all_asteroid.draw(window)

            pos_vaisseau = self.player.rect.y + self.player.rect.width
            if self.pressed.get(pygame.K_DOWN) and pos_vaisseau < 380:
                self.player.mv_down()
            elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 0:
                self.player.mv_up()

    def detect_collision(self, sprite, group):
        """
        Fonction pour détecter la collision entre 2 sprites.
        """
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_asteroid(self):
        """
        Fonction permettant de faire apparaître un atéroïde.
        """
        self.all_asteroid.add(Asteroid(self))

    def maj_game_state(self):
        """
        Met à jour l'état de la partie (en cours ou finie)
        """
        self.is_playing = not self.is_playing

    def reset(self):
        """
        Permet de réinitialiser les différents paramètres pour pouvoir commencer un nouvelle partie.
        """
        self.player.health = self.player.max_hp
        self.player.rect.y = 200
        for asteroids in self.all_asteroid:
            asteroids.reaparition()
