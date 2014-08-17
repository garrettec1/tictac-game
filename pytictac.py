import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)

size = [500,400]
screen = pygame.display.set_mode(size)

def draw_board():
    pygame.draw.line(screen, blue, [100, 150], [400,150], 5)
    pygame.draw.line(screen, blue, [100, 250], [400,250], 5)
    pygame.draw.line(screen, blue, [200, 50], [200,350], 5)
    pygame.draw.line(screen, blue, [300, 50], [300,350], 5)
    pygame.draw.rect(screen, black, [90,40,320,320], 18)
    pygame.draw.rect(screen, red, [82,32,10,10])
    pygame.draw.rect(screen, red, [82,359,10,10])
    pygame.draw.rect(screen, red, [409,32,10,10])
    pygame.draw.rect(screen, red, [409,359,10,10])



pygame.display.set_caption("Tictac Game")

screen.fill(white)

pygame.display.flip()
done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    draw_board()

    pygame.display.flip()
pygame.quit()
#sys.exit()
