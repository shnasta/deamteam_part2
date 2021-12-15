def generate_field():
    print("I try my best")
def build_board(dims):
    return [['O' for count in range(dims)] for count in range(dims)]
def print_board(board):
    for b in board:
        print(*b)
def main():
    board = build_board(5)
    print_board(board)
    print('did something')
    return
main()