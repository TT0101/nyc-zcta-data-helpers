# -*- coding: utf-8 -*-
"""

@author: Theresa Thomaier
"""

#typing functions
#figures out and types the value given 
#supports floats, ints, and strings
def typeInputValue(val):
    isInt = tryParseInt(val)
    isFloat = tryParseFloat(val)
    
    if(isInt == "N"):
        if(isFloat == "N"):
            return str(val)
        else:
            return isFloat
    else:
        return isInt

#tries to type a value to a float, and returns "N" if not successful
def tryParseFloat(possibleFloat):
    try:
        return float(possibleFloat)
    except ValueError:
        return "N"


#tries to type a value to a int, and returns "N" if not successful
def tryParseInt(possibleInt):
    try:
        return int(possibleInt)
    except ValueError:
        return "N"

#tries to type to int and returns 0 if not successful
def cleanInts(val):
    intVal = tryParseInt(val)
        
    if(intVal == 'N'):
        return 0;
        
    return intVal

#tries to type to float and returns 0.0 if not successful
def cleanFloats(val):
    fVal = tryParseFloat(val)
        
    if(fVal == 'N'):
        return 0.0
       
    return fVal

def cleanBools(val):
    if(val.lower() == "true" or val == 1 or val.lower() == "yes" or val.lower() == "y"):
        return True
    
    return False