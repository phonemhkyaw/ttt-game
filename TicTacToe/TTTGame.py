import random
cross_mark = "X"
circle_mark = "O"
should_continue = True

player_1_mark = ""
player_2_mark = ""

class TTTGame: 
    def __init__(self) -> None:    #constructor
       
        self.board = ["-", "-", "-",
    "-", "-", "-", 
    "-", "-", "-"]                  #EVERY new object has these attributes 
        

    def start(self):
        global player_1_mark
        global player_2_mark
        
        print("\nWELCOME TO TIC TAC TOE!\n ")
        version = int(input("Enter 1 for Computer or 2 for 2 - Player: "))
        
        while version != 1 and version != 2:
            print("Invalid Input! ")
            version = int(input("Enter 1 for Computer or 2 for 2-Player: "))

        if version == 1:
            print("\nPLAY!")
            self.print_board() #initial printing of board
            self.computer_path()
        elif version == 2:
            self.player_path()

    def player_path(self):
        global player_1_mark
        global player_2_mark

        player_1 = input("Player 1 - Choose: X or O: ").lower()
        
        while player_1 != "x" and player_1 != "o":
            print("Invalid Input!")
            player_1 = input("Player 1 - Choose: X or O: ").lower()
        
        if player_1 == "x":
            player_1_mark = cross_mark
        elif player_1 == "o":
            player_1_mark = circle_mark

        
        if player_1_mark == cross_mark:
            player_2_mark = circle_mark
        else:
            player_2_mark = cross_mark
        
        print(f"Player 2 - Your mark: {player_2_mark}")

        print("\nPLAY!")
        self.print_board()

        
        while should_continue:
            position_num = int(input("\nPLAYER 1 - Choose a position 1-9: "))
            position_index = position_num - 1


            while self.board[position_index] != "-":
                print("\nThis Spot is Already Taken! ")
                position_num = int(input("PLAYER 1 - RECHOOSE a position 1-9: "))
                position_index = position_num - 1 
                
            self.board[position_index] = player_1_mark

            self.print_board()

            if self.check_player_1_win():
                print("\nPLAYER 1 WINS!")
                break
            elif self.check_tie():
                print("\nIT'S A TIE!")
                break
            
            position_num = int(input("\nPLAYER 2 - Choose a position 1-9: "))
            position_index = position_num - 1


            while self.board[position_index] != "-":
                print("\nThis Spot is Already Taken! ")
                position_num = int(input("PLAYER 2 - RECHOOSE a position 1-9: "))
                position_index = position_num - 1 
                
            self.board[position_index] = player_2_mark
 
            self.print_board()

            if self.check_player_2_win():
                print("\nPLAYER 2 WINS!")
                break

              

    def computer_path(self):
        global should_continue
        
        while should_continue:
            position_num = int(input("\nChoose a position 1-9: "))
            position_index = position_num - 1


            while self.board[position_index] != "-":
                print("\nThis Spot is Already Taken! ")
                position_num = int(input("RECHOOSE a position 1-9: "))
                position_index = position_num - 1 
                
            self.board[position_index] = cross_mark

            print(f"\nYOUR TURN: ")  
            self.print_board()

        # MUST CHECK FOR WIN/TIE BEFORE COMPUTER GETS STUCK IN LOOP
            if self.check_player_win():
                print("\nPLAYER WINS!")
                break
            elif self.check_tie():
                print("\nIT'S A TIE!")
                break
            
            random_num = random.randint(1,9)
            computer_position_index = random_num - 1
        
            while self.board[computer_position_index] != "-": #keep looking for empty slot
                random_num = random.randint(1,9)
                computer_position_index = random_num - 1

            self.board[computer_position_index] = circle_mark    
            
            
            if self.check_computer_win():
                print("\nCOMPUTER'S TURN: ")
                self.print_board()
                print("\nCOMPUTER WINS!")
                break
            else:
                print("\nCOMPUTER'S TURN: ")
                self.print_board()

                

    def check_player_1_win(self):

        if (self.board[0] == player_1_mark) and (self.board[1] == player_1_mark) and (self.board[2] == player_1_mark):
            return True
            
        elif (self.board[3] == player_1_mark) and (self.board[4] == player_1_mark) and (self.board[5] == player_1_mark):
            return True
            
        elif (self.board[6] == player_1_mark) and (self.board[7] == player_1_mark) and (self.board[8] == player_1_mark):
            return True
            
        elif (self.board[0] == player_1_mark) and (self.board[3] == player_1_mark) and (self.board[6] == player_1_mark):
            return True
            
        elif (self.board[1] == player_1_mark) and (self.board[4] == player_1_mark) and (self.board[7] == player_1_mark):
            return True
            
        elif (self.board[2] == player_1_mark) and (self.board[5] == player_1_mark) and (self.board[8] == player_1_mark):
            return True
        
        elif (self.board[0] == player_1_mark) and (self.board[4] == player_1_mark) and (self.board[8] == player_1_mark):
            return True
              
        elif (self.board[2] == player_1_mark) and (self.board[4] == player_1_mark) and (self.board[6] == player_1_mark):
            return True
       
    
    def check_player_2_win(self):
     
        if (self.board[0] == player_2_mark) and (self.board[1] == player_2_mark) and (self.board[2] == player_2_mark):
            return True
            
        elif (self.board[3] == player_2_mark) and (self.board[4] == player_2_mark) and (self.board[5] == player_2_mark):
            return True
            
        elif (self.board[6] == player_2_mark) and (self.board[7] == player_2_mark) and (self.board[8] == player_2_mark):
            return True
            
        elif (self.board[0] == player_2_mark) and (self.board[3] == player_2_mark) and (self.board[6] == player_2_mark):
            return True
            
        elif (self.board[1] == player_2_mark) and (self.board[4] == player_2_mark) and (self.board[7] == player_2_mark):
            return True
            
        elif (self.board[2] == player_2_mark) and (self.board[5] == player_2_mark) and (self.board[8] == player_2_mark):
            return True
        
        elif (self.board[0] == player_2_mark) and (self.board[4] == player_2_mark) and (self.board[8] == player_2_mark):
            return True
              
        elif (self.board[2] == player_2_mark) and (self.board[4] == player_2_mark) and (self.board[6] == player_2_mark):
            return True


    def check_tie(self):
        if "-" not in self.board:
            return True
        

    def check_player_win(self):
    
        if (self.board[0] == cross_mark) and (self.board[1] == cross_mark) and (self.board[2] == cross_mark):
            return True
        
        elif (self.board[3] == cross_mark) and (self.board[4] == cross_mark) and (self.board[5] == cross_mark):
            return True
            
        elif (self.board[6] == cross_mark) and (self.board[7] == cross_mark) and (self.board[8] == cross_mark):
            return True
            
        elif (self.board[0] == cross_mark) and (self.board[3] == cross_mark) and (self.board[6] == cross_mark):
            return True
            
        elif (self.board[1] == cross_mark) and (self.board[4] == cross_mark) and (self.board[7] == cross_mark):
            return True
            
        elif (self.board[2] == cross_mark) and (self.board[5] == cross_mark) and (self.board[8] == cross_mark):
            return True
        
        elif (self.board[0] == cross_mark) and (self.board[4] == cross_mark) and (self.board[8] == cross_mark):
            return True
              
        elif (self.board[2] == cross_mark) and (self.board[4] == cross_mark) and (self.board[6] == cross_mark):
            return True
       
    def check_computer_win(self):
        
        if (self.board[0] == circle_mark) and (self.board[1] == circle_mark) and (self.board[2] == circle_mark):
            return True
            
        elif (self.board[3] == circle_mark) and (self.board[4] == circle_mark) and (self.board[5] == circle_mark):
            return True
      
        elif (self.board[6] == circle_mark) and (self.board[7] == circle_mark) and (self.board[8] == circle_mark):
            return True
         
        elif (self.board[0] == circle_mark) and (self.board[3] == circle_mark) and (self.board[6] == circle_mark):
            return True
           
        elif (self.board[1] == circle_mark) and (self.board[4] == circle_mark) and (self.board[7] == circle_mark):
            return True
           
        elif (self.board[2] == circle_mark) and (self.board[5] == circle_mark) and (self.board[8] == circle_mark):
            return True
           
        elif (self.board[0] == circle_mark) and (self.board[4] == circle_mark) and (self.board[8] == circle_mark):
            return True
         
        elif (self.board[2] == circle_mark) and (self.board[4] == circle_mark) and (self.board[6] == circle_mark):
            return True
            
    
    def print_board(self):
        
        print(self.board[0] + "|" + self.board[1] + "|" + self.board[2])
        print("—————")
        print(self.board[3] + "|" + self.board[4] + "|" + self.board[5])
        print("—————")
        print(self.board[6] + "|" + self.board[7] + "|" + self.board[8])



