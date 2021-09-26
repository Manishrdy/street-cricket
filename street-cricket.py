# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 09:43:42 2021

@author: Manish Reddy.
"""

import random
import time
import pandas as pd
import os
import glob
import shutil
import sys
from prettytable import PrettyTable

outcomes = [0, 1, 2, 3, 4, 6, 'OUT', 'Wide']
outList = ['Bowled', 'Caught', 'Run Out']
gameRate = 0.05 # seconds between balls

overs = 5
balls = 6

def prepInnings(team1, team2):
    
    with open(team1+'.txt') as team1Text:
        team1Players = team1Text.readlines()
    
    with open(team2+'.txt') as team2Text:
        team2Players = team2Text.readlines()
    
    for i in range(len(team1Players)):
        team1Players[i] = team1Players[i].replace('\n','')
    
    for i in range(len(team2Players)):
        team2Players[i] = team2Players[i].replace('\n','')
        
    t = PrettyTable([team1, team2])
    for i in range(len(team1Players)):
        t.add_row([team1Players[i], team2Players[i]])
    
    print('{}'.format(t).center(shutil.get_terminal_size().columns))
    print()
    print()
    
    print(team1+' first innings')
    print()
    
    onStrike = team1Players[0]
    offStrike = team2Players[1]
    
    onStrikeRuns = 0
    onStrikeBalls = 0
    onStrikeFours = 0
    onStrikeSixes = 0
    
    offStrikeRuns = 0
    offStrikeBalls = 0
    offStrikeFours = 0
    offStrikeSixes = 0
    
    totalBalls = 0
    initialBalls = 0
    
    totalWickets = 0
    initialWickets = 0
    
    totalWides = 0
    initialWides = 0
    
    initialScore = 0
    totalScore = 0
    
    bowlers = team2Players.copy()
    bowlerPresent = random.choice(bowlers)
    bowlers.remove(bowlerPresent)
    
    for over in range(overs):
        for ball in range(1,balls+1):
            # outcomes = [0, 1, 2, 3, 4, 6, 'OUT', 'Wide']
            ballOutcome = random.choices(outcomes,weights=(2,3,2.5,0.25,2,2,1,0.25),k=1)
            if ballOutcome == [0]:
                print('{}.{}  {} to {}, no runs'.format(over,ball,bowlerPresent,onStrike))
            elif ballOutcome == [1]:
                print('{}.{}  {} to {}, one run'.format(over,ball,bowlerPresent,onStrike))
            elif ballOutcome == [2]:
                print('{}.{}  {} to {}, two runs'.format(over,ball,bowlerPresent,onStrike))
            elif ballOutcome == [3]:
                print('{}.{}  {} to {}, three runs'.format(over,ball,bowlerPresent,onStrike))
            elif ballOutcome == [4]:
                print('{}.{}  {} to {}, FOUR'.format(over,ball,bowlerPresent,onStrike))
        print()
    
    

#Checking for teams data
os.chdir('./')
result = glob.glob( '*.txt' )
print('Avaliable teams: ',result)

for i in range(1):
    team1 = int(input("Enter team 1 index: "))
    team1 = result[team1 - 1].replace('.txt', '')
    team2 = int(input("Enter team 2 index: "))
    team2 = result[team2 - 1].replace('.txt', '')

print()
print('{}  vs {}'.format(team1, team2).center(shutil.get_terminal_size().columns))
print()

#toss options
toss = ['Heads','Tails']
tossChoice = random.choice(toss)

#2nd team toss call and generating random option (Away team choice)
#Dhoni spins the coin "Williamson choose tails".
tossCall = ['Heads', 'Tails']
team2Call = random.choice(tossCall)

#Generating toss
print('- x -'.center(shutil.get_terminal_size().columns))
print()
print('{} spins the coin'.format(team1))
print('{} - {} is the call. And its {}'.format(team2, team2Call, tossChoice))
# print(team1+" spins the coin \n"+team2+" - "+team2Call+" is the call. And it's "+tossChoice)

#Setting up who wont the toss and what they want to choose first.
firstChoice = ['Bat','Bowl']
firstChoiceCall = random.choice(firstChoice)
#Checking if team 2 toss call is same with coin toss or not
if team2Call == tossChoice:
    # print(team2+' won the toss and choose to '+firstChoiceCall+' first !')
    print('{} won the toss and choose to {} first !'.format(team2,firstChoiceCall))
    print()
    print('- x -'.center(shutil.get_terminal_size().columns))
    print()
    if firstChoiceCall == 'Bowl':
        team1, team2 = team1, team2
        prepInnings(team1, team2)

    elif firstChoiceCall == 'Bat':
        team1, team2 = team2, team1
        prepInnings(team1, team2)    
else:
    # print(team1+' won the toss and choose to '+firstChoiceCall+' first !')
    print('{} won the toss and choose to {} first !'.format(team1,firstChoiceCall))
    print()
    print('- x -'.center(shutil.get_terminal_size().columns))
    print()
    if firstChoiceCall == 'Bowl':
        team1, team2 = team2, team1
        prepInnings(team1, team2)

    elif firstChoiceCall == 'Bat':
        team1, team2 = team1, team2
        prepInnings(team1, team2)