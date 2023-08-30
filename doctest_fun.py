"""
Purpose: Illustrate how to write good functions, 
        discuss types of arguments:
             - positional (unnamed args - based on order
             - keyword args (these are named args and optional)
             - default values for keyword args can be provided

        every function gets an implicit *args and **kwargs
        *args is the list of positional arguments
        **kwargs is the dictionary of keyword arguments

        You don't have to master args and kwargs but it's good to know

In general, try to write functions that return a value (or values).

If the function does something else (e.g. prints to the console),
it's called a 'side effect'.

Being able to write good, simple, straightforward reusable functions is a very valuable skill.

With Python we can define 'unit tests' right here in the docstring.
 - Show what SHOULD happen (will test this with doctest)
 - Using interactive Python style to illustrate desired behavior.
 - Writing unit tests along with code is a very valuable practice. 

 ----------------------------------------------------------
 UNIT TESTS BELOW - SPECIFY CORRECT BEHAVIOR
 ----------------------------------------------------------

>>> add_two(1,2)
3

>>> add_two("hello"," world")
'hello world'

>>> add_triangle_list( [3,4,5] )
12

>>> transform_using_keyword_args_with_default_values()
'bearcat'

>>> transform_using_keyword_args_with_default_values(reverse=True)
'tacraeb'

>>> transform_using_keyword_args_with_default_values(input="hello", reverse=True)
'olleh'

>>> add_any_using_args(1,1,1,1,1,1,1,1)
8

>>> add_any_with_keyword_arguments_kwargs(a=1,b=2)
3

@uses doctest - to verify our functions are correct
"""

import doctest

from util_logger import setup_logger
logger, logname = setup_logger(__file__)


def add_two(first, second):
    """Return the sum of any two arguments."""
    logger.info(f"CALLING add_two({first},{second})")

    sum = first + second

    logger.info(f"RETURNING {sum}")
    return sum


def add_triangle_list(list_triangle):
    """Return the sum of three numbers in a list."""
    logger.info(f"CALLING add_triangle_list({list_triangle})")

    sum = 0
    for value in list_triangle:
        sum = sum + value
        
    logger.info(f"RETURNING {sum}")
    return sum



def add_any_using_args(*args):
    """Return the sum of numbers, using built-in *args."""
    logger.info(f"CALLING add_any_using_args({args})")
    sum = 0
    for x in args:
        sum += x  # Use the popular and concise version of sum = sum + x

    logger.info(f"RETURNING {sum}")
    return sum


def add_any_with_keyword_arguments_kwargs(**kwargs):
    """Return the sum of numbers, using built-in keyword args, **kwargs."""
    logger.info(f"CALLING add_any_with_keywords({kwargs})")
    sum = 0
    for value in kwargs.values():  # use values() - name doesn't matter
        sum += value  # Use the popular and concise version of sum = sum + x
    
    logger.info(f"RETURNING {sum}")
    return sum

def transform_using_keyword_args_with_default_values(input="bearcat", reverse=False):
    '''Return a string with the input string reversed, if reverse is True.
    @kwargs:
        input: a string, default "bearcat"
        reverse: a boolean, default False'''
    s = f"CALLING transform_using_keyword_args_with_default_values(input={input}, reverse={reverse})"
    logger.info(s)

    result = input
    if reverse:
        result = input[::-1]
    
    logger.info(f"RETURNING {result}")
    return result



if __name__ == "__main__":

    # -------------------------------------------------------------
    # Call some functions and execute code!

    add_two(7,7)
    add_triangle_list([5,5,5])
    add_any_using_args(2)
    add_any_using_args(2,2)
    add_any_using_args(2,2,2)
    add_any_using_args(2,2,2,2)
    add_any_with_keyword_arguments_kwargs(a=9,b=4)
    add_any_with_keyword_arguments_kwargs(first=8,second=2, third=3)
    add_any_with_keyword_arguments_kwargs(only=11)

    transform_using_keyword_args_with_default_values()
    transform_using_keyword_args_with_default_values(reverse=True)
    transform_using_keyword_args_with_default_values(input="hello", reverse=True)

    logger.info("===========================================================")
    logger.info("Running doctest.testmod() function to unit test our code")
    logger.info("===========================================================")

    # Run doctest and log the results

    doctest_result = doctest.testmod()
    if doctest_result.failed == 0:
        logger.info("All tests passed!")
    else:
        logger.error(f"{doctest_result.failed} tests failed!")

    logger.info("Script complete. More info in the log file.")
        
