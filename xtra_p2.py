"""
Purpose: 

Practice writing functions using positional and keyword arguments.
Practice logging functions using the util_datafun_logger module
Log each time the function is called (along with its arguments)
Log the result of each function just before you return the result

 ----------------------------------------------------------
 UNIT TESTS BELOW - SPECIFY CORRECT BEHAVIOR
 ----------------------------------------------------------

>>> sum_two(1,2)
3

>>> sum_two("hello"," world")
'hello world'

>>> sum_rectangle_list( [1,1,3,3] )
8

>>> transform_using_keyword_args_with_default_values()
'bea'

>>> transform_using_keyword_args_with_default_values(reverse=True)
'aeb'

>>> transform_using_keyword_args_with_default_values(input="hello", reverse=True)
'leh'

>>> sum_any_using_args(1,1,1,2)
5

>>> sum_any_with_keyword_arguments_kwargs(a=1,b=2,c=3)
6

@uses doctest - to verify our functions are correct
"""
# TODO: Add functions to get the unit tests to pass 
# TODO: Log each time the function is called (along with its arguments)
# TODO: Log the result of each function just before you return the result
# TODO: Fix this function to get just the first 3 letters (possibly reversed)

import doctest
from util_logger import setup_logger

logger, logname = setup_logger(__file__)

# Function to sum two numbers or concatenate two strings
def sum_two(x, y):
    logger.info(f"CALLING sum_two(x={x}, y={y})")
    
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        result = x + y
    elif isinstance(x, str) and isinstance(y, str):
        result = x + y  
    else:
        logger.error("Incompatible types: cannot sum or concatenate.")
        return None
    
    logger.info(f"RETURNING {result}")
    return result

# Function to return the first 3 letters of an input string, possibly reversed
def transform_using_keyword_args_with_default_values(input="bearcat", reverse=False):
    logger.info(f"CALLING transform_using_keyword_args_with_default_values(input={input}, reverse={reverse})")
    result = input[:3][::-1] if reverse else input[:3]
    logger.info(f"RETURNING {result}")
    return result

# Function to sum the area of a rectangle given a list [x1, y1, x2, y2]
def sum_rectangle_list(rect_list):
    logger.info(f"CALLING sum_rectangle_list(rect_list={rect_list})")
    x1, y1, x2, y2 = rect_list
    result = abs(x1 + y1 + x2 + y2)
    logger.info(f"RETURNING {result}")
    return result

# Function to sum any number of arguments
def sum_any_using_args(*args):
    logger.info(f"CALLING sum_any_using_args(args={args})")
    result = sum(args)
    logger.info(f"RETURNING {result}")
    return result

# Function to sum any keyword arguments
def sum_any_with_keyword_arguments_kwargs(**kwargs):
    logger.info(f"CALLING sum_any_with_keyword_arguments_kwargs(kwargs={kwargs})")
    result = sum(kwargs.values())
    logger.info(f"RETURNING {result}")
    return result

if __name__ == "__main__":
    logger.info("===========================================================")
    logger.info("Running doctest.testmod() function to unit test our code")
    logger.info("===========================================================")
    
    doctest_result = doctest.testmod()
    if doctest_result.failed == 0:
        logger.info("All tests passed!")
    else:
        logger.error(f"{doctest_result.failed} tests failed!")
    
    logger.info("Script complete. More info in the log file.")

