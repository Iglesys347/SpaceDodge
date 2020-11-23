"""
Le main permettant de lancer une partie.
"""

import pygame

from game import Game


pygame.init()

pygame.display.set_caption("SpaceDodge")

fenetre = pygame.display.set_mode((697, 380))
# Chargement de l'image de fond
fond = pygame.image.load("img/space.jpg")

game = Game()

score = 0

continuer = True


while continuer:
    # Collage de l'image de fond
    fenetre.blit(fond, (0, 0))

    if game.is_playing:
        # declenchement de la partie
        game.maj(fenetre)
        score += 1
    else:
        score = 0
        main_screen_font = pygame.font.SysFont('impact', 40)
        main_screen_rendu = main_screen_font.render("Appuyez sur la touche espace pour débuter",
                                                    True,
                                                    (255, 255, 255))
        fenetre.blit(main_screen_rendu, (50, 180))

        rules_font = pygame.font.SysFont('impact', 25)
        rules_rendu = rules_font.render("Utilisez les flèches haut et bas pour déplacer le vaisseau",
                                        True,
                                        (255, 255, 255))
        fenetre.blit(rules_rendu, (120, 230))
        if game.pressed.get(pygame.K_SPACE):
            game.maj_game_state()
            print("Debut du jeu")

    score_font = pygame.font.SysFont('impact', 25)
    score_rendu = score_font.render(
        "Score : "+str(score), True, (255, 255, 255), (0, 0, 0))

    fenetre.blit(score_rendu, (580, 40))

    # MAJ
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            pygame.quit()
            print("Fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
