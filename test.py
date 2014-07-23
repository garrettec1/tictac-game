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
...
