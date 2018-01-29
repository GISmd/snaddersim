# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:38:47 2018

@author: smmcdeid

Our snakes and ladders simulator


"""

import random
import pandas

board = [[4,35],[8,47],[20,55],[23,5],[31,85],[33,9],[40,62],[44,15],[60,21],
         [63,82],[68,36],[72,90],[89,56],[91,70],[94,11],[96,81],[83,43]]

def rolldice():
    return random.randint(1,6)

def move(position):
    position += rolldice()
    return position

def check4snadders(position,board):
    for square in board:
        if position == square[0]:
#            if square[1] > position:
#                print('Yay! Climb the ladder from {} to {}!!!'.format(str(position),str(square[1])))
#            else:
#                print('Oh no! A snake got you! Go from {} to {}!!!'.format(str(position),str(square[1])))
            position = square[1]
    return position

def playgame_1player():
    position = 1
    turns = 0
    while position <= 100:
        position = move(position)
        check4snadders(position,board)
        turns += 1
#        print(position)
#    print('It took {} turns to reach 100...'.format(str(turns)))
    return turns

def run_snaddersims(sims = 10000):
    results = []
    for sim in range(sims):
        results.append(playgame_1player())
    return results

results = run_snaddersims(1000000)
df = pandas.DataFrame(results)
df.hist()
df.plot.box()
df.plot.density()