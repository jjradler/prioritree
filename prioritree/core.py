#!/bin/env python3
# core.py
"""Core module of Prioritree handling the calls to IO interface
functions(interface.py), computation helper functions (helpers.py),
and the instantiation of goal,objective, and task objects and
members."""
import objects
import interface
import helpers

## object arrays are initialized as empty objects with id numbers
## they have one of each member object, also empty.
## Initial values are either `none` or correspond to default values.
#TODO: WRITE INITIALIZER FOR GOALS IN `HELPERS.PY`

goal_array = interface.get_goals()
for goal in goal_array:
    objective_array = interface.get_objectives()
    for objective in objective_array:
        tasks_array = interface.get_tasks()


## the interface with the user accepts input in a certain sequence
## the properties of all goal objects are set first to create
## the finite list of goal objects of varying priorities and due dates.
#TODO: WRITE USER INTERFACE IO FUNCTION IN `INTERFACE.PY`
## note:  it might be helpful to use one of the command-line loop tools
## that can be imported into the package.

## a helper is called to evaluate and rebalance the order of goals
## in the set by combining weights for importance (`priority`) and
## due dates. If no due date exists, its default weight is minimal.

## once the objectives are sorted, the first goal object is
## appended with an objective through the command line interface using IO functions
## called in a specific order by this core function.


