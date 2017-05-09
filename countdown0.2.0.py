#! /usr/bin/python3

# LINUXPLORE - A game that demonstrates linux command-line knowledge!

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

# TODO: factor negative points upon answering challenge question incorrectly
# TODO: refactor score function
# TODO: Read and write to where several user accounts are saved to the userlist.json file
# TODO: Create mission2

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
    '''Should append username and points into empty global array users_list'''
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
                record.append(p)
                elapsedTime(start)
            else:
                print('Success! You have entered \'pwd\' for \'print working directory\'!')
                record.append(p)
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
                record.append(p)
                elapsedTime(start)
            else:
                print('Way to go!')
                record.append(p)
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
                record.append(p)
                elapsedTime(start)
            else:
                print('I see what you did there, and it\'s amazing!')
                record.append(p)
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
                    
        print('How would you access the root directory?')
        print('A).    cd root/')
        print('B).    cd ./')
        print('C).    cd ~/')
        challenge = input()
        if challenge.lower() == 'c':
            print('EUREKA!')
            record.append(p)
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
    
if __name__ == '__main__':
    
    print('Welcome to \'LINUXPLORE\''.center(40, '~') + '\n')
    userInfo()
    userAwait()
    countdownGame()
    
   
    
    
  
    

    
        
            
            
            
                        






