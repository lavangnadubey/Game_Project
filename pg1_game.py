def print_board():
    i=0
    while i!=9:
        print('{} {} {}'.format(board[i],board[i+1],board[i+2]))
        i+=3
def inp():
    c = 0
    while c != 1:
        loc = int(input('Enter location :'))
        if loc in cho:
            print("** ALready Filled ... Enter Again **")
        elif loc>9:
            print("** LOCATION NOT IN BOARD **")
        else:
            cho.append(loc)
            c = 1
            return loc

def play():
    for i in range(1,10):
        if i%2==0:
            print("Player {} :=: X".format(s_name))
            loc=inp()
            board[loc-1]='X'
            print_board()
            if check(): break
        else:
            print("Player {} :=: 0".format(f_name))
            loc=inp()
            board[loc-1] = '0'
            print_board()
            if check(): break
    else:
        print("** NOONE WINS ..TRY AGAIN.. **")


def check():
    if board[0]==board[4]==board[8]=='X' or board[2]==board[5]==board[8]=='X' or board[2]==board[4]==board[6]=='X' or board[3]==board[4]==board[5]=='X' or board[0]==board[1]==board[2]=='X' or board[6]==board[7]==board[8]=='X' or board[0]==board[3]==board[6]=='X' or board[1]==board[4]==board[7]=='X':
        print('** Hurah !! Player 2 won **')
        return True
    elif board[0]==board[4]==board[8]=='0' or board[2]==board[5]==board[8]=='0' or board[2]==board[4]==board[6]=='0' or board[3]==board[4]==board[5]=='0' or board[0]==board[1]==board[2]=='0' or board[6]==board[7]==board[8]=='0' or board[0]==board[3]==board[6]=='0' or board[1]==board[4]==board[7]=='0':
        print('** Hurah !! Player 1 won **')
        return True
    else:
        return False

cho=[]
ch='Y'

while(ch=='Y' or ch=='y'):
    f_name = input("Enter name of first player :")
    s_name = input("Enter name of second player :")
    print("The positions in the board are :")
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print_board()
    board = [".", ".", ".", ".", ".", ".", ".", ".", "."]
    play()
    board = [".", ".", ".", ".", ".", ".", ".", ".", "."]
    cho.clear()
    ch=input("Do you want to play again (Y/N)")
    if ch=='N' or cg=='n':
        print("!!! THANK YOU !!!")