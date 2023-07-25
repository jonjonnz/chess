import pygame


class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = {
            'a': {'1': Piece("R", "w", "a-1"), '2': Piece("P", "w", "a-2"), '3': None, '4': None, '5': None, '6': None, '7': Piece("p", "b", "a-7"),
                  '8': Piece("r", "b", "a-8"), },
            'b': {'1': Piece("N", "w", "b-1"), '2': Piece("P", "w", "b-2"), '3': None, '4': None, '5': None, '6': None, '7': Piece("p", "b", "b-7"),
                  '8': Piece("n", "b", "b-8"), },
            'c': {'1': Piece("B", "w", "c-1"), '2': Piece("P", "w", "c-2"), '3': None, '4': None, '5': None, '6': None, '7': Piece("p", "b", "c-7"),
                  '8': Piece("b", "b", "c-8"), },
            'd': {'1': Piece("Q", "w", "d-1"), '2': Piece("P", "w", "d-2"), '3': None, '4': None, '5': None, '6': None, '7': Piece("p", "b", "d-7"),
                  '8': Piece("q", "b", "d-8"), },
            'e': {'1': Piece("K", "w", "e-1"), '2': Piece("P", "w", "e-2"), '3': None, '4': None, '5': None, '6': None, '7': Piece("p", "b", "e-7"),
                  '8': Piece("k", "b", "e-8"), },
            'f': {'1': Piece("B", "w", "f-1"), '2': Piece("P", "w", "f-2"), '3': None, '4': None, '5': None, '6': None, '7': Piece("p", "b", "f-7"),
                  '8': Piece("b", "b", "f-8"), },
            'g': {'1': Piece("N", "w", "g-1"), '2': Piece("P", "w", "g-2"), '3': None, '4': None, '5': None, '6': None, '7': Piece("p", "b", "g-7"),
                  '8': Piece("n", "b", "g-8"), },
            'h': {'1': Piece("R", "w", "h-1"), '2': Piece("P", "w", "h-2"), '3': None, '4': None, '5': None, '6': None, '7': Piece("p", "b", "h-7"),
                  '8': Piece("r", "b", "h-8"), },

        }

        return board

    def reset_board(self):
        pass

    def display_board(self, screen):
        x = y = 0
        for rows, columns in self.board.items():
            for piece in columns.values():
                if piece is not None:
                    screen.blit(piece.image, (x, y))
                x += 50
            y += 50
            x = 0

class Piece:
    def __init__(self, name, color, start_pos):
        self.name = name
        self.color = color
        self.start_pos = start_pos
        self.current_pos = start_pos
        self.legal_moves = []
        self.previous_positions = []
        self.image = self.load_image()
        self.can_castle = False
        self.en_passant = False

    def load_image(self):
        name = self.name + '_' if self.name.isupper() else self.name
        image_path = f"imgs/pieces/{name}.png"
        image = pygame.image.load(image_path)

        return image

    def move_pawn(self):
        pass

    def move_king(self):
        pass

    def move_queen(self):
        pass

    def move_bishop(self):
        pass

    def move_rook(self):
        pass

    def move_knight(self):
        pass


pygame.init()

# Set the dimensions of the display window
window_width, window_height = 800, 600

# Create the display surface
screen = pygame.display.set_mode((window_width, window_height))

running = True

new_board = Board()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((1, 255, 255))  # Fills the screen with white color

    # Draw the image on the screen
    new_board.display_board(screen)
    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
