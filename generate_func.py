
def build_board(lines):
    board = [['0' for count in range(lines)] for count in range(lines)]
    return board

# Ми пробували, але ми весь час вбили на те, щоби хоча б якось розібратися з гітом

def print_board(desk):
    for figure in desk:
        print(figure)

# В Каті так і не вдалося :(

def main():
    board = build_board(10)
    print_board(board)
    print('did something')
    return
main()

