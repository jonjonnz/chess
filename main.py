import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = self.create_board()
        self.pieces = {}
        self.piece_width = 0
        self.piece_height = 0
        self.coord_map = {}
        self.selected = []
        self.piece_to_move = None
        self.possible_moves = []
        self.attacked_pieces = []

    def create_board(self):
        board = {
            '8': {'a': Piece('r', 'b', '8-a'), 'b': Piece('n', 'b', '8-b'), 'c': Piece('b', 'b', '8-c'), 'd': Piece('q', 'b', '8-d'),
                  'e': Piece('k', 'b', '8-e'), 'f': Piece('b', 'b', '8-f'), 'g': Piece('n', 'b', '8-g'), 'h': Piece('r', 'b', '8-h'), },
            '7': {'a': Piece('p', 'b', '7-a'), 'b': Piece('p', 'b', '7-b'), 'c': Piece('p', 'b', '7-c'), 'd': Piece('p', 'b', '7-d'),
                  'e': Piece('p', 'b', '7-e'), 'f': Piece('p', 'b', '7-f'), 'g': Piece('p', 'b', '7-g'), 'h': Piece('p', 'b', '7-h'), },
            '6': {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, },
            '5': {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, },
            '4': {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, },
            '3': {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, },
            '2': {'a': Piece('P', 'w', '2-a'), 'b': Piece('P', 'w', '2-b'), 'c': Piece('P', 'w', '2-c'), 'd': Piece('P', 'w', '2-d'),
                  'e': Piece('P', 'w', '2-e'), 'f': Piece('P', 'w', '2-f'), 'g': Piece('P', 'w', '2-g'), 'h': Piece('P', 'w', '2-h'), },
            '1': {'a': Piece('R', 'w', '1-a'), 'b': Piece('N', 'w', '1-b'), 'c': Piece('B', 'w', '1-c'), 'd': Piece('Q', 'w', '1-d'),
                  'e': Piece('K', 'w', '1-e'), 'f': Piece('B', 'w', '1-f'), 'g': Piece('N', 'w', '1-g'), 'h': Piece('R', 'w', '1-h'), },

        }

        return board

    def reset_board(self):
        pass

    def display_board(self, screen):
        is_light = True
        x = y = 30
        self.pieces = {}
        for row, columns in self.board.items():
            for column, piece in columns.items():
                if (row, column) in self.selected:
                    pygame.draw.rect(screen, (150, 225, 225), (x + 1, y + 1, self.piece_width, self.piece_height))
                elif is_light:
                    pygame.draw.rect(screen, (225, 225, 225), (x + 1, y + 1, self.piece_width, self.piece_height))
                else:
                    pygame.draw.rect(screen, (100, 100, 100), (x + 1, y + 1, self.piece_width, self.piece_height))

                if piece is not None:
                    self.piece_width = piece.rect.width
                    self.piece_height = piece.rect.height
                    self.pieces[(row, column)] = piece
                    piece.current_coord = (x + 1, y + 1)
                    screen.blit(piece.image, (x + 1, y + 1, self.piece_width, self.piece_height))
                is_light = not is_light
                self.coord_map[(x + 1, y + 1)] = (row, column)
                x += self.piece_width + 1
            y += self.piece_height + 1
            is_light = not is_light
            x = 30

    def update_selected(self, pos):
        match_diff = [(pos[0] - x[0], pos[1] - x[1]) for x in self.coord_map.keys()]
        x_coord = sorted([x[0] for x in match_diff if x[0] >= 0 and x[1] >= 0])[0]
        y_coord = sorted([x[1] for x in match_diff if x[0] >= 0 and x[1] >= 0])[0]
        index = match_diff.index((x_coord, y_coord))
        selected = self.coord_map.get([x for x in self.coord_map.keys()][index])
        if selected in self.selected:
            self.selected = []
            self.piece_to_move = None
        else:
            self.selected = [selected]
            if self.piece_to_move:
                self.piece_to_move.move_piece(self.board, self.piece_to_move, selected)
                self.piece_to_move = None
                self.selected = []
            if self.selected and self.pieces.get(self.selected[0]):
                self.piece_to_move = self.pieces.get(selected)


class Piece:
    def __init__(self, name, color, start_pos):
        self.name = name
        self.color = color
        self.start_pos = start_pos
        self.current_pos = start_pos
        self.current_coord = ()
        self.legal_moves = []
        self.previous_positions = []
        self.image = self.load_image()
        self.rect = self.image.get_rect()
        self.can_castle = False
        self.en_passant = False
        self.is_pinned = False
        self.is_forked = False

    def load_image(self):
        name = self.name + '_' if self.name.isupper() else self.name
        image_path = f"imgs/pieces/{name}.png"
        image = pygame.image.load(image_path)

        return image

    def get_coord(self):
        return self.current_pos.split('-')

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

    def move_piece(self, board, piece_to_move, pos):
        board[pos[0]][pos[1]] = piece_to_move
        old_pos = piece_to_move.get_coord()
        board[old_pos[0]][old_pos[1]] = None
        piece_to_move.current_pos = "-".join(pos)


pygame.init()

# Set the dimensions of the display window
window_width, window_height = 800, 640

# Create the display surface
screen = pygame.display.set_mode((window_width, window_height))

running = True

new_board = Board(600, 600)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            btn = pygame.mouse
            new_board.update_selected(pos)

    # Clear the screen
    screen.fill((1, 100, 100))  # Fills the screen with white color

    # Draw the image on the screen
    new_board.display_board(screen)
    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
