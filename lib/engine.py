



class Engine :
    def __init__(self):
        self.board = [
            ['bR','bH','bB','bK','bQ','bB','bH','bR'],
            ['bP','bP','bP','bP','bP','bP','bP','bP',],
            ['--','--','--','--','--','--','--','--',],
            ['--','--','--','--','--','--','--','--',],
            ['wR','--','bP','--','--','--','--','--',],
            ['--','--','--','--','--','--','--','--',],
            ['--','wP','wP','wP','wP','wP','wP','wP',],
            ['bP','wH','wB','wK','wQ','wB','wH','wR'],
        ] 
        self.move_log = []
        self.w_pawn_enpass_able = {}
        self.b_pawn_enpass_able = {}
        self.white_turn = True
        self.black_turn = False 

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

    def string_to_index(self,str):
        return ord(str) -97

    def move_piece(self,piece_x,piece_y,x,y):
        piece_start_x = self.string_to_index(piece_x) 
        piece_start_y = piece_y -1
        target_x = self.string_to_index(x)
        target_y = y -1
        
        if self.is_move_legal(piece_start_x,piece_start_y,target_x,target_y) == True:
            #White and black Pawn moves 
            if self.board[piece_start_y][piece_start_x] == 'wP': #check if the piece being moved is white pawn and begin secondary checks 
                if piece_x in self.w_pawn_enpass_able: #check if the piece has been moved yet and has an entry in self.w_pawn_enpass_able
                    if self.w_pawn_enpass_able[piece_x] == True:  #if previously able to be taken by en passant then flip it to False 
                        self.w_pawn_enpass_able[piece_x] = False 
                        self.move(target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y) 

                    elif self.w_pawn_enpass_able[piece_x] == False: #if it is false keep false and move 
                        self.move(target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y) 

                elif piece_start_y - target_y == 2:  # if there is no entry in the enpass log and it is moved by 2 then add entry to enpass 
                        self.w_pawn_enpass_able[piece_x] = True
                        self.move(target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y)                         

                else:  #if no enpass entry is present and it isn't moving 2 then set the enpass log to false 
                    self.w_pawn_enpass_able[piece_x] = False 
                    self.move(target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y)                     

            
            elif self.board[piece_start_y][piece_start_x] == 'bP': #check if the piece being moved is white pawn and begin secondary checks 
                if piece_x in self.b_pawn_enpass_able: #check if the piece has been moved yet and has an entry in self.w_pawn_enpass_able
                    if self.b_pawn_enpass_able[piece_x] == True:  #if previously able to be taken by en passant then flip it to False 
                        self.b_pawn_enpass_able[piece_x] = False  
                        self.move(target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y)                         


                    elif self.b_pawn_enpass_able[piece_x] == False: #if it is false keep false and move 
                        self.move(target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y)                         

                elif target_y - piece_start_y == 2:  # if there is no entry in the enpass log and it is moved by 2 then add entry to enpass 
                        self.b_pawn_enpass_able[piece_x] = True
                        self.move(target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y) 

                else:  #if no enpass entry is present and it isn't moving 2 then set the enpass log to false 
                    self.b_pawn_enpass_able[piece_x] = False
                    self.move(target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y)                      


            else : #pieces that don't require any extra checks can have their move executed after checking for legality 
                self.move(target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y)                 
                     
        else:
            print('Move is not legal')
    

    def is_move_legal(self,piece_x,piece_y,target_x,target_y):
        print(piece_x,target_x)
        print(piece_y,target_y)
        #White and black pawn legal moves 
        if self.board[piece_y][piece_x] == 'wP':
            if piece_x == target_x and target_y == piece_y - 1 and self.board[target_y][target_x] == '--': #alows to move 1 space forward into an empty space 
                return True
            elif piece_x == target_x and piece_y == 6 and target_y == piece_y -2:  #alows for double move on the first turn of the pawn 
                return True
            elif target_y == piece_y - 1 and  self.is_space_blank(self.board[target_y][target_x]) == False: #allows for a diagonal take  from the
                return True 
            elif self.board[piece_y][piece_x +1] == 'bP' and self.is_space_blank(self.board[target_y][target_x]) == True and self.b_pawn_enpass_able[chr(piece_x + 98)] == True or self.b_pawn_enpass_able[chr(piece_x + 96)] == True:  #en passant 
                self.board[target_y + 1][target_x] = '--'
                return True 
            else:
                return False
              
        if self.board[piece_y][piece_x] == 'bP':
            if piece_x == target_x and target_y == piece_y + 1 and self.board[target_y][target_x] == '--': #alows to move 1 space forward into an empty space 
                return True
            elif piece_x == target_x and piece_y == 1 and target_y == piece_y + 2:  #alows for double move on the first turn of the pawn 
                return True
            elif target_y == piece_y + 1 and  self.is_space_blank(self.board[target_y][target_x]) == False: #allows for a diagonal take  from the
                return True 
            elif self.board[piece_y][piece_x +1] == 'wP' and self.is_space_blank(self.board[target_y][target_x]) == True and self.w_pawn_enpass_able[chr(piece_x + 98)] == True or self.w_pawn_enpass_able[chr(piece_x + 96)] == True:  #en passant 
                self.board[target_y - 1][target_x] = '--'
                return True 
            else:
                return False
        ##white and black rook legal moves 
        if self.board[piece_y][piece_x] == 'wR' or self.board[piece_y][piece_x] == 'bR' : 
            print(self.is_rook_blocked(piece_y,piece_x,target_y,target_x))
            if piece_x == target_x  and self.is_rook_blocked(piece_y,piece_x,target_y,target_x) == False :
                return True  
            elif piece_y == target_y and self.is_rook_blocked(piece_y,piece_x,target_y,target_x) == False:
                return True
        
        else:
            return False

    def is_space_blank(self,space):
        if space == '--':
            return True
        else:
            return False

    def is_rook_blocked(self,piece_start_y,piece_start_x,target_y,target_x):
        x_index = piece_start_x
        y_index = piece_start_y
        print(y_index) 
        print(target_y)
        if target_x == piece_start_x: #is rook blocked on the y axis move 
            while y_index > target_y + 1 : 
                if self.is_space_blank(self.board[y_index - 1][x_index]) == True : 
                    y_index -= 1
                    
                elif self.is_space_blank(self.board[y_index - 1][x_index]) == False :
                    return True

        elif target_y == piece_start_y: #is rook blocked on the x axis move 
            while x_index < target_x - 1 : 
                if self.is_space_blank(self.board[y_index][x_index + 1]) == True : 
                    x_index += 1
                    
                elif self.is_space_blank(self.board[y_index ][x_index + 1]) == False :
                    return True
        
        return False 
    def move(self,target_y,target_x,piece_start_y,piece_start_x,piece_x,piece_y,x,y):
        self.board[target_y][target_x] = self.board[piece_start_y][piece_start_x]
        self.board[piece_start_y][piece_start_x] = '--'
        self.move_log.append([piece_x,piece_y,x,y])
        pass
            
    
    


           
        
            



        
