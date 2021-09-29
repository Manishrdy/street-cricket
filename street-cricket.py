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
import io

#Creating arrays for 4's and 6's
zeroComm = []
oneComm = []
twoComm = []
threeComm = []
fourComm = []
sixComm = []
outComm = []
batsmenScoreboard1 = []
batsmenScoreboard2 = []

file = io.open('./commentry/0.txt','r',encoding="utf8")
for i in file.readlines():
    zeroComm.append(i)

for i in range(len(zeroComm)):
    zeroComm[i] = zeroComm[i].replace('\n','')
    
file = io.open('./commentry/1.txt','r',encoding="utf8")
for i in file.readlines():
    oneComm.append(i)

for i in range(len(oneComm)):
    oneComm[i] = oneComm[i].replace('\n','')

file = io.open('./commentry/2.txt','r',encoding="utf8")
for i in file.readlines():
    twoComm.append(i)

for i in range(len(twoComm)):
    twoComm[i] = twoComm[i].replace('\n','')
    
file = io.open('./commentry/3.txt','r',encoding="utf8")
for i in file.readlines():
    threeComm.append(i)

for i in range(len(threeComm)):
    threeComm[i] = threeComm[i].replace('\n','')

file = io.open('./commentry/4.txt','r',encoding="utf8")
for i in file.readlines():
    fourComm.append(i)

for i in range(len(fourComm)):
    fourComm[i] = fourComm[i].replace('\n','')
    
file = io.open('./commentry/6.txt','r',encoding="utf8")
for i in file.readlines():
    sixComm.append(i)

for i in range(len(sixComm)):
    sixComm[i] = sixComm[i].replace('\n','')
    
file = io.open('./commentry/out.txt','r',encoding="utf8")
for i in file.readlines():
    outComm.append(i)

for i in range(len(outComm)):
    outComm[i] = outComm[i].replace('\n','')

outcomes = [0, 1, 2, 3, 4, 6, 'OUT']
outList = ['Bowled', 'Caught', 'Run Out']
gameRate = 0.05 # seconds between balls

overs = 5
balls = 6

oneInnBat = PrettyTable(['Batsmen',' ','Fielder','Bowler','Runs','Balls','4s','6s','SR'])
oneIngBowl = PrettyTable(['Bowler', 'Overs', 'Dots', 'Runs', 'Wickets', 'Economy'])
twoIngBat = PrettyTable(['Batsmen',' ','Fielder','Bowler','Runs','Balls','4s','6s','SR'])
twoIngBowl = PrettyTable(['Bowler', 'Overs', 'Dots', 'Runs', 'Wickets', 'Economy'])


def checkWinner(over, ball, totalScore, totalWickets, target):
    team1Score = target - 1
    
    if totalScore == target or totalScore > target:
        wicketsWon = 5 - totalWickets
        print()
        print('     '+team1+' won by '+str(wicketsWon)+' wickets.')
        return True
    elif over == 4 and ball == 6:
        if totalScore < target-1:
            print()
            runsWon = target - totalScore - 1
            print('     '+team1+' won by '+str(runsWon)+' runs')
            return True
        if totalScore == target-1:
            print()
            print('     Draw Match')
            return True
    

def prepInnings2(team1, team2, target):
    
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
    
    print()
    print()
    
    print(team1+' Second innings')
    print()
    
    onStrike = team1Players[0]
    offStrike = team1Players[1]
    
    onStrikeRuns = 0
    onStrikeBalls = 0
    onStrikeFours = 0
    onStrikeSixes = 0
    
    offStrikeRuns = 0
    offStrikeBalls = 0
    offStrikeFours = 0
    offStrikeSixes = 0
    
    
    initialBalls = 0
    
    totalWickets = 0
    initialWickets = 0
    
    totalWides = 0
    initialWides = 0
    
    totalDotBalls = 0
    initialDotBalls = 0
    
    initialScore = 0
    totalScore = 0
    
    bowlers = team2Players.copy()
    bowlerPresent = random.choice(bowlers)
    bowlers.remove(bowlerPresent)
    
    for over in range(overs):
        for ball in range(1,balls+1):
            check = checkWinner(over, ball, totalScore, totalWickets, target)
            if check == True:
                break
            # outcomes = [0, 1, 2, 3, 4, 6, 'OUT', 'Wide']
            ballOutcome = random.choices(outcomes,weights=(2,3,2.5,0.25,2,2,0.85),k=1)
            initialBalls = initialBalls + 1
            onStrikeBalls = onStrikeBalls + 1
            
            if over == 0 and ball == 1:
                if ballOutcome == ['OUT']:
                    print('{}.{}  {} to {}, OUT !, The batsmen isnt happy and its declared as a trail ball'.format(over,ball,bowlerPresent,onStrike))
                    ballOutcome = [0]
                    continue
                    
            
            if ballOutcome == [0]:
                initialDotBalls = initialDotBalls + 1
                totalDotBalls = totalDotBalls + 1
                initialScore = initialScore + 0
                totalScore = totalScore + 0
                
                onStrikeRuns = onStrikeRuns + 0
                
                
                print('{}.{}  {} to {}, no runs, {}'.format(over,ball,bowlerPresent,onStrike, random.choice(zeroComm)))
                
                if ball == 6:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRuns,offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRuns,offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                    
            elif ballOutcome == [1]:
                initialDotBalls = initialDotBalls + 0
                initialScore = initialScore + 1
                totalScore = totalScore + 1
                
                onStrikeRuns = onStrikeRuns + 1
                
                
                print('{}.{}  {} to {}, one run, {}'.format(over,ball,bowlerPresent,onStrike, random.choice(oneComm)))
                
                if ball == 6:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRuns,offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                else:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRuns,offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                    
            elif ballOutcome == [2]:
                initialDotBalls = initialDotBalls + 0
                initialScore = initialScore + 2
                totalScore = totalScore + 2
                
                onStrikeRuns = onStrikeRuns + 2
                
                
                print('{}.{}  {} to {}, two runs, {}'.format(over,ball,bowlerPresent,onStrike, random.choice(twoComm)))
                
                if ball == 6:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRuns,offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRuns,offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                
            elif ballOutcome == [3]:
                initialDotBalls = initialDotBalls + 0
                initialScore = initialScore + 3
                totalScore = totalScore + 3
                
                onStrikeRuns = onStrikeRuns + 3
                
                
                print('{}.{}  {} to {}, three runs, {}'.format(over,ball,bowlerPresent,onStrike, random.choice(threeComm)))
                
                if ball == 6:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRuns,offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                else:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRuns,offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                
            elif ballOutcome == [4]:
                initialDotBalls = initialDotBalls + 0
                initialScore = initialScore + 4
                totalScore = totalScore + 4
                
                onStrikeRuns = onStrikeRuns + 4
                
                onStrikeFours = onStrikeFours + 1
                
                print('{}.{}  {} to {}, FOUR, {}'.format(over,ball,bowlerPresent,onStrike, random.choice(fourComm)))
                
                if ball == 6:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRuns,offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRuns,offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                
            elif ballOutcome == [6]:
                initialDotBalls = initialDotBalls + 0
                initialScore = initialScore + 6
                totalScore = totalScore + 6
                
                onStrikeRuns = onStrikeRuns + 6
                
                onStrikeSixes = onStrikeSixes + 1
                
                print('{}.{}  {} to {}, SIX, {}'.format(over,ball,bowlerPresent,onStrike,random.choice(sixComm)))
                
                if ball == 6:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRuns,offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRuns,offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                
            elif ballOutcome == ['OUT']:
                # oneInnBat = PrettyTable(['Batsmen',' ','Fielder','Bowler','Runs','Balls','4s','6s','SR'])
                outType = random.choices(outList,weights=(1,1,0.45),k=1)
                # outList = ['Bowled', 'Caught', 'Run Out']
                if outType == ['Bowled']:
                    
                    
                    totalDotBalls = totalDotBalls + 1
                    initialDotBalls = initialDotBalls + 1
                    
                    initialWickets = initialWickets + 1
                    totalWickets = totalWickets + 1
                    
                    print('{}.{}  {} to {}, Bowled !, {}'.format(over,ball,bowlerPresent,onStrike, random.choice(outComm)))
                    print()
                    print('     b. {}     {}({}){} [{}x4, {}x6]'.format(bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                    print()
                    
                    sr = (onStrikeRuns/onStrikeBalls)*100
                    twoIngBat.add_row([onStrike,'b.','',bowlerPresent,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes,round(sr,2)])
                    onStrike = team1Players[totalWickets+1]
                    if ball == 6:
                        onStrike, offStrike = offStrike, onStrike
                        onStrikeRuns,offStrikeRuns = offStrikeRuns, onStrikeRuns
                        onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                        onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                        onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                    else:
                        onStrike, offStrike = onStrike, offStrike
                        onStrikeRuns,offStrikeRuns = onStrikeRuns, offStrikeRuns
                        onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                        onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                        onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                    
                elif outType == ['Caught']:
                    
                    totalDotBalls = totalDotBalls + 1
                    initialDotBalls = initialDotBalls + 1
                    initialWickets = initialWickets + 1
                    totalWickets = totalWickets + 1
                    outPlayer = random.choice(team2Players)
                    
                    print('{}.{}  {} to {}, Caught by {}, {}'.format(over,ball,bowlerPresent,onStrike,outPlayer, random.choice(outComm)))
                    print()
                    print('     c. {}     b. {}     {}({}){} [{}x4, {}x6]'.format(outPlayer,bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                    print()
                    
                    sr = (onStrikeRuns/onStrikeBalls)*100
                    twoIngBat.add_row([onStrike,'c.',outPlayer,bowlerPresent,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes,round(sr,2)])
                    onStrike = team1Players[totalWickets+1]
                    if ball == 6:
                        onStrike, offStrike = offStrike, onStrike
                        onStrikeRuns,offStrikeRuns = offStrikeRuns, onStrikeRuns
                        onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                        onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                        onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                    else:
                        onStrike, offStrike = onStrike, offStrike
                        onStrikeRuns,offStrikeRuns = onStrikeRuns, offStrikeRuns
                        onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                        onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                        onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes    
                
                elif outType == ['Run Out']:
                    
                    totalDotBalls = totalDotBalls + 1
                    initialDotBalls = initialDotBalls + 1
                    initialWickets = initialWickets + 1
                    totalWickets = totalWickets + 1
                    outPlayer = random.choice(team2Players)
                    
                    print('{}.{}  {} to {}, Run Out by {}, Direct hit and he is gone'.format(over,ball,bowlerPresent,onStrike,outPlayer))
                    print()
                    print('     ro. {}     b. {}     {}({}){} [{}x4, {}x6]'.format(outPlayer,bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                    print()
                    
                    sr = (onStrikeRuns/onStrikeBalls)*100
                    twoIngBat.add_row([onStrike,'ro.',outPlayer,bowlerPresent,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes,round(sr,2)])
                    onStrike = team1Players[totalWickets+1]
                    if ball == 6:
                        onStrike, offStrike = offStrike, onStrike
                        onStrikeRuns,offStrikeRuns = offStrikeRuns, onStrikeRuns
                        onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                        onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                        onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                    else:
                        onStrike, offStrike = onStrike, offStrike
                        onStrikeRuns,offStrikeRuns = onStrikeRuns, offStrikeRuns
                        onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                        onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                        onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                
                onStrikeBalls = 0
                onStrikeFours = 0
                onStrikeRuns = 0
                onStrikeSixes = 0
                
                # if totalWickets < 4:
                #     onStrike = team1Players[totalWickets+1]
                if totalWickets == 4:
                    onStrike = offStrike
                elif totalWickets == 5:
                    if onStrikeBalls == 0:
                        sr = 0
                    else:
                        sr = (onStrikeRuns/onStrikeBalls)*100
                    twoIngBat.add_row([onStrike,'Not Out','','',onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes,round(sr,2)])
                    
                    b = str(over)+'.'+str(ball)
                    rr = totalScore / int(b)
                    break
                    
            if totalWickets == 4:
                onStrikeRuns = offStrikeRuns
                onStrikeBalls = offStrikeBalls
                onStrikeFours = offStrikeFours
                onStrikeSixes =  offStrikeSixes
                    
        print()
        if over == 4:
            if onStrikeBalls == 0:
                sr1 = 0
            else:
                sr1 = (onStrikeRuns/onStrikeBalls)*100
            twoIngBat.add_row([onStrike,'Not Out','','',onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes,round(sr1,2)])
            
            if totalWickets != 4:
                sr2 = (offStrikeRuns/offStrikeBalls)*100
                twoIngBat.add_row([offStrike,'Not Out','','',offStrikeRuns,offStrikeBalls,offStrikeFours,offStrikeSixes,round(sr2,2)])
            
            economy = initialScore / 1
            twoIngBowl.add_row([bowlerPresent, 1, initialDotBalls, initialScore, 
                               initialWickets, round(economy,2)])
            b = '5.0'
            rr = totalScore / 5
            continue
        else:
            economy = initialScore / 1
            twoIngBowl.add_row([bowlerPresent, 1, initialDotBalls, initialScore, 
                               initialWickets, round(economy,2)])
            
            print('     End of over {}.{}'.format(over,ball))
            print('     {}     {}/{}'.format(team1,totalScore,totalWickets))
            rr_new = totalScore/(over+1)
            print('     RR.     {}'.format(round(rr_new,2)))
            
            print()
            print('     {}     ({}){}* [{}x4,{}x6]'.format(onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
            print('     {}     ({}){}* [{}x4,{}x6]'.format(offStrike,offStrikeRuns,offStrikeBalls,offStrikeFours,offStrikeSixes))
            print('     {}     1.0-{}-{}-{}'.format(bowlerPresent,initialDotBalls,initialScore,initialWickets))
            print()
            
            bowlerPresent = random.choice(bowlers)
            bowlers.remove(bowlerPresent)
            
            initialScore = 0
            initialDotBalls = 0
    
        o = str(over)+'.'+str(ball)

    print(twoIngBat)
    print(twoIngBowl)
    twoIngTotal = PrettyTable(['Total', 'Overs', 'Run Rate', 'Extras'])
    twoIngTotal.add_row([totalScore,o,rr,0])
    print(twoIngTotal)

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
    offStrike = team1Players[1]
    
    onStrikeRuns = 0
    onStrikeBalls = 0
    onStrikeFours = 0
    onStrikeSixes = 0
    
    offStrikeRuns = 0
    offStrikeBalls = 0
    offStrikeFours = 0
    offStrikeSixes = 0
    
    
    initialBalls = 0
    
    totalWickets = 0
    initialWickets = 0
    
    totalWides = 0
    initialWides = 0
    
    totalDotBalls = 0
    initialDotBalls = 0
    
    initialScore = 0
    totalScore = 0
    
    bowlers = team2Players.copy()
    bowlerPresent = random.choice(bowlers)
    bowlers.remove(bowlerPresent)
    
    for over in range(overs):
        for ball in range(1,balls+1):
            # outcomes = [0, 1, 2, 3, 4, 6, 'OUT', 'Wide']
            ballOutcome = random.choices(outcomes,weights=(2,3,2.5,0.25,2,2,0.85),k=1)
            initialBalls = initialBalls + 1
            onStrikeBalls = onStrikeBalls + 1
            
            if over == 0 and ball == 1:
                if ballOutcome == ['OUT']:
                    print('{}.{}  {} to {}, OUT !, The batsmen isnt happy and its declared as a trail ball'.format(over,ball,bowlerPresent,onStrike))
                    ballOutcome = [0]
                    continue
                    
            
            if ballOutcome == [0]:
                initialDotBalls = initialDotBalls + 1
                totalDotBalls = totalDotBalls + 1
                initialScore = initialScore + 0
                totalScore = totalScore + 0
                
                onStrikeRuns = onStrikeRuns + 0
                
                
                print('{}.{}  {} to {}, no runs, {}'.format(over,ball,bowlerPresent,onStrike, random.choice(zeroComm)))
                
                if ball == 6:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRuns,offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRuns,offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                    
            elif ballOutcome == [1]:
                initialDotBalls = initialDotBalls + 0
                initialScore = initialScore + 1
                totalScore = totalScore + 1
                
                onStrikeRuns = onStrikeRuns + 1
                
                
                print('{}.{}  {} to {}, one run, {}'.format(over,ball,bowlerPresent,onStrike, random.choice(oneComm)))
                
                if ball == 6:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRuns,offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                else:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRuns,offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                    
            elif ballOutcome == [2]:
                initialDotBalls = initialDotBalls + 0
                initialScore = initialScore + 2
                totalScore = totalScore + 2
                
                onStrikeRuns = onStrikeRuns + 2
                
                
                print('{}.{}  {} to {}, two runs, {}'.format(over,ball,bowlerPresent,onStrike, random.choice(twoComm)))
                
                if ball == 6:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRuns,offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRuns,offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                
            elif ballOutcome == [3]:
                initialDotBalls = initialDotBalls + 0
                initialScore = initialScore + 3
                totalScore = totalScore + 3
                
                onStrikeRuns = onStrikeRuns + 3
                
                
                print('{}.{}  {} to {}, three runs, {}'.format(over,ball,bowlerPresent,onStrike, random.choice(threeComm)))
                
                if ball == 6:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRuns,offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                else:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRuns,offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                
            elif ballOutcome == [4]:
                initialDotBalls = initialDotBalls + 0
                initialScore = initialScore + 4
                totalScore = totalScore + 4
                
                onStrikeRuns = onStrikeRuns + 4
                
                onStrikeFours = onStrikeFours + 1
                
                print('{}.{}  {} to {}, FOUR, {}'.format(over,ball,bowlerPresent,onStrike, random.choice(fourComm)))
                
                if ball == 6:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRuns,offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRuns,offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                
            elif ballOutcome == [6]:
                initialDotBalls = initialDotBalls + 0
                initialScore = initialScore + 6
                totalScore = totalScore + 6
                
                onStrikeRuns = onStrikeRuns + 6
                
                onStrikeSixes = onStrikeSixes + 1
                
                print('{}.{}  {} to {}, SIX, {}'.format(over,ball,bowlerPresent,onStrike, random.choice(sixComm)))
                
                if ball == 6:
                    onStrike, offStrike = offStrike, onStrike
                    onStrikeRuns,offStrikeRuns = offStrikeRuns, onStrikeRuns
                    onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                    onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                    onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                else:
                    onStrike, offStrike = onStrike, offStrike
                    onStrikeRuns,offStrikeRuns = onStrikeRuns, offStrikeRuns
                    onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                    onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                    onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                
            elif ballOutcome == ['OUT']:
                # oneInnBat = PrettyTable(['Batsmen',' ','Fielder','Bowler','Runs','Balls','4s','6s','SR'])
                outType = random.choices(outList,weights=(1,1,0.45),k=1)
                # outList = ['Bowled', 'Caught', 'Run Out']
                if outType == ['Bowled']:
                    
                    
                    totalDotBalls = totalDotBalls + 1
                    initialDotBalls = initialDotBalls + 1
                    
                    initialWickets = initialWickets + 1
                    totalWickets = totalWickets + 1
                    
                    print('{}.{}  {} to {}, Bowled !, {}'.format(over,ball,bowlerPresent,onStrike, random.choice(outComm)))
                    print()
                    print('     b. {}     {}({}){} [{}x4, {}x6]'.format(bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                    print()
                    
                    sr = (onStrikeRuns/onStrikeBalls)*100
                    oneInnBat.add_row([onStrike,'b.','',bowlerPresent,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes,round(sr,2)])
                    onStrike = team1Players[totalWickets+1]
                    if ball == 6:
                        onStrike, offStrike = offStrike, onStrike
                        onStrikeRuns,offStrikeRuns = offStrikeRuns, onStrikeRuns
                        onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                        onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                        onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                    else:
                        onStrike, offStrike = onStrike, offStrike
                        onStrikeRuns,offStrikeRuns = onStrikeRuns, offStrikeRuns
                        onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                        onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                        onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                    
                elif outType == ['Caught']:
                    
                    totalDotBalls = totalDotBalls + 1
                    initialDotBalls = initialDotBalls + 1
                    initialWickets = initialWickets + 1
                    totalWickets = totalWickets + 1
                    outPlayer = random.choice(team2Players)
                    
                    print('{}.{}  {} to {}, Caught by {}, {}'.format(over,ball,bowlerPresent,onStrike,outPlayer, random.choice(outComm)))
                    print()
                    print('     c. {}     b. {}     {}({}){} [{}x4, {}x6]'.format(outPlayer,bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                    print()
                    
                    sr = (onStrikeRuns/onStrikeBalls)*100
                    oneInnBat.add_row([onStrike,'c.',outPlayer,bowlerPresent,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes,round(sr,2)])
                    onStrike = team1Players[totalWickets+1]
                    if ball == 6:
                        onStrike, offStrike = offStrike, onStrike
                        onStrikeRuns,offStrikeRuns = offStrikeRuns, onStrikeRuns
                        onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                        onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                        onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                    else:
                        onStrike, offStrike = onStrike, offStrike
                        onStrikeRuns,offStrikeRuns = onStrikeRuns, offStrikeRuns
                        onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                        onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                        onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes    
                
                elif outType == ['Run Out']:
                    
                    totalDotBalls = totalDotBalls + 1
                    initialDotBalls = initialDotBalls + 1
                    initialWickets = initialWickets + 1
                    totalWickets = totalWickets + 1
                    outPlayer = random.choice(team2Players)
                    
                    print('{}.{}  {} to {}, Run Out by {}, Thats a direct hit and the stone is broken !'.format(over,ball,bowlerPresent,onStrike,outPlayer))
                    print()
                    print('     ro. {}     b. {}     {}({}){} [{}x4, {}x6]'.format(outPlayer,bowlerPresent,onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
                    print()
                    
                    sr = (onStrikeRuns/onStrikeBalls)*100
                    oneInnBat.add_row([onStrike,'ro.',outPlayer,bowlerPresent,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes,round(sr,2)])
                    onStrike = team1Players[totalWickets+1]
                    if ball == 6:
                        onStrike, offStrike = offStrike, onStrike
                        onStrikeRuns,offStrikeRuns = offStrikeRuns, onStrikeRuns
                        onStrikeBalls, offStrikeBalls = offStrikeBalls, onStrikeBalls
                        onStrikeFours, offStrikeFours = offStrikeFours, onStrikeFours
                        onStrikeSixes, offStrikeSixes = offStrikeSixes, onStrikeSixes
                    else:
                        onStrike, offStrike = onStrike, offStrike
                        onStrikeRuns,offStrikeRuns = onStrikeRuns, offStrikeRuns
                        onStrikeBalls, offStrikeBalls = onStrikeBalls, offStrikeBalls
                        onStrikeFours, offStrikeFours = onStrikeFours, offStrikeFours
                        onStrikeSixes, offStrikeSixes = onStrikeSixes, offStrikeSixes
                
                onStrikeBalls = 0
                onStrikeFours = 0
                onStrikeRuns = 0
                onStrikeSixes = 0
                
                # if totalWickets < 4:
                #     onStrike = team1Players[totalWickets+1]
                if totalWickets == 4:
                    onStrike = offStrike
                elif totalWickets == 5:
                    if onStrikeBalls == 0:
                        sr = 0
                    else:
                        sr = (onStrikeRuns/onStrikeBalls)*100
                    oneInnBat.add_row([onStrike,'Not Out','','',onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes,round(sr,2)])
                    
                    b = str(over)+'.'+str(ball)
                    rr = totalScore / float(b)
                    break
                    
            if totalWickets == 4:
                onStrikeRuns = offStrikeRuns
                onStrikeBalls = offStrikeBalls
                onStrikeFours = offStrikeFours
                onStrikeSixes =  offStrikeSixes
                    
        print()
        if over == 4:
            if onStrikeBalls == 0:
                sr1 = 0
            else:
                sr1 = (onStrikeRuns/onStrikeBalls)*100
            oneInnBat.add_row([onStrike,'Not Out','','',onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes,round(sr1,2)])
            
            if totalWickets != 4:
                sr2 = (offStrikeRuns/offStrikeBalls)*100
                oneInnBat.add_row([offStrike,'Not Out','','',offStrikeRuns,offStrikeBalls,offStrikeFours,offStrikeSixes,round(sr2,2)])
            
            economy = initialScore / 1
            oneIngBowl.add_row([bowlerPresent, 1, initialDotBalls, initialScore, 
                               initialWickets, round(economy,2)])
            b = '5.0'
            rr = totalScore / 5
            continue
        else:
            economy = initialScore / 1
            oneIngBowl.add_row([bowlerPresent, 1, initialDotBalls, initialScore, 
                               initialWickets, round(economy,2)])
            
            print('     End of over {}.{}'.format(over,ball))
            print('     {}     {}/{}'.format(team1,totalScore,totalWickets))
            rr_new = totalScore/(over+1)
            print('     RR.     {}'.format(round(rr_new,2)))
            
            print()
            print('     {}     ({}){}* [{}x4,{}x6]'.format(onStrike,onStrikeRuns,onStrikeBalls,onStrikeFours,onStrikeSixes))
            print('     {}     ({}){}* [{}x4,{}x6]'.format(offStrike,offStrikeRuns,offStrikeBalls,offStrikeFours,offStrikeSixes))
            print('     {}     1.0-{}-{}-{}'.format(bowlerPresent,initialDotBalls,initialScore,initialWickets))
            print()
            
            bowlerPresent = random.choice(bowlers)
            bowlers.remove(bowlerPresent)
            
            initialScore = 0
            initialDotBalls = 0
    
    print(oneInnBat)
    print(oneIngBowl)
    oneIngTotal = PrettyTable(['Total', 'Overs', 'Run Rate', 'Extras'])
    oneIngTotal.add_row([totalScore,b,rr,0])
    print(oneIngTotal)
    
    team1, team2 = team2, team1
    target = totalScore + 1
    
    prepInnings2(team1, team2, target)
    

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