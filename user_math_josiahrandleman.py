"""
Author: Josiah Randleman
Date: 9/1/2023
Description: This file contains custom functions for fraud detection using various parameters.
"""

# Import the math module for mathematical operations
import math

# Import custom logger setup function from util_logger
from util_logger import setup_logger

# Initialize logger
logger, logname = setup_logger(__file__)

# Custom Functions

# Function to calculate the size of a dataset given its dimensions x and y
def size_of_dataset(x, y):
    return x * y

# Function to evaluate fraudulent activity based on transaction amount and average spending
def is_fraudulent(transaction_amount, avg_spending_last_month, threshold):
    # Calculate the product of the transaction amount and average spending using math.prod
    product = math.prod([transaction_amount, avg_spending_last_month])
    
    # Check the calculated product against a predefined threshold to determine if it's a potential fraud
    if product > threshold:
        return True, product
    else:
        return False, product

# Function to evaluate fraudulent activity based on transaction frequency and average amount
def is_frequency_based_fraud(transaction_count_today, average_transaction_amount, threshold):
    # Calculate the product of the transaction count today and the average transaction amount
    product = math.prod([transaction_count_today, average_transaction_amount])
    
    # Check if the calculated product crosses a certain threshold to flag it as potential fraud
    if product > threshold:
        return True, product
    else:
        return False, product

# Function to evaluate fraudulent activity based on login attempts and account balance
def is_login_based_fraud(login_attempts_today, account_balance, threshold):
    # Calculate the product of the login attempts today and the current account balance
    product = math.prod([login_attempts_today, account_balance])
    
    # Check the calculated product against a predefined threshold for potential fraud detection
    if product > threshold:
        return True, product
    else:
        return False, product

# Main function to test the custom functions
if __name__ == "__main__":
    # Define variables for each function's example usage
    # For is_fraudulent function
    transaction_amount = 500
    avg_spending_last_month = 100
    threshold = 40000

    # For is_frequency_based_fraud function
    transaction_count_today = 10
    average_transaction_amount = 200
    threshold2 = 15000

    # For is_login_based_fraud function
    login_attempts_today = 5
    account_balance = 1000
    threshold3 = 4000

    # Execute custom functions and store their output
    is_fraud, product_value = is_fraudulent(transaction_amount, avg_spending_last_month, threshold)
    is_fraud2, product_value2 = is_frequency_based_fraud(transaction_count_today, average_transaction_amount, threshold2)
    is_fraud3, product_value3 = is_login_based_fraud(login_attempts_today, account_balance, threshold3)

    # Log some examples of the math module functions
    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")

    logger.info("--------------------------------------")

    # Log the output from the custom functions
    # For the size_of_dataset function
    logger.info(f"Area of Dataset (10, 10): {size_of_dataset(10, 10)}")
    logger.info(f"Area of Dataset (15, 15): {size_of_dataset(15, 15)}")
    logger.info(f"Area of Dataset (7, 9): {size_of_dataset(7, 9)}")
    logger.info(f"Area of Dataset (8, 12): {size_of_dataset(8, 12)}")

    logger.info("--------------------------------------")

    # Log the output from the is_fraudulent function
    if is_fraud:
        logger.info(f"Potential fraudulent transaction detected! The product of the transaction amount and average spending is {product_value}, which exceeds the threshold of {threshold}.")
    else:
        logger.info(f"No fraudulent transaction detected. The product of the transaction amount and average spending is {product_value}.")

    logger.info("--------------------------------------")

    # Log the output from the is_frequency_based_fraud function
    if is_fraud2:
        logger.info(f"Potential frequency-based fraud detected! Product value is {product_value2}, which exceeds the threshold of {threshold2}.")
    else:
        logger.info(f"No frequency-based fraud detected. Product value is {product_value2}.")

    logger.info("--------------------------------------")

    # Log the output from the is_login_based_fraud function
    if is_fraud3:
        logger.info(f"Potential login-based fraud detected! Product value is {product_value3}, which exceeds the threshold of {threshold3}.")
    else:
        logger.info(f"No login-based fraud detected. Product value is {product_value3}.")

    logger.info("--------------------------------------")
