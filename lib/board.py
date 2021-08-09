

class Board :
    '''
    The chess board is defied by ICCF numberic notation for ease of operation 
    https://en.wikipedia.org/wiki/ICCF_numeric_notation
    the self.board attribute reutrns a dictionary with the ICCF number as the key to store the positions of all pieces currently on the board
    '''
    def __init__(self):
         self.build_board_squares()

    def build_board_squares(self):
        board_squares = {}
        i = 11 
        while i < 89:
            board_squares.update(self.build_column(i))
            i += 10
        self.board_positions = board_squares

    def build_column(self,column_index):
        column = {}
        index = column_index
        while index < column_index + 8:
            column[index] = 'EMPTY'
            index += 1 
        return column 
    
    def pawn_start_positions(self,pawn):
        if pawn.colour == 'white' :
            pass




       
