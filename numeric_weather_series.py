'''
Purpose: Create a class that inherits everything from NumericSeries and adds
attributes and/or behavior specific to Weather. 

If you don't need to add specialized attributes or behavior, 
you can just use the original NumericSeries class directly. 
No subclassing required.

We get all of our parent's attributes and methods for free (no coding required).

Weather adds:

- a location attribute

'''

# From the name of the module (the file name without .py), import the class we want to inherit from
from numeric_series import NumericSeries

from util_logger import setup_logger
logger, logname = setup_logger(__file__)


class NumericWeatherSeries(NumericSeries):
    """
    A class representing a numeric series customized for weather data.

    (Additional) Attributes:
       location (string): the location where the data was collected
    """

    def __init__(self, name, units, data, location):
        """
        Initialize the object when first created using the arguments passed in.
        Every class needs an __init__ method to construct a new object.

        @args:
            self (object): the object being created that will hold the real data
            name (str): a short name for this list of numeric data
            units (str): the units in which the data is measured
            data (list): the list of numeric data to be held by the object
            location (str): the location where the data was collected

        """

        # First, initialize the parent (super) class with parent's attributes
        # By calling the super constructor method
        super().__init__(name, units, data)

        # Then, initialize our additional specialized attributes
        self.location = location

    def __str__(self):
        """
        Return a string representation of the instantiated object.
        The two underscores before and after indicate this is a special method.
        Every class needs a __str__ method that returns a string representation of the object.
        Be sure to use self.attribute_name so you use the object's attribute, not a local variable! 

        Returns:
            str: a string representation of the instantiated object
        """
        str = f"NumericWeatherSeries with name={self.name}, units={self.units}, location={self.location}, and {len(self.data)} data points: {self.data}"
        return str




if __name__ == "__main__":
    # If we're running this script (instead of using it in another class or script), 
    # Run some code to try our class

    # Create an object by calling the constructor 
    # The constructor method is always the name of the class
    # pass in the information required by the __init__ method defined in the class

    name1 = "Monday Temperatures"
    units1 = "F"
    data1 = [45.8, 73.4, 73.4, 78, 76.3]
    loc = "Maryville MO"

    object1 = NumericWeatherSeries(name1, units1, data1, loc)

  
    name2 = "Tuesday Temperatures"
    units2 = "F"
    data2 = [64.2, 67.2, 52.8, 63.4, 71.4, 73.1, 76.3]
    loc2 = "Maryville MO"

    object2 = NumericWeatherSeries(name2, units2, data2, loc2)

    
    # Create another object 

    # use range() to create a list of values from 65 to 78
    # list() converts the range object to a list
    # range() is a generator - it creates a sequence of numbers without storing them in memory
    # The arguments in range are from (inclusive) and to (exclusive)
    data3 = list(range(66, 79))
    name3 = "Wednesday Temperatures"
    units3 = "F"
    loc3 = "Maryville MO"

    object3 = NumericWeatherSeries(name3, units3, data3, loc3)

    # log the objects created
    logger.info(f"Created: {object1}")
    logger.info(f"Created: {object2}")
    logger.info(f"Created: {object3}")

    object_list = [object1, object2, object3]


    for object in object_list:
        logger.info(object)
        logger.info(f"Count: {object.count()}")
        logger.info(f"Sum: {object.sum()}")
        logger.info(f"Mean: {object.mean()}")
        logger.info(f"Median: {object.median()}")
        logger.info("------------------")

