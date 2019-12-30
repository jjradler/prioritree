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
    Defines the properties common to all vertices  of the priority tree.
    Methods in this class will also populate member objects with values given
    user input. Vertex-class objects interact through dependencies which are
    recalculated each time the goals, objectives, or task lists are updated.

    Attributes:
        _parent_id          :(string) parent object id (added to dependencies)
        name                :(string) name visible to user
        _id_tuple           :(int tuple) assigned numerical identifier (j,k,l)
        raw_priority        :(integer) user-defined input priority (1 - 3)
        _weighted_priority  :(float) algorithm-computed output priority
        due_date            :(date yyyy-mm-dd) user-defined due date
        due_time            :(hour 00:00 - 24:00) user-defined time on due date
        _time_until_due     :(float) internal value for hours until due time
        _time_weight        :(float) internal, computed value for time-priority
        description         :(string) user-input string describing the object
        _dependency_list    :(list of pairs) list of other vertex dependencies
        _dependency_weight  :(float) priority weight from dependent vertices

    Methods:
        get_name()
        get_priority()
        calc_priority()
        get_due_date()
        get_due_time()
        calc_time_until_due()
        get_description()
        get_dependencies()
        map_dependencies()

    Vertex Class Objects:
        goal_j
        objective_jk
        task_jkl

    """
    def __init__(self, name, j):
        """
        Vertex object instantiation
        """
        self.get_id(name, j) ## object id tag (GL,OB,or TK)
        self._id_tuple = (j, 0, 0)     ## gets assignment from instance arg
        self.raw_priority = 1   ## default object priority set to 1
        self.due_date = None
        self.due_time = None
        self.description = None
        self._time_until_due = None
        self._time_weight = 0
        self._dependency_list = []
        self._dependency_weight = []
        self._weighted_priority = 1  ## default
        self._parent_id = None      ## default for a goal object

    def get_id(self, name, number):
        """
        Gets id for the goal as a combination of the name as well as the number
        """
        self.name = name + "_" + number
        ## TEST PRINT
        print("The Vertex ID for this object is:\t%s\n % self.v_id")

    def get_priority(self):
        """
        Prompts the user to set the priority for this object.
        """
        print("Nothing to set here yet...")

    def _calc_priority(self):
        """
        calculates the priority for this object given the values of member
        objects 'Vertex._time_weight' and 'Vertex._dependency_weight'"""
        print("Under construction...")

    def get_due_date(self):
        """
        Prompt the user to enter the due date for this object
        """
        print("get_due_date under construction!")

    def get_due_time(self):
        """
        Prompt the user to enter a due time (if any) after creating the object
        """
        print("Nothing here yet")

    def calc_until_due(self):
        """
        Takes input from user values to establish how many minutes until the
        item is due.
        """

    def get_description(self):
        """
        Prompts the user for a description of the object.
        """

    def get_dependencies(self):
        """
        Prompts the user to enter any other goals that this one is dependent on.
        Display a list of already-entered goals and allow them to input the
        number code for that task, objective, or goal.
        """

    def map_dependencies(self):
        """
        Maps the dependencies as a matrix of dependencies with 1 corresponding
        to a dependency ON the task, 0 corresponding to no dependency, and
        -1 corresponding to a dependency of that task on this object.
        """


if __name__ == '__main__':
    GL_1 = Vertex('goal_1', 1)
    print("\nVertex class object %s of default priority %s created!\n" \
            % (GL_1.name, GL_1.raw_priority))
    GL_1.raw_priority = 3
    print("\nVertex class object %s has been upgraded to priority %s...\n" \
            % (GL_1.name, GL_1.raw_priority))
