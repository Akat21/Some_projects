import pygame
from Network import Network
from Player import Player

width = 500
height = 500

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Client")

def redrawWindow(player,player2,win):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    pygame.init()
    n = Network()
    p = n.getP()
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        p2 = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        p.move() 
        redrawWindow(p, p2, win)
    pygame.quit()

main()