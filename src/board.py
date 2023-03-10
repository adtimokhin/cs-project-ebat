from game_piece import GamePiece


class Board:
    """
    A class that represents the board of the game.

    Attributes:
    - number_of_rows : The number of rows of the board.
    - number_of_cols : The number of columns of the board.
    - grid : The grid of the board. It stores the game pieces.
    """
    def __init__(self, number_of_rows, number_of_cols):
        self.number_of_rows = number_of_rows
        self.number_of_cols = number_of_cols
        self.grid = []
        # Populate the board with empty spaces
        for i in range(number_of_rows):
            line = []
            for j in range(number_of_cols):
                line.append(None)
            self.grid.append(line)

    def move_piece(self, initial_pos: tuple, final_pos: tuple, game):
        """
        Moves a piece from initial position to final position

        Input:
            initial_pos: tuple(int,int) - initial position of the piece (row, col)

            final_pos: tuple(int,int) - final position of the piece (row, col)

            game: Game - the game object
        
        :raises: Exception if the piece cannot be moved
        """

        if self.grid[initial_pos[0]][initial_pos[1]] is None:
            raise Exception("There is no piece at the initial position")
        
        if self.grid[final_pos[0]][final_pos[1]] is not None:
            raise Exception("There is piece at the final position")

        self.grid[initial_pos[0]][initial_pos[1]].position = final_pos
        self.grid[final_pos[0]][final_pos[1]] = self.grid[initial_pos[0]][initial_pos[1]]
        self.grid[initial_pos[0]][initial_pos[1]] = None
        
        if abs(initial_pos[0] - final_pos[0]) == 2:
            row_to_remove = (initial_pos[0] + final_pos[0]) // 2
            column_to_remove = (initial_pos[1] + final_pos[1]) // 2
            self.remove_piece(self.grid[row_to_remove][column_to_remove], game)
        if final_pos[0] == 0 or final_pos[0] == self.number_of_rows -1:
            self.grid[final_pos[0]][final_pos[1]].transform()

    def place_piece(self, piece):
        """
        Places a piece on the board.

        Input:
            piece: (GamePiece) - the piece to be placed on the board
        
        :raises: Exception if the piece cannot be placed
        """

        if self.grid[piece.position[0]][piece.position[1]] is not None:
            raise Exception("There is already a piece at that position")
        
        self.grid[piece.position[0]][piece.position[1]] = piece

    def is_on_grid(self, position):
        """
        Checks if the coordinates given are correspondive to an unoccupied cell on the grid
        If the coordinates are out of bound, then False is returned.

        Input:
            pos - (int, int) is a position coordinates of the cell. Given as (row, col)
        
        Output:
            True - if the cell is in range of board
            False - otherwise
        """
        row_pos = position[0]
        col_pos = position[1]

        # Checking if the cell is out of bound
        if not (0 <= row_pos < len(self.grid)):
            return False
        if not (0 <= col_pos < len(self.grid[0])):
            return False

        return True

    def is_empty_cell(self, pos):
        """
        Checks if the coordinates given are correspondive to an unoccupied cell on the grid
        If the coordinates are out of bound, then False is returned.

        Input:
            pos - (int, int) is a position coordinates of the cell. Given as (row, col)
        
        Output:
            True - if the cell is in range of board and also is not occupied
            False - otherwise
        """

        if not self.is_on_grid(pos):
            return False

        row_pos = pos[0]
        col_pos = pos[1]

        # Checking if the cell is occupied or not
        return self.grid[row_pos][col_pos] is None

    def remove_piece(self, piece, game):
        """
        Removes a piece from the board.

        Input:
            piece: (GamePiece) - the piece to be removed from the board

            game: Game - the game object, so that the piece can be removed from the piece_dict
        
        :raises: Exception if the piece cannot be removed
        """
        game.pieces_dict[piece.player].remove(piece)
        if self.grid[piece.position[0]][piece.position[1]] is None:
            raise Exception("There is no piece at that position")


        self.grid[piece.position[0]][piece.position[1]] = None
