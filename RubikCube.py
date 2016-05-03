#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'laurenttremblay'


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


    def rotateTop(self, orientation):

    def rotateFront(self, orientation):

    def rotateBack(self, orientation):

    def rotateLeft(self, orientation):

    def rotateRight(self, orientation):

    def rotateBottom(self, orientation):

    def rotateMiddleVert(self, orientation):

    def rotateMiddleHori(self, orientation):

    def rotateSolidFace(self, face):
        """Rotate a single flat face, not accounting for the cube's geometry"""

