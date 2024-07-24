import random

l = ["rock", "scissor", "paper"]

'''
rock vs paper -> paper wins
rock vs scissor -> rock wins
paper vs scissor -> scissor wins
'''

while True:
    ucount = 0
    count = 0

    uc = int(input('''
Game Start.....
1 Yes
2 No | Exit
    '''))

    if uc == 1:
        for _ in range(5):
            userInput = int(input('''
1 Rock
2 Scissor
3 Paper
    '''))

            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                uchoice = "scissor"
            elif userInput == 3:
                uchoice = "paper"
            else:
                print("Invalid input, please try again.")
                continue

            Cchoice = random.choice(l)
            print("Computer Value: ", Cchoice)
            print("User Value: ", uchoice)

            if Cchoice == uchoice:
                print("Game Draw")
            elif (uchoice == "rock" and Cchoice == "scissor") or \
                 (uchoice == "scissor" and Cchoice == "paper") or \
                 (uchoice == "paper" and Cchoice == "rock"):
                print("You win")
                ucount += 1
            else:
                print("Computer wins")
                count += 1

        if ucount == count:
            print("Final Game Draw.....")
        elif ucount > count:
            print("Final You Win The Game.....")
        else:
            print("Final Computer Wins The Game.....")
            
        print("User Score: ", ucount)
        print("Computer Score: ", count)
    else:
        break
