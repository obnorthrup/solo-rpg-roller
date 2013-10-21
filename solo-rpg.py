#!/usr/bin/env python

__author__ = 'obnorthrup'
__email__ = "oliver.northrup@gmail.com"

import sys
import random


def d(rolls,sides):
    '''Roll some dice, and return a list of the rolls.'''
    rollList = []
    for i in range(0,rolls):
        rollList.append(random.randint(1,sides))
    return rollList
    
def fateWrapper(advantage=''):
    '''Prints the output from fateRoller'''
    # Set theRoll to a triple (rolls list, fate string, twist string)
    theRoll = fateRoller(advantage)
    print theRoll[1]
    if theRoll[2] != "No twist.":
        print theRoll[2]
    
def fateRoller(advantage=''):
    '''Rolls normal dice and twist die, then returns a tuple of:
    Rolls (list of ints), the fate response (string), and the twist (string)'''
    # Build a dict of responses
    fate = {}
    fate[1] = "No and..."
    fate[2] = "No."
    fate[3] = "No but..."
    fate[4] = "Yes but..."
    fate[5] = "Yes."
    fate[6] = "Yes and..."
    
    # Roll the right number of dice, depending of there's advantage or not
    if advantage == '':
        myRoll = d(1,6)
    else:
        myRoll = d(2,6)
    
    # Take the minimum if the roll's at disadvantage, or the maximum otherwise
    if advantage == '-':
        myFate = min(myRoll)
    else:
        myFate = max(myRoll)
    
    # Get a string response for the twist
    twistLine = isTwist()
    
    # Return a tuple of the rolls (list), fate (string) and the twist (string)
    output = (myRoll, fate[myFate], twistLine)
    return output
    
def isTwist():
    '''Rolls a d6. On a 1, returns a twist via twistRoller.
    Otherwise, returns "No twist."'''
    isTwistRoll = d(1,6)[0]
    
    if isTwistRoll != 1:
        return 'No twist.'
    else:
        return twistRoller()
    

def twistRoller():
    """Rolls 2d6, gives the result, and prints the outcome from the dict."""
    
    # Build a dict of nouns
    noun = {}
    noun[1] = "NPC"
    noun[2] = "PC"
    noun[3] = "Organization"
    noun[4] = "Physical event"
    noun[5] = "Emotional event"
    noun[6] = "Item"
    
    # Build a dict of verbs
    verb = {}
    verb[1] = "appears"
    verb[2] = "alters the location"
    verb[3] = "helps the hero"
    verb[4] = "hinder the hero"
    verb[5] = "changes the goal"
    verb[6] = "ends the scene"
    
    # Roll em!
    twistRoll = d(2,6)
    theNoun = noun[twistRoll[0]]
    theVerb = verb[twistRoll[1]]
    
    # Return twist string
    return "Twist! " + theNoun + " " + theVerb + "."

if __name__ == "__main__":
    try:
        advantage = str(sys.argv[1])
    except:
        advantage = ''
    
    okResponses = ['+','-','']
    if advantage not in okResponses:
        print "Sorry, please specify advantage (+), disadvantage (-), or normal (no arg)."
    else:
        fateWrapper(advantage)