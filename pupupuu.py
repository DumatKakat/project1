def format_board(board):
    joined_rows = [" "]
    cifra = list(range(1, len(board)+1, 1))
    cifra = [str(x) for x in cifra]
    joined_rows.append("".join(cifra))
    for row in board:
        joined_rows.append("|".join(row))
    print(joined_rows)
    return f"\n".join(joined_rows)

format_board([
        ['X', 'O', 'X'],
        ['O', ' ', ' '],
        [' ', 'X', 'O']
    ])
