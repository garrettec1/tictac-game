foo = {'1': 'X', '2':' ', '3':'X', '4':' ', '5':'O'}

win = [('1','2','3')]

#I need to use elements in each tuple of win to call board info, to check.
#I need a nested looping structure that accesses the first element of win
#then accesses dic elements of foo to check for conditions.
#I need to keep the count of
'''
counter = 0

for tups in win:
    for keys in tups:
        if foo[keys] == 'X':
            counter += 1
        if foo[keys] == ' ':
            empty = keys
        if counter == 2:
            move = empty
print(move)
'''
'''
do = [1,2,3]
dict = {'a' : 1}


def test():
    do.pop()
    print(do)

def main():
    test()

def fix():
    do = [3,2,1]
    print(do)
    return do
main()
do = fix()
print(do)
'''

import pygame
pygame.init()
screen = pygame.display.set_mode((400,400))

white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
green = (0,225,0)
background = screen.fill(blue)
clock = pygame.time.Clock()

pygame.display.flip()
done = False
while not done:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    rec1 = pygame.Rect(50,50, 100,100)
    screen.blit(rec1)

    pygame.display.flip()

pygame.quit()
