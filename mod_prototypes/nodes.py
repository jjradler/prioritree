#!/bin/env python3
#nodes.py
"""
    Prototype of Node class objects for the priority tree graph.
    Date: 2019.04.26
    Copyright Joseph J. Radler 2019
"""
class Node():
    """
        Node object corresponding to Goals, Objectives, and Tasks.
        Attributes:
            str     label:     String containing the node label
            int     pweight:    Priority Weight (from 0 to 2)
            str     node_type:  Node type ('goal', 'objective', 'task')
            strlist node_deps:  List of dependent nodes (reducing Node.pweight)
            strlist node_spawn: List of nodes dependent on this one (increasing Node.pweight)

    """
    def __init__(self, node_type):
        """
            Node class constructor
        """
        self.label = self.__class__.__name__
        self.pweight = 0
        self.node_type = node_type
        self.description = "Default Description"

        self.set_description()

    def set_nodetype(self):
        """
            Docstring
        """

    def set_description(self):
        """
            Prompt the user for a description of the node
        """
        self.description = input("Enter a description for {}: ".format(self.label))
        try:
            self.description.lower()
        except ValueError:
            print("This is not a string and cannot be used for description.")

    def set_deps(self):
        """
            Check dependencies on other nodes.
        """
        self.node_deps = list()

if __name__ == "__main__":
    # Test goal node construction
    print("Testing Goal Node Construction...")
    print("Constructing the first Goal-type node...")
    Goal1 = Node(node_type='goal')
    print("Goal named {} has been instantiated.".format(Goal1.label))
    print("The node named {} has a default description:  {}".format(Goal1.label,\
            Goal1.description))
    # Goal1.description = "A test to make sure that a Goal Node object has been instantiated!"
    # print("The {} object has a description: ".format(Goal1.label), Goal1.description)
    print("The goal {} has a default priority weight of: ".format(Goal1.label), Goal1.pweight)
    print("The goal {} has had its priority weight changed to {}".format(Goal1.label,\
            Goal1.pweight))
