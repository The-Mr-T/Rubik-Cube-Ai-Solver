#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'laurenttremblay'

import sys
from termcolor import colored, cprint

class RubikCube():
    """Represents a Rubik cube. Color of the faces are represented by strings

    By convention, the cube remains always in the same orientation.
    Top is red, Front is Yellow, Back is white, Left is green, Right is blue and bottom is orange.
    """

    def __init__(self):
        """Initialize a solved cube"""

        # Creates a list containing 5 lists, each of 8 items, all set to 0
        w, h = 3, 3
        self.topFace = [["R" for x in range(w)] for y in range(h)]
        self.frontFace = [["Y" for x in range(w)] for y in range(h)]
        self.backFace = [["W" for x in range(w)] for y in range(h)]
        self.leftFace = [["G" for x in range(w)] for y in range(h)]
        self.rightFace = [["B" for x in range(w)] for y in range(h)]
        self.bottomFace = [["O" for x in range(w)] for y in range(h)]

        self.faces = {'top': self.topFace,
                      'front': self.frontFace,
                      'back': self.backFace,
                      'left': self.leftFace,
                      'right': self.rightFace,
                      'bottom': self.bottomFace}

        self.color = {'R': 'red',
                      'B': 'blue' ,
                      'G': 'green',
                      'W': 'white',
                      'O': 'cyan',
                      'Y': 'yellow'}

    #def rotateTop(self, orientation):

    #def rotateFront(self, orientation):

    #def rotateBack(self, orientation):

    #def rotateLeft(self, orientation):

    #def rotateRight(self, orientation):

    #def rotateBottom(self, orientation):

    #def rotateMiddleVert(self, orientation):

    #def rotateMiddleHori(self, orientation):

    def rotateSolidFace(self, face, direction):
        """Rotate a single flat face, not accounting for the cube's geometry

        Returns the rotated face
        """
        # Borrowed to Peter Norvig http://www.norvig.com/python-iaq.html
        # And http://stackoverflow.com/a/496056

        if direction == "cw":
            # Rotates Clockwise
            return zip(*face[::-1])

        elif direction == "ccw":
            # Rotate counter-clockwise
            return zip(*face)[::-1]

        else:
            raise NameError('NotAValidOrientation')
            return

def printCube(cube):
    """Prints an unwrapped cube to the terminal, using ANSII codes"""
    size = len(cube.faces['top'])
#█
    #Prints the first back cube
    text = ""

    for elem in range(size):
        for x in range(size):
            text = text + colored(' ', 'red')
        for y in range(size):
            text = text + colored('█', cube.color[cube.faces['back'][elem][y]] )
        print(text)
        text = ""

    for elem in range(size):
        #left
        for y in range(size):
            text = text + colored('█', cube.color[cube.faces['left'][elem][y]] )
        #top
        for y in range(size):
            text = text + colored('█', cube.color[cube.faces['top'][elem][y]] )
        #right
        for y in range(size):
            text = text + colored('█', cube.color[cube.faces['right'][elem][y]] )
        #botom
        for y in range(size):
            text = text + colored('█', cube.color[cube.faces['bottom'][elem][y]] )
        print(text)
        text = ""

    #Prints the last front cube
    for elem in range(size):
        for x in range(size):
            text = text + colored(' ', 'red')
        for y in range(size):
            text = text + colored('█', cube.color[cube.faces['front'][elem][y]] )
        print(text)
        text = ""

x = RubikCube()

printCube(x)


