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

    def score(self):
        score = 0
        frameIndex  = 0
        for frame in range(10):
            if self._isStrike(frameIndex):
                score += 10 + self._strikeBonus(frameIndex)
                frameIndex  += 1
            elif self._isSpare(frameIndex):
                score += 10 + self._spareBonus(frameIndex)
                frameIndex  += 2
            else:
                score += self._sumOfBallsInFrame(frameIndex)
                frameIndex  += 2
        return score
