import random 

# 2 users
human_user = 0
computer_user = 0

options = ['rock','paper','scissors']

while True:
    human_input = input('type rock/paper/scissors or Q to quit.').lower()
    if human_input == 'q':
        break

    if human_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock=0, paper=1, scissors=2 

    computer_pick = options[random_number]
    print('computer picked', computer_pick + '.')

    #compering human choice and computer choice 
    if human_input == 'rock' and computer_pick == 'scissors':
        print('you won!')
        human_user += 1
       
    elif human_input == 'paper' and computer_pick == 'rock':
        print('you won!')
        human_user += 1
       
    elif human_input == "scissors" and computer_pick == 'paper':
        print('you won!')
        human_user += 1
    else:
        print('you lost!')
        computer_user += 1


print('you won ', human_user, 'times')
print('the computer won ', computer_user, 'times')                  
print('byebye!')    




