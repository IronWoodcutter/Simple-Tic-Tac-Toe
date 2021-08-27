win_x = ()
win_o = ()
empty_ = ()
cells = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')


def board(cells):
    print('---------')
    print('|', cells[0], cells[1], cells[2], '|')
    print('|', cells[3], cells[4], cells[5], '|')
    print('|', cells[6], cells[7], cells[8], '|')
    print('---------')


def winx(pos):
    global win_x
    if pos[0] != '_' and pos[0] == pos[1] and pos[1] == pos[2] == 'X':
        win_x = True
    elif pos[3] != '_' and pos[3] == pos[4] and pos[4] == pos[5] == 'X':
        win_x = True
    elif pos[6] != '_' and pos[6] == pos[7] and pos[7] == pos[8] == 'X':
        win_x = True
    elif pos[0] != '_' and pos[0] == pos[3] and pos[3] == pos[6] == 'X':
        win_x = True
    elif pos[1] != '_' and pos[1] == pos[4] and pos[4] == pos[7] == 'X':
        win_x = True
    elif pos[2] != '_' and pos[2] == pos[5] and pos[5] == pos[8] == 'X':
        win_x = True
    elif pos[0] != '_' and pos[0] == pos[4] and pos[4] == pos[8] == 'X':
        win_x = True
    elif pos[2] != '_' and pos[2] == pos[4] and pos[4] == pos[6] == 'X':
        win_x = True
    else:
        win_x = False
    return win_x


def wino(pos):
    global win_o
    if pos[0] != '_' and pos[0] == pos[1] and pos[1] == pos[2] == 'O':
        win_o = True
    elif pos[3] != '_' and pos[3] == pos[4] and pos[4] == pos[5] == 'O':
        win_o = True
    elif pos[6] != '_' and pos[6] == pos[7] and pos[7] == pos[8] == 'O':
        win_o = True
    elif pos[0] != '_' and pos[0] == pos[3] and pos[3] == pos[6] == 'O':
        win_o = True
    elif pos[1] != '_' and pos[1] == pos[4] and pos[4] == pos[7] == 'O':
        win_o = True
    elif pos[2] != '_' and pos[2] == pos[5] and pos[5] == pos[8] == 'O':
        win_o = True
    elif pos[0] != '_' and pos[0] == pos[4] and pos[4] == pos[8] == 'O':
        win_o = True
    elif pos[2] != '_' and pos[2] == pos[4] and pos[4] == pos[6] == 'O':
        win_o = True
    else:
        win_o = False
    return win_o


def moveх():
    global cells
    while True:
        row, column = input('Enter the coordinates: ').split()
        coordinates = ''.join(row + column)
        if coordinates.isdigit() == False:
            print('You should enter numbers!')
        elif int(row) not in range(1, 4) or int(column) not in range(1, 4):
            print('Coordinates should be from 1 to 3! ')
        elif cells[((int(row) - 1) * 3) + (int(column) + 2) - 3] != ' ':
            index = ((int(row) - 1) * 3) + (int(column) + 2) - 3
            print('This cell is occupied! Choose another one!')
            print(index)
        else:
            index = ((int(row) - 1) * 3) + (int(column) + 2) - 3
            cells = list(cells)
            cells[index] = 'X'
            cells = "".join(cells)
            board(cells)
            break


def moveo():
    global cells
    while True:
        row, column = input('Enter the coordinates: ').split()
        coordinates = ''.join(row + column)
        if coordinates.isdigit() == False:
            print('You should enter numbers!')
        elif int(row) not in range(1, 4) or int(column) not in range(1, 4):
            print('Coordinates should be from 1 to 3! ')
        elif cells[((int(row) - 1) * 3) + (int(column) + 2) - 3] != ' ':
            index = ((int(row) - 1) * 3) + (int(column) + 2) - 3
            print('This cell is occupied! Choose another one!')
            print(index)
        else:
            index = ((int(row) - 1) * 3) + (int(column) + 2) - 3
            cells = list(cells)
            cells[index] = 'O'
            cells = "".join(cells)
            board(cells)
            break


def empty(pos):
    global empty_
    empty_ = pos.count(' ')
    return empty_


board(cells)
while True:

    moveх()
    winx(cells)
    if win_x is True:
        print('X wins')
        break
    empty(cells)
    if empty_ == 0:
        print('Draw')
        break
    moveo()
    wino(cells)
    if win_o is True:
        print('O wins')
        break
    empty(cells)
    if empty_ == 0:
        print('Draw')
        break