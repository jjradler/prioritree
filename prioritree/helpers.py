#!/bin/env python3
#prioritree/helpers.py
"""
Helper functions for Priortree.

Copyright Joseph James Radler, 2019
Date Written:   2019.01.31
Date Appended:  2019.01.31
Version: 0.0.1a prototype
"""
def get_g_num(goals_list):
    """
    Gets the number of goals in the `goals_list` to set the cardinality of the
    next goal object referenced and constructed by the prompt.
    InputType => List of Strings
    ReturnType => String
    """
    g_num = len(goals_list)    ## how many goals are in goals_list
    if g_num == 0:
        g_card = "1st"   ## cardinality of new object
    elif g_num == 1:
        g_card = "2nd"
    elif g_num == 2:
        g_card = "3rd"
    else:
        g_card = "%sth" % (g_num + 1)

    return g_card

def recall_gs():
    ## TODO: INSTEAD OF DOING THIS USING STATE-SAVING FILES, IT MAKES A LOT MORE
    ## SENSE TO USE AN SQLITE DATABASE TO PRESERVE THE STATE OF THE TASK TREE
    """Retrieves the list of goal objects from their IDs in a *.list file
        then will assign their attributes from a corresponding *.attr file.

        InputType => Void
        ReturnType => List of Strings
    """
    ## keep the list of goal object IDs as a *.list file in dir
    with open("goals.list", 'r') as g_file:
        g_object_list = g_file.readlines()

    for g_object in g_object_list:
        ## for each goal object `g_object` ID, there is a corresponding *.attr
        with open("{g_object}.attr", 'r') as file:
            lines = file.readlines()

        # TODO: what do I do with the attribute lines? explicitly parse?
        # TODO: perhaps set the attributes as local variables and then
        #       construct the objects again from there?

    return goals_list
