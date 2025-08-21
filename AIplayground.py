import os
import random

# --- Game Constants ---
MAZE_WIDTH = 25
MAZE_HEIGHT = 15
PLAYER_ICON = '🏃'
CHASER_ICON = '🤖'
WALL_ICON = '█'
PATH_ICON = ' '
GEM_ICON = '💎'
EXIT_ICON = '🚪'


class MazeGame:
    """
    A class to manage the text-based maze game logic.
    """

    def __init__(self):
        self.maze = []
        self.player_pos = {'x': 0, 'y': 0}
        self.chaser_pos = {'x': 0, 'y': 0}
        self.exit_pos = {'x': 0, 'y': 0}
        self.gems = []
        self.score = 0
        self.is_game_over = False

    def generate_maze(self):
        """
        Generates a new maze using a simple recursive backtracking algorithm.
        """
        grid = [[WALL_ICON for _ in range(MAZE_WIDTH)] for _ in range(MAZE_HEIGHT)]
        stack = []

        # Start at a random odd-numbered coordinate
        start_x, start_y = (random.randint(0, MAZE_WIDTH // 2) * 2 + 1,
                            random.randint(0, MAZE_HEIGHT // 2) * 2 + 1)
        stack.append((start_x, start_y))
        grid[start_y][start_x] = PATH_ICON

        while stack:
            x, y = stack[-1]

            # Find unvisited neighbors (2 steps away)
            neighbors = []
            if y > 1 and grid[y - 2][x] == WALL_ICON:
                neighbors.append((x, y - 2))
            if y < MAZE_HEIGHT - 2 and grid[y + 2][x] == WALL_ICON:
                neighbors.append((x, y + 2))
            if x > 1 and grid[y][x - 2] == WALL_ICON:
                neighbors.append((x - 2, y))
            if x < MAZE_WIDTH - 2 and grid[y][x + 2] == WALL_ICON:
                neighbors.append((x + 2, y))

            if neighbors:
                nx, ny = random.choice(neighbors)
                # Carve a path to the neighbor
                grid[y + (ny - y) // 2][x + (nx - x) // 2] = PATH_ICON
                grid[ny][nx] = PATH_ICON
                stack.append((nx, ny))
            else:
                stack.pop()

        self.maze = grid

        # Find valid positions for player, chaser, gems, and exit
        valid_positions = []
        for y in range(MAZE_HEIGHT):
            for x in range(MAZE_WIDTH):
                if self.maze[y][x] == PATH_ICON:
                    valid_positions.append({'x': x, 'y': y})

        # Shuffle and assign positions
        random.shuffle(valid_positions)
        self.player_pos = valid_positions.pop()
        self.chaser_pos = valid_positions.pop()
        self.exit_pos = valid_positions.pop()

        # Place gems randomly
        self.gems = []
        for _ in range(5):
            if valid_positions:
                self.gems.append(valid_positions.pop())

    def draw_maze(self):
        """
        Renders the current state of the maze to the console.
        """
        # Clear the console for a clean view
        os.system('cls' if os.name == 'nt' else 'clear')

        # Create a copy of the maze to draw on
        display_maze = [row[:] for row in self.maze]

        # Place game elements
        display_maze[self.exit_pos['y']][self.exit_pos['x']] = EXIT_ICON
        for gem in self.gems:
            display_maze[gem['y']][gem['x']] = GEM_ICON
        display_maze[self.player_pos['y']][self.player_pos['x']] = PLAYER_ICON
        display_maze[self.chaser_pos['y']][self.chaser_pos['x']] = CHASER_ICON

        # Print the maze and info
        for row in display_maze:
            print("".join(row))
        print(f"Score: {self.score}")
        print("Use WASD or arrow keys to move. Collect gems and find the exit!")

    def move_player(self, direction):
        """
        Handles player movement and checks for collisions and collectibles.
        """
        new_pos = self.player_pos.copy()
        if direction == 'w' or direction == 'up':
            new_pos['y'] -= 1
        elif direction == 's' or direction == 'down':
            new_pos['y'] += 1
        elif direction == 'a' or direction == 'left':
            new_pos['x'] -= 1
        elif direction == 'd' or direction == 'right':
            new_pos['x'] += 1

        # Check if the new position is a valid path
        if self.maze[new_pos['y']][new_pos['x']] == PATH_ICON:
            self.player_pos = new_pos
            self.check_gems()

    def move_chaser(self):
        """
        Simple chaser AI: it moves one step closer to the player.
        """
        chaser_x, chaser_y = self.chaser_pos['x'], self.chaser_pos['y']
        player_x, player_y = self.player_pos['x'], self.player_pos['y']

        # Determine the best move based on distance to the player
        dx = player_x - chaser_x
        dy = player_y - chaser_y

        move_x, move_y = 0, 0

        # Prioritize the larger movement
        if abs(dx) > abs(dy):
            if dx > 0:
                move_x = 1
            elif dx < 0:
                move_x = -1
        else:
            if dy > 0:
                move_y = 1
            elif dy < 0:
                move_y = -1

        # Check for collision with walls and adjust movement
        if self.maze[chaser_y + move_y][chaser_x + move_x] == PATH_ICON:
            self.chaser_pos['x'] += move_x
            self.chaser_pos['y'] += move_y
        else:
            # If the primary direction is blocked, try the other direction
            move_x, move_y = 0, 0
            if abs(dx) <= abs(dy):
                if dx > 0:
                    move_x = 1
                elif dx < 0:
                    move_x = -1
            else:
                if dy > 0:
                    move_y = 1
                elif dy < 0:
                    move_y = -1
            if self.maze[chaser_y + move_y][chaser_x + move_x] == PATH_ICON:
                self.chaser_pos['x'] += move_x
                self.chaser_pos['y'] += move_y

    def check_gems(self):
        """
        Checks if the player has collected a gem.
        """
        for i, gem in enumerate(self.gems):
            if self.player_pos['x'] == gem['x'] and self.player_pos['y'] == gem['y']:
                self.gems.pop(i)
                self.score += 10
                break

    def check_game_state(self):
        """
        Checks for win or lose conditions.
        """
        # Lose condition: Chaser catches the player
        if self.player_pos['x'] == self.chaser_pos['x'] and self.player_pos['y'] == self.chaser_pos['y']:
            self.is_game_over = True
            print("Game Over! The chaser caught you.")

        # Win condition: Player reaches the exit
        if self.player_pos['x'] == self.exit_pos['x'] and self.player_pos['y'] == self.exit_pos['y']:
            self.is_game_over = True
            print("You Win! You found the exit.")
            print(f"Final Score: {self.score}")

    def run(self):
        """
        Main game loop.
        """
        self.generate_maze()
        while not self.is_game_over:
            self.draw_maze()

            try:
                # Get a single character for input
                import sys, tty, termios
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                try:
                    tty.setraw(sys.stdin.fileno())
                    ch = sys.stdin.read(1)
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

                direction = ch.lower()

                if direction in ['w', 'a', 's', 'd']:
                    self.move_player(direction)
                    self.move_chaser()
                elif direction == 'q':
                    self.is_game_over = True

                self.check_game_state()
            except ImportError:
                # Fallback for systems that don't support tty (like some online interpreters)
                direction = input("Enter a move (W/A/S/D): ").lower()
                self.move_player(direction)
                self.move_chaser()
                self.check_game_state()

        print("\nThanks for playing!")


if __name__ == "__main__":
    game = MazeGame()
    game.run()