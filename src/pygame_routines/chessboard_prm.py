import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the chessboard
WIDTH, HEIGHT = 800, 800

# Set the dimensions of each square
SQUARE_SIZE = WIDTH // 8

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chessboard")


class Square:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.color = BLACK
        self.parameter = 0

    def set_parameter(self, value):
        self.parameter = value

    def draw(self):
        square_rect = pygame.Rect(self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(screen, self.color, square_rect)

        # Add text on the square
        font = pygame.font.Font(None, 20)
        text = font.render(f"Prm: {self.parameter}", True, RED)
        text_rect = text.get_rect(center=square_rect.center)
        screen.blit(text, text_rect)


# Create a two-dimensional list to represent the chessboard
chessboard = [[Square(row, col) for col in range(8)] for row in range(8)]

# Variable to keep track of the currently selected square
selected_square = None

# Variable to store the parameter input
parameter_input = ""

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

            # Check if the click is inside the chessboard
            if 0 <= row < 8 and 0 <= col < 8:
                square = chessboard[row][col]

                # Check if the square is selected
                if selected_square == square:
                    selected_square = None
                else:
                    selected_square = square

            # Check if the click is on the parameter input button
            parameter_button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 40, 100, 30)
            if parameter_button_rect.collidepoint(x, y):
                if selected_square is not None:
                    try:
                        parameter_value = int(parameter_input)
                        selected_square.set_parameter(parameter_value)
                    except ValueError:
                        pass
                parameter_input = ""

        elif event.type == pygame.KEYDOWN:
            # Handle key press events
            if selected_square is not None:
                if event.key == pygame.K_BACKSPACE:
                    parameter_input = parameter_input[:-1]
                elif event.key == pygame.K_RETURN:
                    try:
                        parameter_value = int(parameter_input)
                        selected_square.set_parameter(parameter_value)
                        parameter_input = ""
                    except ValueError:
                        parameter_input = ""
                else:
                    parameter_input += event.unicode

    # Clear the screen
    screen.fill(GRAY)

    # Draw the chessboard
    for row in range(8):
        for col in range(8):
            square = chessboard[row][col]
            square.draw()

            # # Highlight the selected square
            # if selected_square == square:
            #     pygame.draw.rect(screen, GREEN, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 4)

    # Draw the parameter input button
    parameter_button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 40, 100, 30)
    pygame.draw.rect(screen, WHITE, parameter_button_rect)
    font = pygame.font.Font(None, 20)
    button_text = font.render("Set Prm", True, BLACK)
    button_text_rect = button_text.get_rect(center=parameter_button_rect.center)
    screen.blit(button_text, button_text_rect)

    # Draw the parameter input text
    input_rect = pygame.Rect(WIDTH // 2 - 40, HEIGHT - 70, 80, 30)
    pygame.draw.rect(screen, WHITE, input_rect)
    font = pygame.font.Font(None, 20)
    input_text = font.render(parameter_input, True, BLACK)
    input_text_rect = input_text.get_rect(center=input_rect.center)
    screen.blit(input_text, input_text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

