import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.max_hp = 100
        self.hp = self.max_hp
        self.atk = 10
        self.velocity = 3
        self.image = pygame.image.load('img/spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 200

    def damage(self, montant):
        if self.hp - montant  > montant:
            self.hp -= montant
        else:
            self.hp = 0

    def maj_hp(self, surface):
        # couleur rgb vert
        bar_color = (111, 210, 46)    #couleur rgb vert

        # couleur arrirere plan (gris)
        bar_back = (60, 63, 60)

        # position (x,y) + largeur (w) + epaisseur (h) de la jauge
        pos_bar = [self.rect.x, self.rect.y - 10, self.hp, 7]
        pos_back = [self.rect.x, self.rect.y - 10, self.max_hp, 7]

        # dessin de la jauge
        pygame.draw.rect(surface, bar_back, pos_back)
        pygame.draw.rect(surface, bar_color, pos_bar)

    def mv_up(self):
        self.rect.y -= self.velocity

    def mv_down(self):
        self.rect.y += self.velocity