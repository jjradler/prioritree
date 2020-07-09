#!/bin/env python3
#node.py
"""
    Prototype of Node class objects for the priority tree graph.
    Date: 2019.04.26
    Copyright Joseph J. Radler 2019
"""
import abc


class Node(abc):
    """
        Node object corresponding to Goals, Objectives, and Tasks.
        Attributes:
            str     label:     String containing the node label
            int     user_priority_weight:    Priority Weight (from 0 to 2)
            str     node_type:  Node type ('goal', 'objective', 'task')
            strlist node_dependencies:  List of dependent nodes (reducing Node.user_priority_weight)
            strlist node_spawn: List of nodes dependent on this one (increasing Node._internal_weight)

    """
    def __init__(self):
        """
            Node class constructor
        """
        self.__accepted_node_types = ['root', 'goal', 'objective', 'task']
        self._label = self.__class__.__name__
        self.user_priority_weight = None
        self.node_type = None
        self._dependencies = []
        self._parents = []
        self.description = ""

    @property
    def _internal_weight(self):
        """

        :return:
        """
        # Not yet implemented, but recalculates based on dependencies and/or due dates
        yield None

    def set_node_type(self):
        """

        :param node_type:
        :return:
        """
        _check_node_type(self)

    def _check_node_type(self):
        """

        :return:
        """
        try:
            assert self._node_type in self.__accepted_node_types
        except ValueError("This is not an accepted Node Type for Prioritree! Enter a different value or -111 to quit."):
            pass

    def set_description(self):
        """
            Prompt the user for a description of the node
        """
        self.description = input("Enter a description for {}: ".format(self.label))

        try:
            self.description.lower()
        except ValueError:
            print("This is not a string and cannot be used for description.")

    def set_dependencies(self):
        """
            Check dependencies on other nodes.
        """
        raise NotImplemented


if __name__ == "__main__":
    # Test goal node construction
    pass
