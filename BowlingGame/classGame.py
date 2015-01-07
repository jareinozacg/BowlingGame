'''
Created on 7/1/2015

@author: alfonzo
'''

class Game():
    def __init__(self):
        self._rolls = [0] * 21
        self._currentRoll = 0
 
    def roll(self, pins):
        self._rolls[self._currentRoll] = pins
        self._currentRoll += 1
