"""
This is where we put all of our documentation 
"""

"""
Example calls:
>>> game = Game(players, number_populated_rows=2, width=8)
>>> game.get_possible_moves_for_piece(game.pieces_dict[player_1])
>>> game.get_possible_jumps_for_piece(selected_piece)
>>> game.get_all_jumps_moves(selected_piece.position, selected_piece)
>>> game.get_possible_moves(current_player)
>>> game.make_move(game.get_possible_jumps_for_piece(selected_piece)[0])
>>> board.move_piece((0,1), (1,0), game)
>>> board.place_piece(GamePiece(...))
>>> board.is_on_grid((9,3))
>>> board.is_empty_cell((9,3))
>>> board.remove_piece(GamePiece(...))
>>> gamepiece.transform()
>>> checkers_bot.choose_move(board, game.get_all_jumps_moves(selected_piece.position, selected_piece))
>>> checkers_bot.aggressive_moves(self, valid_moves, board)
>>> TUI.print_board(game)
>>> TUI.get_bool_input("Do you want to surrender?", true_ans=["y", "sure", "yes"], false_ans=["n", "no", "nope"]):
>>> TUIGame.play_game()
>>> draw_board(game, WINDOW)
>>> play_checkers(game)
>>> get_piece(board, (9,5))
"""

class Game:
    """
    This class represents a collection of functionality
    responsible for the game logic. This class also stores board.

    Public attributes of this class:
    - players: list of players playing the game.

    - number_populated_rows: number of rows in the board that have been
                        populated with game pieces of a single player.
    
    - width: width of the board

    - board: Board object created from the input data.
    
    - pieces_dict: dictionary of game pieces.
    """

    def __init__(self, players, number_populated_rows, width=8):
        raise NotImplementedError

    def get_possible_moves_for_piece(self, piece):
        """
        finds possible moves for a given piece
        :param piece
            the specific game piece for which the moves are found
        :returns
            either list[(int,int)] which is a list of tuples of coordinates, representing moves,
            or None
        """
        raise NotImplementedError

    def get_possible_jumps_for_piece(self, piece):
        """
        finds possible jumps for a given piece and formats them accordingly with the design 
        :param piece
            the specific game piece for which the jumps are found
        :returns
            list[GamePiece, list[tuple(int,int)]] which is a list of tuples of coordinates, representing jumps,
        """
        raise NotImplementedError

    def get_all_jumps_moves (self, start_pos, piece, blocked_pos=[]):
        """
        finds all possible jumps for a given piece
        :param start_pos
            the starting position of the piece
        :param piece
            the specific game piece for which the jumps are found
        :param blocked_pos
            a list of coordinates which the piece cannot jump over.
        :returns
            list[tuple(int,int), list[(),...]] which is a list of tuples of coordinates, representing jumps,
        """
        raise NotImplementedError

    def get_possible_moves(self, player):
        """
        finds possible moves for a given player
        :param player
            Player for whom possible moves are found
        :returns
            list[(piece, [(int, int)])] - list of tuples that show a piece and a possible move coordinate
            if jumps are possible returns only jump-moves
        """
        raise NotImplementedError

    def get_all_jumps(self, player):
        """
        finds all possible jump-moves for a given player
        :param player
            Player for whom possible jumps are found
        :returns
            list[(piece, (int, int))] - list of all possible jump moves
            or None if no 'jump-moves' are found

        """
        raise NotImplementedError
    
    def __populate_board(self):
        """
        Populates the board with Game_Pieces accroding to the rules of checkers.
        """
        raise NotImplementedError

    def make_move(self, move):
        """
        Moves a Game_Piece from initial position to final position on the grid
        removes a Piece from the board if the 'jump-move' was performed
        :param initial_pos:
            (int, int) - represents the coordinates of the piece as (row, col)
        :param final_pos:
            (int, int) - represents the coordinates of the piece as (row, col)
        :returns
            None
        """
        raise NotImplementedError

class Board:
    """
    A class that represents the board of the game.

    Attributes:
    - number_of_rows : The number of rows of the board.
    - number_of_cols : The number of columns of the board.
    - grid : The grid of the board. It stores the game pieces.
    """
     def __init__(self, number_of_rows, number_of_cols):
        raise NotImplementedError

     def move_piece(self, initial_pos: tuple, final_pos: tuple, game):
        """
        Moves a piece from initial position to final position

        Input:
            initial_pos: tuple(int,int) - initial position of the piece (row, col)

            final_pos: tuple(int,int) - final position of the piece (row, col)

            game: Game - the game object
        
        :raises: Exception if the piece cannot be moved
        """

        raise NotImplementedError

     def place_piece(self, piece):
        """
        Places a piece on the board.

        Input:
            piece: (GamePiece) - the piece to be placed on the board
        
        :raises: Exception if the piece cannot be placed
        """

        raise NotImplementedError

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
        raise NotImplementedError

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

        raise NotImplementedError

     def remove_piece(self, piece, game):
        """
        Removes a piece from the board.

        Input:
            piece: (GamePiece) - the piece to be removed from the board

            game: Game - the game object, so that the piece can be removed from the piece_dict
        
        :raises: Exception if the piece cannot be removed
        """
        raise NotImplementedError

class GamePiece: 
    """
    Public attributes of this class:
        - position: tuple(row, column) that represents the position of the game piece.
        - player  : Owner of the piece
        - is_king : whether the piece is a king or not.
    This class is representing a game piece (checker) with its position, 
    player it belongs to and whether the game piece is a king.
    """
    def __init__(self, position, player):
        raise NotImplementedError

    def transform(self):
        """
        Transforms a game piece into a king 
        :param None
            only self
        :returns
            None
        """
        raise NotImplementedError

class Player:

    """
    This is a class representing a player of the game.
    
    Public attributes:
        - name (str) - name of the player
        - color (str) - color of the player's pieces
    """
    
    def __init__(self, name: str, color: str):
        """
        Creates a Player insrtance with a given name
        :param name:
            (str) - name of the player
        :param color:
            (str) - color of the player
        """
        raise NotImplementedError
    
class CheckersBot(Player):
    """
    CheckersBot is a child class of Player which with the simple heuristics suggests a move
    Public attributes:
        name: str  - name of the player, continuation of player interface
    Heuristics:
    1. Try to king with every possible opportunity
    2. Try to move so that the piece is not attacked
    3. Chose the longest jumps
    4. Move aggressively (closer to the enemy pieces but not such that they are attacked
    5. Don't move two back(flank) pieces if possible
    """
    def __init__(self, name: str, color: str):
        raise NotImplementedError

    def choose_move(self, board: Board, possible_moves: list):
        """
        chooses the best possible move
        :param: board Board class instance: current game_board
        :param: possible_moves list of moves
        :return: tuple(GamePiece, [tuple(int, int)]):  a move in a move format specified in the design
        """

        raise NotImplementedError

    def aggressive_moves(self, valid_moves: list, board: Board):
        """
        picks the most aggressive move, by choosing the move which minimizes distance to all of the enemy pieces
        :param: valid_moves: all of the moves that are accessible to the given bot
        :param: board: Board class instance: current game_board
        :return: list(moves): list of moves which are the best by given metric
        """

        raise NotImplementedError

    def check_if_back_pieces(self, valid_moves: list, row_num: int):
        """
        removes defensive pieces from the valid moves
        :param: valid_moves: list of valid moves
        :param: row_num: int: length of the vertical side of the board
        :return: list[moves]: list of all moves that do not involve back pieces
        """
        raise NotImplementedError

    def check_if_danger(self, valid_moves: list, board: Board):
        """
        returns all the moves that do not put the piece in danger of being captured
        :param: valid_moves: list of valid moves available for the bot
        :param: board Board: game board which is currently played
        :return: list of all moves that are not loosing a piece
        """
        raise NotImplementedError

    def best_jump(self, valid_moves: list):
        """
        Out of all jump moves chooses the farthest jump-move (the one which takes the most pieces)
        :param valid_moves: list of valid moves available for the bot
        :return: list of all jumps that capture maximum amount of pieces
        """
        raise NotImplementedError

    def check_if_can_king(self, valid_moves: list, number_of_rows: int):
        """
        Checks if we can turn a piece into a king with one of the moves
        :param: valid_moves list of valid moves
        :param: number_of_rows int: length of the vertical side of the board
        :return: list of all moves that turn a piece into a king
        """
        raise NotImplementedError

class RandomBot(Player):
    """
    A bot that is able to make random moves, made for the tests
    Public attributes:
        name: str: name that is also a parameter of a parent class
        color: color of the pieces of a given bot
    """
    def __init__(self, name: str, color: str):
        raise NotImplementedError

    def choose_move(self, board, possible_moves):
        """
        Randomly chooses a move
        :param board: Board class instance: current game_board
        :return: tuple(GamePiece, tuple(int, int)): a tuple in a move format specified in the design
        """
        raise NotImplementedError

# TUI
class TUI:
    """
    This class is used to call methods for interacting with user via a console 
    (Text-Based User Interface).
    Both input and output functions are located here

    Public attributes:
        - console: Console used to print messages to the terminal
    """
    def __init__(self):
        raise NotImplementedError
    
    def print_board(self, game, highlights=[]):
        """
        This function prints the board to the console.

        Input:
            game: (Game) The game that is being played

            highlights: (list) A list of (row_number, col_number) tuples to
                         highlight on the board

        """
        raise NotImplementedError

    def print_winner_screen(self, winner=None) -> None:
        """
        Prints information which player won.

        Input:
            player (Player) - player that has won the game. 
                            If player is passed as None, then the game was 
                            terminated with a draw
        """
        raise NotImplementedError

    def get_int_input(self, prompt, range=(-1, -1)):
        """
        This method will repeatedly ask user to select a user to enter an
        integer until a valid value is given.
        
        Inputs:
            prompt (str) - a message that explains what the input is for
            range (tuple(int, int)) - an inclusive range of accepted values, as
                                    follows: (min_val, max_val). If the tuple is
                                    given as (-1,-1) then the range is not
                                    applicable.
        Output:
            (int) - a value of type integer and in a certain range,
                    if was provided.
        """
        raise NotImplementedError

    def get_bool_input(self, prompt, true_ans=["y"], false_ans=["n"]):
        """
        This method will repeatedly ask user to select a user to enter an string
        until a valid value is given.
        Inputs:
            prompt (str) - a message that explains what the input is for
            true_ans (list[str]) - a list of inputs by user that would be
                            considered to be equivalent to an answer of True
            false_ans (list[str]) - a list of inputs by user that would be
                            considered to be equivalent to an answer of False
        Output:
            (bool) - a value of type boolean and in a certain range,
                    if was provided.
        """

        raise NotImplementedError
    
    def get_valid_pos(self, valid_poisitions, prompt="Choose a piece to move"):
        """
        This method will repeatedly ask user to select a valid row and column
        from a list of valid positions. The positions do not get printed in this
        method.

        Inputs:
            valid_poisitions (list[tuple(int, int)]) - a list of valid positions a user must chose from.

            prompt (str) - a message that explains what the input is for
        Output:
            tuple(int,int)
        """
        raise NotImplementedError

    def get_player_move(self,player,game):
        """
        This method will ask user to select a piece to move.

        Inputs:
            player (Player) - player that has to choose a piece to move

            game (Game) - the game that the player has to choose a piece to move
        Output:
            [GamePiece,list[tuple(int,int)]] - the piece that the user chose to move and the move they selected.
        """

        raise NotImplementedError

def is_bot(player) -> bool:
    """
    This method checks if the user passed in parameters is a Bot.

    Input:
        player (Player) - player or an object that inherits from Player class

    Output:
        True - if the player is of class that inherits Player
        False - if the player is of class Player and not its children.
    """
    raise NotImplementedError

class TUIGame:
    """
    This is a class that allows to play a game through TUI.

    parameters:

        players: list[Player]
        board: Booard
        tui: TUI
    """

    def __init__(self, game):
        raise NotImplementedError

    def play_game(self):
        """
        This function is called to play the game,
        using the board set as a class parameters
        """
        raise NotImplementedError       

    def check_player_lost(self, current_player):
        """
        Checks if the player lost the game or not
        Input:
            current_player (Player) - a player whose turn it is
        Output:
            True - if the player has lost the game
            False - if the player has not lost the game
        """
        raise NotImplementedError

    def is_draw(self, current_player, next_player):
        """
        Checks if draw is offered and accepted. Prompts users to
        enter their answer to see if the game should end with a draw.
        Input:
            current_player (Player) - Player that can offer a draw as 
                                      it is their turn.
            next_player (Player) - Player to whom offer can be offered, and they
                                    may accept it or not.
        Output:
            True - the game should be terminated with a draw
            False - the game continues
        """
        raise NotImplementedError


# GUI
def is_players_piece(surface, coordinates, player_color):
    '''
    Checks if the selected location stores the piece of a given player
    '''
    raise NotImplementedError

def get_piece(board, coordinates):
    '''
    Finds and returns the piece (GamePiece) on the board given its coordinates
    '''
    raise NotImplementedError

def get_position(coordinates, game):
    '''
    Converts pixel coordinates into board position (row, column)
    '''
    raise NotImplementedError

def draw_board(game, surface, game_piece = None):
    """ 
    Draws the current state of the board in the window
    Args:
        surface: Pygame surface to draw the board on
        board: The board to draw
    Returns: None
    """
    raise NotImplementedError

def play_checkers(game):
    '''
    Plays a game of Checkers on a Pygame window
    Args:
        board: The board to play on
        players: A list of players (GUIPlayer objects)
    Returns: None
    '''
    raise NotImplementedError

def is_piece_moved(game,piece_to_move, selected_final_position, should_be_jump):
    """
    Checks if the piece is moved or not
    Input:
        piece_to_move (GamePiece) - the piece to move
        selected_final_position (tuple) - the final position of the piece
        should_be_jump (bool) - if the move should be a jump (because the player
                                 has to jump if possible)
    Output:
        True - if the piece is moved to a valid location
        False - if the piece is not moved to a valid location
    """
    raise NotImplementedError

def check_player_lost(game, current_player):
    """
    Checks if the player lost the game or not
    Input:
        current_player (Player) - a player whose turn it is
    Output:
        True - if the player has lost the game
        False - if the player has not lost the game
    """
    raise NotImplementedError
 