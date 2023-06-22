class TicTacToe():
    """ Tic-Tac-Toe game class """

    def __init__(self):
        self.running = True
        self.tictactoe = []

        # Init arr with 9 zeroes
        for i in range(9):
            self.tictactoe.append(0)

        # True represents playerones turn
        self.playerone_turn = True
      
        pass
    

    def play_turn(self,x_coord,y_coord):
        """ Classic turn of Tic-Tac-Toe """

        # Error checking
        if 3<x_coord<0:
            print("Err: X coord out of range")
            return
        if 3<y_coord<0:
            print("Err: Y coord out of range")
            return
        if self.tictactoe[y_coord*3+x_coord] != 0:
            print("Error: already selected")
            return
        

        # Set value
        val_to_set = 2
        # 1:X
        # 2:O
        if self.playerone_turn:
            val_to_set-=1
        self.tictactoe[y_coord*3+x_coord] = val_to_set

        # Switch turn
        self.playerone_turn = not self.playerone_turn




    def print_board(self):
        """ 
        Print the board\n
        Player one = X\n
        Player two = O
        """

        translte_table = "-XO"
        for i in range(3):
            row_substr = ""
            for j in range(3):
                row_substr = row_substr + translte_table[self.tictactoe[i*3+j]] + " "
            print(row_substr)

    
    def check_win(self):
        """
        Checks for win on vertical, horizontal and diagonal
        """

        # Check columns
        # Col num
        for x in range(3):
            num = x
            # Y pos
            for i in range(3):
                actual_num = self.tictactoe[num]

                # Exit loop if 0
                if self.tictactoe[num] == 0 or self.tictactoe[num] != actual_num:
                    break
                num +=3

                # If make all loops without fail
                if i == 2:
                    return "O" if self.playerone_turn else "X"

        
        # Check rows
        # Row num
        for y in range(3):
            num = y*3
            # X pos
            for i in range(3):
                actual_num = self.tictactoe[num]

                # Exit loop if 0
                if self.tictactoe[num] == 0 or self.tictactoe[num] != actual_num:
                    break

                num +=1

                # If make all loops without fail
                if i == 2:
                    return "O" if self.playerone_turn else "X"

        # Check diags manually
        if self.tictactoe[0] == self.tictactoe[4] == self.tictactoe[8] != 0:
            return "O" if self.playerone_turn else "X"
        if self.tictactoe[2] == self.tictactoe[4] == self.tictactoe[6] != 0:
            return "O" if self.playerone_turn else "X"        