# Import des librairies
import pygame
import sys

pygame.init()

# Création de couleurs
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
color = black

# Taille du pinceau
size = 10

# Création de la fenêtre
width, height = 2560, 1440
screen = pygame.display.set_mode((width, height))
screen.fill(white)
pygame.draw.rect(screen, black, [100, 1290, 50, 50])
pygame.draw.rect(screen, red, [200, 1290, 50, 50])
pygame.draw.rect(screen, green, [300, 1290, 50, 50])
pygame.draw.rect(screen, blue, [400, 1290, 50, 50])


# Réinitialisation de la fenetre
def clear():
    siz = 10
    pos = 100
    for i in range(0, 8):
        pygame.draw.rect(screen, black, [pos, 1290, 50, 50], 3)
        pos += 100
        if i > 4:
            siz += 10
            pygame.draw.circle(screen, black, [pos - 75, 1315], siz/2)


clear()


# Information concernant la souris
down = False
isPressed = False
cx = []
cy = []

clock = pygame.time.Clock()

while True:
    clock.tick(240)
    x, y = pygame.mouse.get_pos()  # Récupération de la position de la souris
    cx.append(x)
    cy.append(y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Changement de couleurs
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 100 <= x <= 150 and 1290 <= y <= 1390:
                color = black
            elif 200 <= x <= 250 and 1290 <= y <= 1390:
                color = red
            elif 300 <= x <= 350 and 1290 <= y <= 1390:
                color = green
            elif 400 <= x <= 450 and 1290 <= y <= 1390:
                color = blue
            elif 500 <= x <= 550 and 1290 <= y <= 1390:
                color = white
            elif 600 <= x <= 650 and 1290 <= y <= 1390:
                size = 10
            elif 700 <= x <= 750 and 1290 <= y <= 1390:
                size = 20
            elif 800 <= x <= 850 and 1290 <= y <= 1390:
                size = 30
            else:
                isPressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
        # Dessine sur la fenêtre si un clic souris est enfoncé
        elif event.type == pygame.MOUSEMOTION and isPressed:
            pygame.draw.circle(screen, color, [x, y], size * 0.4)
            try:
                pygame.draw.line(screen, color, [cx[-2], cy[-2]], [cx[-1], cy[-1]], size)
            except:
                pass
        if event.type == pygame.KEYDOWN:
            # Réinitialise la fenêtre avec la touche echap
            if event.key == pygame.K_ESCAPE:
                screen.fill(white)
                pygame.draw.rect(screen, black, [100, 1290, 50, 50])
                pygame.draw.rect(screen, red, [200, 1290, 50, 50])
                pygame.draw.rect(screen, green, [300, 1290, 50, 50])
                pygame.draw.rect(screen, blue, [400, 1290, 50, 50])
                clear()
            # Sauvegarde l'image avec la touche espace
            elif event.key == pygame.K_SPACE:
                pygame.image.save(screen, 'dessin.png')

    # Update de la fenêtre
    pygame.display.flip()
    pygame.display.update()
