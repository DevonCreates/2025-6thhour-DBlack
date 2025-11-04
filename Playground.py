
import curses
import random
import time

# Define the shapes (rotations)
SHAPES = [
    [[1, 1, 1, 1]],                          # I
    [[1, 1], [1, 1]],                        # O
    [[0, 1, 0], [1, 1, 1]],                  # T
    [[1, 0, 0], [1, 1, 1]],                  # J
    [[0, 0, 1], [1, 1, 1]],                  # L
    [[1, 1, 0], [0, 1, 1]],                  # S
    [[0, 1, 1], [1, 1, 0]]                   # Z
]

# Dimensions
HEIGHT = 20
WIDTH = 10

# Initialize new piece
def new_piece():
    shape = random.choice(SHAPES)
    return {'shape': shape, 'x': WIDTH // 2 - len(shape[0]) // 2, 'y': 0}

# Check if the piece fits
def valid_position(board, piece, adj_x=0, adj_y=0):
    shape = piece['shape']
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = piece['x'] + x + adj_x
                new_y = piece['y'] + y + adj_y
                if new_x < 0 or new_x >= WIDTH or new_y >= HEIGHT:
                    return False
                if new_y >= 0 and board[new_y][new_x]:
                    return False
    return True

# Add piece to the board
def merge_piece(board, piece):
    shape = piece['shape']
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                board[piece['y'] + y][piece['x'] + x] = 1

# Clear full lines
def clear_lines(board):
    new_board = [row for row in board if any(v == 0 for v in row)]
    lines_cleared = HEIGHT - len(new_board)
    for _ in range(lines_cleared):
        new_board.insert(0, [0 for _ in range(WIDTH)])
    return new_board, lines_cleared

# Rotate a piece
def rotate(piece):
    shape = piece['shape']
    rotated = [list(row) for row in zip(*shape[::-1])]
    return {'shape': rotated, 'x': piece['x'], 'y': piece['y']}

# Draw board and piece
def draw_board(stdscr, board, piece, score):
    stdscr.clear()
    # Draw borders
    for y in range(HEIGHT):
        stdscr.addstr(y, 0, '|')
        stdscr.addstr(y, WIDTH * 2 + 1, '|')
    stdscr.addstr(HEIGHT, 0, '+' + '-' * (WIDTH * 2) + '+')

    # Draw board
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell:
                stdscr.addstr(y, x * 2 + 1, "██")

    # Draw piece
    for y, row in enumerate(piece['shape']):
        for x, cell in enumerate(row):
            if cell:
                if 0 <= piece['y'] + y < HEIGHT and 0 <= piece['x'] + x < WIDTH:
                    stdscr.addstr(piece['y'] + y, (piece['x'] + x) * 2 + 1, "██")

    stdscr.addstr(1, WIDTH * 2 + 5, f"Score: {score}")
    stdscr.refresh()

# Main game loop
def tetris(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(150)  # Game speed

    board = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    current_piece = new_piece()
    next_fall = time.time() + 0.5
    score = 0

    while True:
        draw_board(stdscr, board, current_piece, score)

        # Input
        try:
            key = stdscr.getch()
        except:
            key = -1

        if key == ord('q'):
            break
        elif key == curses.KEY_LEFT and valid_position(board, current_piece, adj_x=-1):
            current_piece['x'] -= 1
        elif key == curses.KEY_RIGHT and valid_position(board, current_piece, adj_x=1):
            current_piece['x'] += 1
        elif key == curses.KEY_DOWN and valid_position(board, current_piece, adj_y=1):
            current_piece['y'] += 1
        elif key == curses.KEY_UP:
            rotated_piece = rotate(current_piece)
            if valid_position(board, rotated_piece):
                current_piece = rotated_piece

        # Gravity
        if time.time() > next_fall:
            next_fall = time.time() + 0.5
            if valid_position(board, current_piece, adj_y=1):
                current_piece['y'] += 1
            else:
                merge_piece(board, current_piece)
                board, cleared = clear_lines(board)
                score += cleared * 100
                current_piece = new_piece()
                if not valid_position(board, current_piece):
                    # Game over
                    stdscr.clear()
                    stdscr.addstr(HEIGHT // 2, WIDTH - 4, "GAME OVER")
                    stdscr.addstr(HEIGHT // 2 + 2, WIDTH - 6, f"Score: {score}")
                    stdscr.refresh()
                    stdscr.nodelay(False)
                    stdscr.getch()
                    break

if __name__ == "__main__":
    curses.wrapper(tetris)
