


class Board:
    board = [ ['##' for _ in range(8)] for _ in range(8) ]
    pieces_on_board = []
    pieces_removed = []

    #generates the pieces and adds them to the list of pieces on the board 
    def set_pieces_on_board(self):
        self.pieces_on_board.append(self.generate_piece('white',Pawn,1,6,0,1,'pawn','wP',8))
        self.pieces_on_board.append(self.generate_piece('black',Pawn,1,6,0,1,'pawn','bP',8))

        self.pieces_on_board.append(self.generate_piece('black',Knight,0,7,1,5,'knight','bH',2)) 
        self.pieces_on_board.append(self.generate_piece('white',Knight,0,7,1,5,'knight','wH',2)) 

        self.pieces_on_board.append(self.generate_piece('white',King,0,7,4,0,'king','wK',1))     
        self.pieces_on_board.append(self.generate_piece('black',King,0,7,4,0,'king','bK',1))  

        self.pieces_on_board.append(self.generate_piece('white',Queen,0,7,3,0,'queen','wQ',1))     
        self.pieces_on_board.append(self.generate_piece('black',Queen,0,7,3,0,'queen','bQ',1))

        self.pieces_on_board.append(self.generate_piece('white',Bishop,0,7,2,3,'bishop','wB',2))     
        self.pieces_on_board.append(self.generate_piece('black',Bishop,0,7,2,3,'bishop','bB',2))

        self.pieces_on_board.append(self.generate_piece('white',Rook,0,7,0,7,'rook','wR',2))     
        self.pieces_on_board.append(self.generate_piece('black',Rook,0,7,0,7,'rook','bR',2))
    
    def update_board(self):
        self.board = [ ['##' for _ in range(8)] for _ in range(8) ]
        for i in self.pieces_on_board:
            for x in i:
                self.board[x.piece_info.position[1]][x.piece_info.position[0]] = x.piece_info.piece_token

    def generate_piece(self,colour,piece_obj,black_y_start,white_y_start,x_start,x_increment,rank,piece_token,number_of_tokens):
        pieces = []
        if colour == 'black':
            i = 0
            x = x_start
            y = black_y_start
            while i < number_of_tokens :
                pieces.append(piece_obj(Piece(colour,rank,[x,y],piece_token)))
                x += x_increment 
                i += 1
            
        if colour == 'white':
            i = 0
            x = x_start
            y = white_y_start 
            while i < number_of_tokens :
                pieces.append(piece_obj(Piece(colour,rank,[x,y],piece_token)))
                x += x_increment
                i += 1
        return pieces  

    def get_piece_index(self,coords:list):
        #returns position in the pieces_on_board list from the coords of piece return: [x, y]
        counter = 0
        for i in self.pieces_on_board:
            counter += 1
            for x in i :
                if x.piece_info.position == coords:
                    
                    return [self.pieces_on_board.index(i), self.pieces_on_board[counter-1].index(x)]
        
                else:
                    return False

    def update_piece_position(self,coords:list, target:list):
        piece_index = board.get_piece_index(coords) 
        self.pieces_on_board[piece_index[0]][piece_index[1]].piece_info.position = target
    
    def string_to_index(self,str):
         return ord(str) -97
        
    def move_piece(self,move_str):
        if self.is_move_legal() == True :
            parsed_str = self.parse_move_string(move_str)
            piece_coords= [parsed_str[0], parsed_str[1]]
            target_coords = [parsed_str[2], parsed_str[3]]
            self.update_piece_position(piece_coords,target_coords)
            self.update_board()
        else:
            print('Move is not legal')

    def is_move_legal(self,move,piece:object):
        pass

    def is_position_occupied(self,target_coords:list):
        if self.get_piece_index(target_coords) == False:
            return True
        else:
            return False


        

    def parse_move_string(self,move_str:str):
        #parse the move string input by player e.g. a 1 a 2 
        move_str_list = move_str.split(' ')
        move_str_list[0] , move_str_list[2] = self.string_to_index(move_str_list[0]) , self.string_to_index(move_str_list[2])
        move_str_list[1] , move_str_list[3] = int(move_str_list[1]) , int(move_str_list[3])
        return move_str_list
            
    def print_board(self):
        print(' _____________________________________________________________________')
        print('｜',self.board[0][0],'｜','｜',self.board[0][1],'｜','｜',self.board[0][2],'｜','｜',self.board[0][3],'｜','｜',self.board[0][4],'｜','｜',self.board[0][5],'｜','｜',self.board[0][6],'｜','｜',self.board[0][7],'｜',)
        print('｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ')
        print(' _____________________________________________________________________')
        print('｜',self.board[1][0],'｜','｜',self.board[1][1],'｜','｜',self.board[1][2],'｜','｜',self.board[1][3],'｜','｜',self.board[1][4],'｜','｜',self.board[1][5],'｜','｜',self.board[1][6],'｜','｜',self.board[1][7],'｜',)
        print('｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ')
        print(' _____________________________________________________________________')
        print('｜',self.board[2][0],'｜','｜',self.board[2][1],'｜','｜',self.board[2][2],'｜','｜',self.board[2][3],'｜','｜',self.board[2][4],'｜','｜',self.board[2][5],'｜','｜',self.board[2][6],'｜','｜',self.board[2][7],'｜',)
        print('｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ')
        print(' _____________________________________________________________________')
        print('｜',self.board[3][0],'｜','｜',self.board[3][1],'｜','｜',self.board[3][2],'｜','｜',self.board[3][3],'｜','｜',self.board[3][4],'｜','｜',self.board[3][5],'｜','｜',self.board[3][6],'｜','｜',self.board[3][7],'｜',)
        print('｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ')
        print(' _____________________________________________________________________')
        print('｜',self.board[4][0],'｜','｜',self.board[4][1],'｜','｜',self.board[4][2],'｜','｜',self.board[4][3],'｜','｜',self.board[4][4],'｜','｜',self.board[4][5],'｜','｜',self.board[4][6],'｜','｜',self.board[4][7],'｜',)
        print('｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ')
        print(' _____________________________________________________________________')
        print('｜',self.board[5][0],'｜','｜',self.board[5][1],'｜','｜',self.board[5][2],'｜','｜',self.board[5][3],'｜','｜',self.board[5][4],'｜','｜',self.board[5][5],'｜','｜',self.board[5][6],'｜','｜',self.board[5][7],'｜',)
        print('｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ')
        print(' _____________________________________________________________________')
        print('｜',self.board[6][0],'｜','｜',self.board[6][1],'｜','｜',self.board[6][2],'｜','｜',self.board[6][3],'｜','｜',self.board[6][4],'｜','｜',self.board[6][5],'｜','｜',self.board[6][6],'｜','｜',self.board[6][7],'｜',)
        print('｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ')
        print(' _____________________________________________________________________')
        print('｜',self.board[7][0],'｜','｜',self.board[7][1],'｜','｜',self.board[7][2],'｜','｜',self.board[7][3],'｜','｜',self.board[7][4],'｜','｜',self.board[7][5],'｜','｜',self.board[7][6],'｜','｜',self.board[7][7],'｜',)
        print('｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ')
        print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')

class Piece:
    colour: str 
    rank: str 
    position: list
    piece_token: str

    def __init__(self,colour,rank,position,piece_token):
        self.colour = colour
        self.rank = rank 
        self.position = position
        self.piece_token = piece_token
        

    def __repr__(self):
        return f'{self.colour}  {self.rank} {str(self.position)}'

class Pawn(Board):
    piece_info: Piece
    en_passant_vunerable: False
    has_moved: False
    promoted :False
   

    def __init__(self,piece_info):
        self.piece_info = piece_info
    
    def __repr__(self):
        return repr(self.piece_info)
        

    def flip_en_passant(self):
        if self.en_passant_vunerable == False:
            self.en_passant_vunerable = True
        elif self.en_passant_vunerable == True:
            self.en_passant_vunerable = False
    
    def pawn_legal_moves(self):
        legal_moves = []
        if self.piece_info.colour == 'black':
            if self.has_moved == False:
                legal_moves.append([self.piece_info.position[0],self.piece_info.position[1] + 1])
                legal_moves.append([self.piece_info.position[0],self.piece_info.position[1] + 2])
                pass
            elif self.has_moved == True:
                legal_moves.append([self.piece_info.position[0],self.piece_info.position[1] + 1])
            return legal_moves

        if self.piece_info.colour == 'white':
            if self.has_moved == False:
                legal_moves.append([self.piece_info.position[0],self.piece_info.position[1] - 1])
                legal_moves.append([self.piece_info.position[0],self.piece_info.position[1] - 2])
                return legal_moves
            elif self.has_moved == True:
                legal_moves.append([self.piece_info.position[0],self.piece_info.position[1] - 1])
                return legal_moves

    def legal_takes(self):
        #assess if there is a piece on the diagonal 
        #assess if there is a piece ajacent which is a pawn that is in the correct state for en_passant 
        #return those coords if there is a piece to take 
        return_value = []
        ajacent_a, ajacent_b = [self.piece_info.position[0], self.piece_info.position[1] + 1] , [self.piece_info.position[0], self.piece_info.position[1] - 1]
        diagonal_a , diagonal_b = [self.piece_info.position[0] + 1, self.piece_info.position[1] + 1] , [self.piece_info.position[0] - 1, self.piece_info.position[1] + 1]
        if Board.is_position_occupied(diagonal_a) == True :
            return_value.append(diagonal_a)
        if Board.is_position_occupied(diagonal_b) == True :
            return_value.append(diagonal_b)
        if Board.is_position_occupied(ajacent_a) == True and Board.pieces_on_board[Board.get_piece_index(ajacent_a)[0],Board.get_piece_index(ajacent_a)[1]].piece_info.rank == 'pawn':
            if Board.pieces_on_board[Board.get_piece_index(ajacent_a)[0],Board.get_piece_index(ajacent_a)[1]].piece_info.colour == self.piece_info.colour:
                pass
            elif Board.pieces_on_board[Board.get_piece_index(ajacent_a)[0],Board.get_piece_index(ajacent_a)[1]].enpassant_vunerable == True:
                return_value.append(diagonal_a)
        if Board.is_position_occupied(ajacent_b) == True and Board.pieces_on_board[Board.get_piece_index(ajacent_b)[0],Board.get_piece_index(ajacent_b)[1]].piece_info.rank == 'pawn':
            if Board.pieces_on_board[Board.get_piece_index(ajacent_b)[0],Board.get_piece_index(ajacent_b)[1]].piece_info.colour == self.piece_info.colour:
                pass
            elif Board.pieces_on_board[Board.get_piece_index(ajacent_b)[0],Board.get_piece_index(ajacent_b)[1]].enpassant_vunerable == True :
                return_value.append(diagonal_a)
        ##note make this work for both black and white TODO reverse the values 
        pass

class Rook:
    piece_info: Piece
    has_moved: False
    
    def __init__(self,piece_info):
        self.piece_info = piece_info

    def __repr__(self):
        return repr(self.piece_info)
    

class Knight :
    piece_info: Piece
    has_moved: False

    def __init__(self,piece_info):
        self.piece_info = piece_info

    def __repr__(self):
        return repr(self.piece_info)

class Queen :
    piece_info: Piece

    def __init__(self,piece_info):
        self.piece_info = piece_info
    
    def __repr__(self):
        return repr(self.piece_info)

class King:
    piece_info: Piece

    def __init__(self,piece_info):
        self.piece_info = piece_info

    def __repr__(self):
        return repr(self.piece_info)

class Bishop:
    piece_info: Piece

    def __init__(self,piece_info):
        self.piece_info = piece_info
    
    def __repr__(self):
        return repr(self.piece_info)


board = Board()
board.set_pieces_on_board()
board.update_board()
board.print_board()
print(board.get_piece_index([0,7]))
board_index = board.get_piece_index([7,0])
print(board.pieces_on_board[board_index[0]][board_index[1]])
board.move_piece('a 6 a 5')
board.print_board()





##### old code before refactoring #########

# class Engine :
#     def __init__(self):
#         self.board = [
#             ['bR','bH','bB','bK','bQ','bB','bH','bR'],
#             ['bP','bP','bP','bP','bP','bP','bP','bP',],
#             ['--','--','--','--','--','--','--','--',],
#             ['--','--','--','--','--','--','--','--',],
#             ['wR','--','bP','--','--','--','--','--',],
#             ['--','--','--','--','--','--','--','--',],
#             ['--','wP','wP','wP','wP','wP','wP','wP',],
#             ['bP','wH','wB','wK','wQ','wB','wH','wR'],
#         ] 
#         self.move_log = []
#         self.w_pawn_enpass_able = {}
#         self.b_pawn_enpass_able = {}
#         self.white_turn = True
#         self.black_turn = False 
#         self.victory = False 
        

#     def print_board(self):
#         print(' _____________________________________________________________________')
#         print('｜',self.board[0][0],'｜','｜',self.board[0][1],'｜','｜',self.board[0][2],'｜','｜',self.board[0][3],'｜','｜',self.board[0][4],'｜','｜',self.board[0][5],'｜','｜',self.board[0][6],'｜','｜',self.board[0][7],'｜',)
#         print('｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ')
#         print(' _____________________________________________________________________')
#         print('｜',self.board[1][0],'｜','｜',self.board[1][1],'｜','｜',self.board[1][2],'｜','｜',self.board[1][3],'｜','｜',self.board[1][4],'｜','｜',self.board[1][5],'｜','｜',self.board[1][6],'｜','｜',self.board[1][7],'｜',)
#         print('｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ')
#         print(' _____________________________________________________________________')
#         print('｜',self.board[2][0],'｜','｜',self.board[2][1],'｜','｜',self.board[2][2],'｜','｜',self.board[2][3],'｜','｜',self.board[2][4],'｜','｜',self.board[2][5],'｜','｜',self.board[2][6],'｜','｜',self.board[2][7],'｜',)
#         print('｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ')
#         print(' _____________________________________________________________________')
#         print('｜',self.board[3][0],'｜','｜',self.board[3][1],'｜','｜',self.board[3][2],'｜','｜',self.board[3][3],'｜','｜',self.board[3][4],'｜','｜',self.board[3][5],'｜','｜',self.board[3][6],'｜','｜',self.board[3][7],'｜',)
#         print('｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ')
#         print(' _____________________________________________________________________')
#         print('｜',self.board[4][0],'｜','｜',self.board[4][1],'｜','｜',self.board[4][2],'｜','｜',self.board[4][3],'｜','｜',self.board[4][4],'｜','｜',self.board[4][5],'｜','｜',self.board[4][6],'｜','｜',self.board[4][7],'｜',)
#         print('｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ')
#         print(' _____________________________________________________________________')
#         print('｜',self.board[5][0],'｜','｜',self.board[5][1],'｜','｜',self.board[5][2],'｜','｜',self.board[5][3],'｜','｜',self.board[5][4],'｜','｜',self.board[5][5],'｜','｜',self.board[5][6],'｜','｜',self.board[5][7],'｜',)
#         print('｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ')
#         print(' _____________________________________________________________________')
#         print('｜',self.board[6][0],'｜','｜',self.board[6][1],'｜','｜',self.board[6][2],'｜','｜',self.board[6][3],'｜','｜',self.board[6][4],'｜','｜',self.board[6][5],'｜','｜',self.board[6][6],'｜','｜',self.board[6][7],'｜',)
#         print('｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ')
#         print(' _____________________________________________________________________')
#         print('｜',self.board[7][0],'｜','｜',self.board[7][1],'｜','｜',self.board[7][2],'｜','｜',self.board[7][3],'｜','｜',self.board[7][4],'｜','｜',self.board[7][5],'｜','｜',self.board[7][6],'｜','｜',self.board[7][7],'｜',)
#         print('｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ｜    ｜ ')
#         print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')

#     def string_to_index(self,str):
#         return ord(str) -97

#     def move_piece(self,piece_x,piece_y,x,y):
#         piece_start_x = self.string_to_index(piece_x) 
#         piece_start_y = piece_y -1
#         target_x = self.string_to_index(x)
#         target_y = y -1
        
#         if self.is_move_legal(piece_start_x,piece_start_y,target_x,target_y) == True:
#             #White and black Pawn moves 
#             if self.board[piece_start_y][piece_start_x] == 'wP': #check if the piece being moved is white pawn and begin secondary checks 
#                 if piece_x in self.w_pawn_enpass_able: #check if the piece has been moved yet and has an entry in self.w_pawn_enpass_able
#                     if self.w_pawn_enpass_able[piece_x] == True:  #if previously able to be taken by en passant then flip it to False 
#                         self.w_pawn_enpass_able[piece_x] = False 
#                         self.move(target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y) 

#                     elif self.w_pawn_enpass_able[piece_x] == False: #if it is false keep false and move 
#                         self.move(target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y) 

#                 elif piece_start_y - target_y == 2:  # if there is no entry in the enpass log and it is moved by 2 then add entry to enpass 
#                         self.w_pawn_enpass_able[piece_x] = True
#                         self.move(target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y)                         

#                 else:  #if no enpass entry is present and it isn't moving 2 then set the enpass log to false 
#                     self.w_pawn_enpass_able[piece_x] = False 
#                     self.move(target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y)                     

            
#             elif self.board[piece_start_y][piece_start_x] == 'bP': #check if the piece being moved is white pawn and begin secondary checks 
#                 if piece_x in self.b_pawn_enpass_able: #check if the piece has been moved yet and has an entry in self.w_pawn_enpass_able
#                     if self.b_pawn_enpass_able[piece_x] == True:  #if previously able to be taken by en passant then flip it to False 
#                         self.b_pawn_enpass_able[piece_x] = False  
#                         self.move(target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y)                         


#                     elif self.b_pawn_enpass_able[piece_x] == False: #if it is false keep false and move 
#                         self.move(target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y)                         

#                 elif target_y - piece_start_y == 2:  # if there is no entry in the enpass log and it is moved by 2 then add entry to enpass 
#                         self.b_pawn_enpass_able[piece_x] = True
#                         self.move(target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y) 

#                 else:  #if no enpass entry is present and it isn't moving 2 then set the enpass log to false 
#                     self.b_pawn_enpass_able[piece_x] = False
#                     self.move(target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y)     
                             

#             else : #pieces that don't require any extra checks can have their move executed after checking for legality 
#                 self.move(target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y)                 
                     
#         else:
#             print('Move is not legal')
    

#     def is_move_legal(self,piece_x,piece_y,target_x,target_y):
#         print(piece_x,target_x)
#         print(piece_y,target_y)
#         #White and black pawn legal moves 
#         if self.board[piece_y][piece_x] == 'wP':
#             if piece_x == target_x and target_y == piece_y - 1 and self.board[target_y][target_x] == '--': #alows to move 1 space forward into an empty space 
#                 return True
#             elif piece_x == target_x and piece_y == 6 and target_y == piece_y -2:  #alows for double move on the first turn of the pawn 
#                 return True
#             elif target_y == piece_y - 1 and  self.is_space_blank(self.board[target_y][target_x]) == False: #allows for a diagonal take  from the
#                 return True 
#             elif self.board[piece_y][piece_x +1] == 'bP' and self.is_space_blank(self.board[target_y][target_x]) == True and self.b_pawn_enpass_able[chr(piece_x + 98)] == True or self.b_pawn_enpass_able[chr(piece_x + 96)] == True:  #en passant 
#                 self.board[target_y + 1][target_x] = '--'
#                 return True 
#             else:
#                 return False
              
#         if self.board[piece_y][piece_x] == 'bP':
#             if piece_x == target_x and target_y == piece_y + 1 and self.board[target_y][target_x] == '--': #alows to move 1 space forward into an empty space 
#                 return True
#             elif piece_x == target_x and piece_y == 1 and target_y == piece_y + 2:  #alows for double move on the first turn of the pawn 
#                 return True
#             elif target_y == piece_y + 1 and  self.is_space_blank(self.board[target_y][target_x]) == False: #allows for a diagonal take  from the
#                 return True 
#             elif self.board[piece_y][piece_x +1] == 'wP' and self.is_space_blank(self.board[target_y][target_x]) == True and self.w_pawn_enpass_able[chr(piece_x + 98)] == True or self.w_pawn_enpass_able[chr(piece_x + 96)] == True:  #en passant 
#                 self.board[target_y - 1][target_x] = '--'
#                 return True 
#             else:
#                 return False
#         ##white and black rook legal moves 
#         if self.board[piece_y][piece_x] == 'wR' or self.board[piece_y][piece_x] == 'bR' : 
#             print(self.is_rook_blocked(piece_y,piece_x,target_y,target_x))
#             if piece_x == target_x  and self.is_rook_blocked(piece_y,piece_x,target_y,target_x) == False :
#                 return True  
#             elif piece_y == target_y and self.is_rook_blocked(piece_y,piece_x,target_y,target_x) == False:
#                 return True
#             else:
#                 return False 

#         #knight legal moves 
#         if self.board[piece_y][piece_x] == 'wH' or self.board[piece_y][piece_x] == 'bH':
#             if target_x == piece_x + 1 and target_y == piece_y + 2 or target_y == piece_y - 2 and target_x == piece_x -1 or target_y == piece_y + 2 and target_x == piece_x + 1 or target_y == piece_y -2 and target_x == piece_x -1:
#                 return True
#             elif 
#             else:
#                 return False 
        
#         else:
#             return False

#     def is_space_blank(self,space):
#         if space == '--':
#             return True
#         else:
#             return False

#     def is_rook_blocked(self,piece_start_y,piece_start_x,target_y,target_x):
#         x_index = piece_start_x
#         y_index = piece_start_y
#         print(y_index) 
#         print(target_y)
#         if target_x == piece_start_x: #is rook blocked on the y axis move 
#             while y_index > target_y + 1 : 
#                 if self.is_space_blank(self.board[y_index - 1][x_index]) == True : 
#                     y_index -= 1
                    
#                 elif self.is_space_blank(self.board[y_index - 1][x_index]) == False :
#                     return True

#         elif target_y == piece_start_y: #is rook blocked on the x axis move 
#             while x_index < target_x - 1 : 
#                 if self.is_space_blank(self.board[y_index][x_index + 1]) == True : 
#                     x_index += 1
                    
#                 elif self.is_space_blank(self.board[y_index ][x_index + 1]) == False :
#                     return True
        
#         return False 

#     def move(self,target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y):
#         self.board[target_y][target_x] = self.board[piece_start_y][piece_start_x]
#         self.board[piece_start_y][piece_start_x] = '--'
#         self.move_log.append([piece_x,piece_y,x,y])
#         pass
            
    
    


           
        
            



        
