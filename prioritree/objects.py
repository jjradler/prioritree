#!/bin/env python3
#prioritree/objects.py
"""
Class definitions file containing the goal, objective, and task object
definitions.

Copyright Joseph James Radler, 2019
Date Written:   2019.01.31
Date Appended:  2019.01.31
Version:
"""

class Vertex():
    """
    Core node of the priority tree with attributes common to all types of
    vertices.

    Attributes:

    Methods:

    """
    def __init__(self, ident, priority = 1):
        """
        Vertex object instantiation
        """
        self.ident = ident       ## object identifier tag


if __name__ == __main__():
    u = Vertex(goal_1, priority = 1)
