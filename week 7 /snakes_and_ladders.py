from PIL import Image
import random

end = 100

def show():
    img = Image.open("snakesladders-nationalseriesgames.jpg")
    img.show()

def play():

    #input player 1 name
    ply_1 = input("Player 1, Enter your name : ")

    #input player 2 name
    ply_2 = input("PLayer 2, Enter your name : ")

    #player 1 initial point
    pp1 = 0

    #player 2 initial point 
    pp2 = 0

    turn = 0

    while(1):
        if turn%2 == 0:
            #player 1 turn
            print(ply_1," your turn") 

            # ask player choice to continue
            c = int(input("Press 1 for continue ,0 for quit"))
            if c == 0:
                print(ply_1," scored ",pp1)
                print(ply_2," scored ",pp2)
                print('Quiting the game, Thanks for playing ')
                break
            dice = random.randint(1,6) 
            print('Dice showed 'dice)

            pp1 += dice
            pp1 = checkladder(pp1)
            pp1 = check_snake(pp1)

            # check if the player goes beyond the board

            if pp1 > end:
                pp1 = end

            print(ply_1, ' Your score: ',pp1)

            if reached_end(pp1):
                print(ply_1, ' Won')
                break
        else:
            #player 2 turn
            print(ply_2," your turn") 

            # ask player choice to continue
            c = int(input("Press 1 for continue ,0 for quit"))
            if c == 0:
                print(ply_1," scored ",pp1)
                print(ply_2," scored ",pp2)
                print('Quiting the game, Thanks for playing ')
                break
            dice = random.randint(1,6) 
            print('Dice showed 'dice)

            pp2 += dice
            pp2 = checkladder(pp2)
            pp2 = check_snake(pp2)

            # check if the player goes beyond the board

            if pp1 > end:
                pp1 = end

            print(ply_2, ' Your score: ',pp2)

            if reached_end(pp2):
                print(ply_2, ' Won')
                break