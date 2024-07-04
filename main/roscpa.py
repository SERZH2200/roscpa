from random import *

options=['ножницы','камень','бумага']
computer_wins=0
your_wins=0

while True:
    player_input=input('chose камень/ножницы/бумага or q to quit')

    if player_input=='q':
        break
    
    if player_input not in options:
        continue


    random_num = randint(0,2)
    comp_pick = options[random_num]

    print("Computer picked", comp_pick + ".")

    if player_input=='камень' and comp_pick=='ножницы':
        your_wins+=1
        print('YOU WON')
    
    elif player_input=='бумага' and comp_pick=='камень':
        your_wins+=1
        print('YOU WON')

    elif player_input=='ножницы' and comp_pick=='бумага':
        your_wins+=1
        print('YOU WON')

    elif player_input==comp_pick:
        print('DRAW')
    else:
        computer_wins+=1
        print('YOU LOST')

print("You won", your_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
