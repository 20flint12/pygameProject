import pygame
from pygame import gfxdraw
import time

# Initialize Pygame
pygame.init()

# Set the dimensions of the chessboard
WIDTH, HEIGHT = 800, 800

# Set the dimensions of each square
SQUARE_AMOUNT = 12
SQUARE_SIZE = WIDTH // SQUARE_AMOUNT

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Evolution game")


class Square:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.clicks = 0
        self.start_time = None

    def toggle_color(self):
        self.clicks += 1
        if self.start_time is None:
            self.start_time = time.time()

    def get_color(self):
        brightness = min(self.clicks * 5, 255)
        return (brightness, brightness, brightness)

    def draw(self):
        square_rect = pygame.Rect(self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(screen, self.get_color(), square_rect)

        # Add text on the square
        font = pygame.font.Font(None, 20)
        text = font.render(f"{self.row},{self.col}", True, RED)
        text_rect = text.get_rect(center=square_rect.center)
        screen.blit(text, text_rect)

        # Add click counter on the square
        counter_text = font.render(str(self.clicks), True, GREEN)
        counter_rect = counter_text.get_rect(center=(square_rect.centerx, square_rect.centery + SQUARE_SIZE // 4))
        screen.blit(counter_text, counter_rect)

        # Add timer label on the square
        if self.start_time is not None:
            elapsed_time = int(time.time() - self.start_time)
            timer_text = font.render(str(elapsed_time), True, BLUE)
            timer_rect = timer_text.get_rect(center=(square_rect.centerx, square_rect.centery - SQUARE_SIZE // 4))
            screen.blit(timer_text, timer_rect)


# Create a two-dimensional list to represent the chessboard
chessboard = [[Square(row, col) for col in range(SQUARE_AMOUNT)] for row in range(SQUARE_AMOUNT)]

# Variable to keep track of the currently selected square
selected_square = None

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            x, y = pygame.mouse.get_pos()

            # Determine the row and column of the clicked square
            row = y // SQUARE_SIZE
            col = x // SQUARE_SIZE

            # Toggle the color of the selected square
            square = chessboard[row][col]
            square.toggle_color()

    # Draw the chessboard
    for row in range(SQUARE_AMOUNT):
        for col in range(SQUARE_AMOUNT):
            chessboard[row][col].draw()

    # Highlight the selected square
    if selected_square is not None:
        row, col = selected_square
        pygame.draw.rect(screen, GREEN, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 4)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
