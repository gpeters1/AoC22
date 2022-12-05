test_board = [i.replace("[","").replace("]", "").replace("   ", " ").replace("  ", "0").replace("\n", "").replace(" ", "") for i in open("test_board.input")]
test_moves = [i.replace("\n", "") for i in open("test_moves.input")]

day_board = [i.replace("[","").replace("]", "").replace("   ", " ").replace("  ", "0").replace("\n", "").replace(" ", "") for i in open("day_board.input")]
day_moves = [i.replace("\n", "") for i in open("day_moves.input")]


def generate_moves(test_moves):
    moves = []
    for test_move in test_moves:
        print(test_move)
        move, moves_to_from =(test_move.split(" from "))
        moves_from, moves_to = moves_to_from.split(" to ")
        move_word, move_to_make = move.split("move ")
        moves.append([move_to_make, moves_from, moves_to])
    return moves


def create_crates(crates):
    zip_board = zip(*crates)
    board = []
    for column in zip_board:
        new_column = [item for item in column if item != "0"]
        board.append(new_column)
    return board

def minus_1(moves):
    moves_array = []
    for i in moves:
        moves_row = []
        for j in i:
            moves_row.append(int(j)-1)
        moves_array.append(moves_row)
    return moves_array


def update_board(board, moves_to_make, move_from, move_to):
    print(board)
    while moves_to_make > 0:
        crane_item = board[move_from].pop(0)
        board[move_to].insert(0, crane_item)
        moves_to_make -= 1
    return board

        
def get_answer(board):
    answer = ""
    for i in board:
        answer = answer + i.pop(0)
    return answer

def make_moves(board, moves):
    for move in range(0, len(moves)):
        for part in range(0, len(moves[move])):
            if part == 0:
                move_to_make = moves[move][part] + 1
                print(f"Move: {move_to_make}")
            if part == 1:
                move_from = moves[move][part]
                print(f"Move from: {move_from}")
            if part == 2:
                move_to = moves[move][part]
                print(f"Move to: {move_to}")
        new_board = update_board(board, move_to_make, move_from, move_to)
    answer = get_answer(new_board)
    return answer


board = create_crates(day_board)
test = generate_moves(day_moves)
moves = minus_1(test)
answer = make_moves(board, moves)
print(answer)
