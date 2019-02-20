#!/bin/env python3
#prioritree/interface.py
"""
User interface functions for Priortree that constructs the objects that
are interacting while generating the priorities list.

Copyright Joseph James Radler, 2019
Date Written:   2019.01.31
Date Appended:  2019.02.20
Version: 0.0.1a prototype
"""
import os.path
import helpers

def greeting():
    """Greetings and instructions for using the program.
    """
    pass

def open_prompt():
    """Open the prompt for managing existing goals or adding new ones,
    then adding new objectives or tasks.
    """
    add_g = input("Would you like to add any new goals? [Yes/No]")
    tempctl = (add_g.lower() is "yes")
    if tempctl:
        get_goals()
    else:
        goals_list = helpers.recall_gs()
        print("Your list of current goals is:\n\t%s\n" % goals_list)
        print('''
                Would you like to add any new objectives or tasks? If so
                please type either `objective` or `task` at the prompt below.
                ''')
        t_or_obj = input(">>> ")


def get_goals():
    """Runs prompt-input for goals"""
    loopctl = True      ## initialize
    while loopctl is True:
        if os.path.isfile("goals.list"):
            goals_list = helpers.recall_gs()
        else:
            goals_list = []
        # TODO: construct the goal objects from the list using an object construction
        # TODO: helper function that sets the attributes of existing goals.
        g_num = helpers.get_g_num(goals_list)
        g_desc = input("What is your {goalNum} goal?")
        # TODO: construct new goal object and add to list (in helpers?)
        add_g = input("Would you like to add another goal? [Yes/No]?")
        loopctl = bool(add_g.lower() is "yes")  ## loop control parameter update
        ## if add_g.lower() is "yes":
        ##     loopctl = True
        ## else:
        ##     loopctl = False

    return goals_list


def get_objectives():
    """"""
    objectives_list = []
    return objectives_list

def get_tasks():
    """"""
    tasks_list = []
    return tasks_list
