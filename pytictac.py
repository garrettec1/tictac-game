import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
green = (0,225,0)

size = (400,400)

screen = pygame.display.set_mode(size,pygame.RESIZABLE)

def calc_lines(size):
    """Calculates the whitespace in pixels before the gridlines are drawn if
    the window is redrawn. Current implementation is just a rough mock up of
    functionality.
    """

    hieght = size[1]
    width = size[0]
    box_size_down = int(hieght/3)
    box_size_right = int(width/3)

    down1 = ((1, box_size_down),(width, box_size_down))
    down2 = ((1, box_size_down*2), (width, box_size_down*2))
    right1 = ((box_size_right, 1), (box_size_right, hieght))
    right2 = ((box_size_right*2, 1), (box_size_right*2, hieght))

    lines = [down1,down2,right1,right2]
    return (lines)

def find_board_location(lines,mouse_location):
    """This function finds the location of the mouse click by comparing the
    click position with the lines returned from calc_lines. So lines[0]
    indicates down1, and lines[0][1][1] returns the second y variable where the
    line is drawn. I found the y first because the format of the tictac_game
    takes locations like '1a'.
    """
    if mouse_location[1] < lines[0][1][1]:
        spot = '1'
    elif mouse_location[1] < lines[1][1][1]:
        spot = '2'
    else:
        spot = '3'
    if mouse_location[0] < lines[2][0][0]:
        spot = spot + 'a'
    elif mouse_location[0] < lines[3][0][0]:
        spot = spot + 'b'
    else:
        spot = spot + 'c'

    return(spot)

def draw_board(size):

    lines = calc_lines(size)
    for position in lines:
        pygame.draw.line(screen, blue, position[0], position[1], 20)

    return(lines)

pygame.display.set_caption("Tictac Game")

background = screen.fill(white)
clock = pygame.time.Clock()

background
lines = draw_board(size)

pygame.display.flip()
done = False
while not done:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.VIDEORESIZE:
            size = (event.w, event.h)
            screen = pygame.display.set_mode(size,pygame.RESIZABLE)
            screen.fill(white)
            lines = draw_board(size)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_location = event.pos
            spot = find_board_location(lines,mouse_location)
    pygame.display.flip()

    '''mouse = pygame.mouse.get_pos()
    box = pygame.Surface((100,100))
    box.set_alpha(10)
    box.fill(green)
    screen.blit(box,mouse)'''

    pygame.display.flip()


pygame.quit()

#sys.exit()
