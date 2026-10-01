def diagonal_winner(board):
    flag = False
    diaga1 = board[0][0]
    diaga2 = board[len(board)-1][0]
    for k in range(len(board), 0, -1):
        if (diaga1 == ' ' and board[-k][-k] == ' ') or\
            (diaga2 == ' ' and board[k-1][-k] == ' '):
            flag = False
        elif (diaga1 != board[-k][-k]) and\
            (diaga2 != board[k-1][-k]):
            flag = False
        else:
            flag = True
    return flag

print(diagonal_winner(
        [
            ['O', 'X', 'O', 'X'],
            [' ', 'O', 'X', ' '],
            ['X', 'X', ' ', 'X'],
            ['X', ' ', 'O', 'O']
        ]))
print(diagonal_winner(
        [   ['S', 'M', ' ', 'M'],
            ['S', 'S', 'S', ' '],
            ['S', 'S', 'S', 'S'],
            [' ', 'M', ' ', 'S']
        ]
))



