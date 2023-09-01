from numeric_series import NumericSeries

from util_logger import setup_logger

logger, logname = setup_logger(__file__)

class FraudSeries(NumericSeries):
    """
    A derived class from NumericSeries that adds additional attributes and methods
    specific to fraud investigation.

    Attributes:
        fraud_flags (list): A list that marks each data point as fraudulent or not
        investigator (str): The name of the investigator handling the case
    """
    
    def __init__(self, name, units, data, fraud_flags, investigator):
        """
        Initialize the FraudSeries object by calling the parent class's __init__ method
        and adding additional attributes specific to fraud investigation.
        
        Args:
            name (str): The name of the data series
            units (str): The units for the data points
            data (list): The list of data points
            fraud_flags (list): A list indicating whether each data point is fraudulent
            investigator (str): The name of the investigator
        """
        # Initialize attributes from the parent class
        super().__init__(name, units, data)
        
        # Initialize additional attributes for fraud investigation
        self.fraud_flags = fraud_flags
        self.investigator = investigator
        
    def count_fraud(self):
        """
        Count the number of fraudulent activities.

        Returns:
            int: The number of fraudulent activities
        """
        return sum(self.fraud_flags)
    
    def fraud_percentage(self):
        """
        Calculate the percentage of fraudulent activities.

        Returns:
            float: The percentage of fraudulent activities
        """
        return (self.count_fraud() / self.count()) * 100
    
    def __str__(self):
        """
        Extend the string representation of the object to include new attributes.

        Returns:
            str: The string representation of the object
        """
        base_str = super().__str__()
        return f"{base_str}, investigator={self.investigator}, fraud_count={self.count_fraud()}"

if __name__ == "__main__":
    # Create an instance of FraudSeries
    name = "Transaction Amounts"
    units = "USD"
    data = [100, 200, 150, 50, 75]
    fraud_flags = [0, 1, 0, 0, 1]  # 1 indicates fraud, 0 indicates legitimate
    investigator = "John Doe"
    
    fraud_series = FraudSeries(name, units, data, fraud_flags, investigator)
    
    # Log the object and its attributes
    logger.info(f"Created: {fraud_series}")
    logger.info(f"Count: {fraud_series.count()}")
    logger.info(f"Sum: {fraud_series.sum()}")
    logger.info(f"Mean: {fraud_series.mean()}")
    logger.info(f"Median: {fraud_series.median()}")
    logger.info(f"Count of Fraud: {fraud_series.count_fraud()}")
    logger.info(f"Fraud Percentage: {fraud_series.fraud_percentage()}%")
