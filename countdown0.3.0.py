#! /usr/bin/python3

# LINUXPLORE - A game that demonstrates linux command-line knowledge! - Tope Technologies (c. 2017)
# By Thomas Vilela and Christopher Short



# The program has been tested using a python3 IDLE shell, a cygwin bash, and a Debian 8/Linux bash
# This program will create folders into your directory if you are using a bash, including a .json file from the user input
# If there are any issues, feel free to do a pull request or e-mail me at thomasavilela@gmail.com with the report of bug
# HAVE FUN

import time, math, sys, os, pprint, re, json
from subprocess import call

# Globals

p = 'Points'
prompt = ['You are the sole remaining survivor on an abandoned space vessel after being attacked by beligerent Windows Users...', 'You have made haste to the nearest terminal that dismantles an escape craft...', 'The only catch is that you must maneuver through murky linux commands to find the unlocking mechanism!', 'You must use the Bourne-Again Shell (bash) and conjure any inkling of knowledge in order to proceed to the escape craft!', 'Thanks for boarding Elon Musk\'s Enceladus Cruise... have a great weekend.']
prompt_two = 'You have one minute before the atmosphere leaks into the vessel!'
mission1 = ['*CLICK*', '*WHIRRRRRRRRRRR*', '*WHOOOOOOSH!*', 'You have managed to board the escape craft; meagerly, you have waded through daunting command-lines. Next stop: Enceladus!']
users_list = {'Username': '', 'Points': 0}                                          # Contents for user data to keep track of user accounts and respective scores
record = []                                                                         # empty list that helps append 'Points' or remove 'Points' accordingly
response = ''
userDataFile = 'userData.json'

### Program addendums/notes:

# TODO: Syncronize midi sounds with prints of characters in list indices
# TODO: factor negative points upon answering challenge question incorrectly
# TODO: refactor score function
# TODO: Read and write to where several user accounts are saved to the userlist.json file
# TODO: Create mission2

# Functions/Modules

def elapsedTime(t):
    '''Keeps track of the time remaining for the player'''
    secondMinute = []
    elap = time.time() - t
    remain = 60 - round(elap)
    min_remain = remain / 60
    m = math.floor(min_remain)
    s = remain - (m * 60)
    secondMinute.append(m)
    secondMinute.append(s)
    if remain <= 0:
        print('Time has run out!\nGame Over!')
        sys.exit()
    print('\nYour remaining time is {0} minutes and {1} seconds'.format(secondMinute[0], secondMinute[1]))
    score = userUpdate(users_list, record)
    scoreDisplay(score)

def feedJson(user):
    '''
    Feeds users_list into function to display username and score at end of game
    Only saves current user; will program to save several users 
    '''
    s = json.dumps(user)
    with open(userDataFile, 'w') as f:
        f.write(s + '\n')
    f = open(userDataFile, 'r')
    s = f.readlines()
    user_string = ''
    for line in s:
        user_string += line.strip()
    final_user = json.loads(user_string)
    print(final_user)
              
def highScore():
    '''
    Currently lists the current user and score at end of game
    Should display the top 10 high scores loaded into a json file
    '''
    tableHeader = 'HIGHSCORE'.center(40, '=')
    print(tableHeader)
    tableLength = len(tableHeader)
    feedJson(users_list)

def scoreDisplay(userScore):
    '''After each question, function displays username and points'''
    for k, v in userScore.items():
        userScore.setdefault(k, 0)
        print(str(k) + ': ' + str(v))

def tryRemove():
    '''Will decrement points from user upon incorrect answers'''
    try:
        record.remove('Points')
    except ValueError:
        print('Oh no! No points!')

def userAwait():
    '''Menu that asks user if they are ready'''
    ready = input('Are you ready? (y/n) or \'q\' for quit\n')
    if ready == 'n':
        print('No problem...')
        userAwait()
    elif ready == 'y':
        for j in range(0, 3):
            print('. ', end='')
            time.sleep(0.5)
        countdownGame()
    elif ready == 'q':
        print('Okay, goodbye ' + str(users_list['Username']) + '\n')
        sys.exit()

def userContinue(t, r):
    '''Asks user if they want to try again'''
    if t == 0:
        print('You are out of tries! Continue? (y/n)')
        r = input()
        if r == 'y':
            userAwait()
            countdownGame()
        elif r == 'n':
            print('Thank you for playing!')
            sys.exit()
    if t > 0:
        for line in mission1:
            for char in line:
                print(char, end='')
                time.sleep(0.05)
            time.sleep(1)
            print('\n')
        print('Would you next to continue to the next mission? (y/n)')
        r = input()
        if r == 'y':
            sys.exit() # TODO
        elif r == 'n':
            print('Thank you for playing!')
            sys.exit()
                
#NOTE: Character cycle only works in Python IDLE Shell - it's a bug!

def userInfo():
    '''Should append username and points into empty global list users_list'''
    users_list['Username'] = input('\nType Username> ')    
    print('Greetings, ' + str(users_list['Username']) + '!')
    print('Your score is ' + str(users_list['Points']))
    for prompts in prompt:
        for char in prompts:
            print(char, end='')
            time.sleep(0.05)
        time.sleep(4)
        print('\n')

def userUpdate(player, factor):
    '''Adds to record list and adds contents to users_list dictionary'''
    tmp = player
    for i in factor:
        tmp.setdefault(i, 0)
        tmp[i] += 1
    return tmp
   
# Game module
def countdownGame():
    '''Module with questions and function calls'''
    response = ''
    start = time.time()
    print(prompt_two)
    turn = 3
    challenge = ''
    while turn > 0:

# View the current working directory (Question 1)

        print('Which choice selects the \'Print Working Directory\'?')
        print('A).    cd')
        print('B).    ls')
        print('C).    pwd')
        challenge = input()
        if challenge.lower() == 'c':
            try:
                call(["pwd"])
            except FileNotFoundError:
                print('Success! You have entered \'pwd\' for \'print working directory\'!')
                elapsedTime(start)
            else:
                print('Success! You have entered \'pwd\' for \'print working directory\'!')
                elapsedTime(start)
        else:
            turn -= 1
            if turn == 0:
                userContinue(turn, response)
            else:
                if turn == 1:
                    print('Please try again. You have ' + str(turn) + ' try remaining!')
                    tryRemove()
                    elapsedTime(start)
                    continue
                else:
                    print('Please try again. You have ' + str(turn) + ' tries remaining!')
                    tryRemove()
                    elapsedTime(start)
                    continue

# View the amount of memory used on the system (Question 2)
                
        print('Which command allows the user to view the amount of used memory on the system?')
        print('A).    df')
        print('B).    free')
        print('C).    apropos')
        challenge = input()
        if challenge.lower() == 'b':
            try:
                call(["free"])
            except FileNotFoundError:
                print('Way to go!\n')
                elapsedTime(start)
            else:
                print('Way to go!')
                elapsedTime(start)
        else:
            turn -= 1
            if turn == 0:
                userContinue(turn, response)
            else:
                if turn == 1:
                    print('Please try again. You have ' + str(turn) + ' try remaining!')
                    tryRemove()
                    elapsedTime(start)
                    continue
                else:
                    print('Please try again.\nYou have ' + str(turn) + ' tries remaining!')
                    tryRemove()
                    elapsedTime(start)
                    continue

# View the long option for directory contents/files (Question 3)

        print('Which option allows the user to view extra details concerning the list of contents within the working directory?')
        print('A).    -h')
        print('B).    -i')
        print('C).    -l')
        challenge = input()
        if challenge.lower() == 'c':
            try:
                call(["ls", "-l"])
            except FileNotFoundError:
                print('I see what you did there, and it\'s amazing!')
                elapsedTime(start)
            else:
                print('I see what you did there, and it\'s amazing!')
                elapsedTime(start)
        else:
            turn -= 1
            if turn == 0:
                userContinue(turn, response)
            else:
                if turn == 1:
                    print('Please try again. You have ' + str(turn) + ' try remaining!')
                    tryRemove()
                    elapsedTime(start)
                    continue
                else:
                    print('Please try again.\nYou have ' + str(turn) + ' tries remaining!')
                    tryRemove()
                    elapsedTime(start)
                    continue

# View used memory on system (Question 4)
                
        print('Which terminal command will retrieve and install the system upgrade?')
        print('A).    sudo get-apt update')
        print('B).    sudo apt get-install update')
        print('C).    sudo apt-get update')
        challenge = input()
        if challenge.lower() == 'c':
            try:
                call(["sudo", "apt-get", "update"])
            except FileNotFoundError:
                print('Success! You updated the current system')
                elapsedTime(start)
            else:
                print('Success! You updated the current system')
                elapsedTime(start)
        else:
            turn -= 1
            if turn == 0:
                userContinue(turn, response)
            else:
                if turn == 1:
                    print('Please try again. You have ' + str(turn) + ' try remaining!')
                    tryRemove()
                    elapsedTime(start)
                    continue
                else:
                    print('Please try again.\nYou have ' + str(turn) + ' tries remaining!')
                    tryRemove()
                    elapsedTime(start)
                    continue

# Create a directory within the working directory (Question 5)

        print('How would you create a directory named "banana" within the working directory?')
        print('A).    mkdir banana -dir')
        print('B).    mkdir banana')
        print('C).    create banana')
        challenge = input()
        if challenge.lower() == 'b':
            try:
                call(["mkdir", "banana"])
            except FileNotFoundError:
                print('Success! You created the directory named \'banana\'!')
                elapsedTime(start)
            else:
                print('Success! You created the directory named \'banana\'!')
                elapsedTime(start)
        else:
            turn -= 1
            if turn == 0:
                userContinue(turn, response)
            else:
                if turn == 1:
                    print('Please try again. You have ' + str(turn) + ' try remaining!')
                    tryRemove()
                    elapsedTime(start)
                    continue
                else:
                    print('Please try again.\nYou have ' + str(turn) + ' tries remaining!')
                    tryRemove()
                    elapsedTime(start)
                    continue
                
# Change the name of a directory within the working directory (Question 6)

        print('How would you rename a directory "banana" to "apple" within the working directory?')
        print('A).    -append banana apple')
        print('B).    rename banana apple')
        print('C).    mv banana apple')
        challenge = input()
        if challenge.lower() == 'b':
            try:
                call(["rename", "banana", "apple"])
            except FileNotFoundError:
                print('The directory \'banana\' is now named \'apple\'!')
                elapsedTime(start)
            else:
                print('The directory \'banana\' is now named \'apple\'!')
                elapsedTime(start)
        else:
            turn -= 1
            if turn == 0:
                userContinue(turn, response)
            else:
                if turn == 1:
                    print('Please try again. You have ' + str(turn) + ' try remaining!')
                    tryRemove()
                    elapsedTime(start)
                    continue
                else:
                    print('Please try again.\nYou have ' + str(turn) + ' tries remaining!')
                    tryRemove()
                    elapsedTime(start)
                    continue

# Copy all contents of a folder to another (Question 7)

            print('How would copy all the files within /home/apple to /home/orange?')
            print('A).    cp -R /home/apple/* /home/orange')
            print('B).    copy* /home/banana /home/apple')
            print('C).    mv /home/banana /home/apple')
            challenge = input()
            if challenge.lower() == 'a':
                try:
                    call(["cp", "-R", "/home/apple/*", "/home/orange"])
                except FileNotFoundError:
                    print('Good job, slick - you have copied the \'apple\' directory into the \'orange\' directory!')
                    elapsedTime(start)
                else:
                    print('Good job, slick - you have copied the \'apple\' directory into the \'orange\' directory!')
                    elapsedTime(start)
            else:
                turn -= 1
                if turn == 0:
                    userContinue(turn, response)
                else:
                    if turn == 1:
                        print('Please try again. You have ' + str(turn) + ' try remaining!')
                        tryRemove()
                        elapsedTime(start)
                        continue
                    else:
                        print('Please try again.\nYou have ' + str(turn) + ' tries remaining!')
                        tryRemove()
                        elapsedTime(start)
                        continue

# Access the root directory for the user (Question 8) - LAST QUESTION TO MISSION 1
                
        print('How would you access the root directory?')
        print('A).    cd root/')
        print('B).    cd ./')
        print('C).    cd ~/')
        challenge = input()
        if challenge.lower() == 'c':
            print('EUREKA!')
            elapsedTime(start)
            print('You win!')
            highScore()
            userContinue(turn, response)
        else:
            turn -= 1
            if turn == 0:
                userContinue(turn, response)
            else:
                if turn == 1:
                    print('Please try again. You have ' + str(turn) + ' try remaining!')
                    tryRemove()
                    elapsedTime(start)
                    continue
                else:
                    print('Please try again. You have ' + str(turn) + ' tries remaining!')
                    tryRemove()
                    elapsedTime(start)
                    continue

# Main

if __name__ == '__main__':
    
    print('Welcome to \'LINUXPLORE\''.center(40, '~') + '\n')
    userInfo()
    userAwait()
    countdownGame()
    
   
    
    
  
    

    
        
            
            
            
                        






