'''
Created on 7/1/2015

@author: alfonzo
'''
import unittest


from classGame import Game
import unittest
 
class BowlingGameTest(unittest.TestCase):
    def setUp(self):
        self.g = Game()
 
    def testminScoringMinRollsGame(self):
        self.roll_many(9, 10)
        self.assertEquals(240, self.g.score())
 
 
    def roll_many(self, n, pins):
        for i in range(n):
            self.g.roll(pins)
 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()