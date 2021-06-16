

class Piece :

    def __init__(self, rank, colour , position):
        
        self.rank = rank
        self.colour = colour
        self.position = position 
    
            
class Board :
    '''
    The chess board is defied by ICCF numberic notation for ease of operation 
    https://en.wikipedia.org/wiki/ICCF_numeric_notation
    '''
    def __init__(self):
        self.board_squares = self.build_board_squares()

    def build_board_squares(self):
        board_squares = {}
        i = 11 
        while i < 89:
            board_squares.update(self.build_column(i))
            i += 10
        return board_squares

    def build_column(self,column_index):
        column = {}
        index = column_index
        while index < column_index + 8:
            column[index] = 'EMPTY'
            index += 1 
        return column 





        

                 
                

       
            
            




    

        
    


    



