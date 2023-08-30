# Import the statistics module for statistical calculations
import statistics

# Import the logger setup function from an instructor-provided module
from util_logger import setup_logger

# Set up the logger using the current file's name
logger, logname = setup_logger(__file__)

# Define bivariate data for 'hours studied' and 'exam scores'
study_hours_x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
exam_scores_y = [65, 70, 75, 80, 85, 90, 92, 95, 98, 100]

# Calculate descriptive statistics for 'exam_scores_y'
# 1. Mean
mean_scores = statistics.mean(exam_scores_y)
# 2. Median
median_scores = statistics.median(exam_scores_y)
# 3. Mode (Be cautious, all values are unique in this dataset)
mode_scores = statistics.mode(exam_scores_y)
# 4. Variance
variance_scores = statistics.variance(exam_scores_y)
# 5. Standard Deviation
std_deviation_scores = statistics.stdev(exam_scores_y)
# 6. Minimum score
min_score = min(exam_scores_y)
# 7. Maximum score
max_score = max(exam_scores_y)

# Calculate descriptive statistics for 'study_hours_x'
# 1. Mean
mean_hours = statistics.mean(study_hours_x)
# 2. Median
median_hours = statistics.median(study_hours_x)
# 3. Mode (Be cautious, all values are unique in this dataset)
try:
    mode_hours = statistics.mode(study_hours_x)
except statistics.StatisticsError:
    mode_hours = 'No unique mode'
# 4. Variance
variance_hours = statistics.variance(study_hours_x)
# 5. Standard Deviation
std_deviation_hours = statistics.stdev(study_hours_x)
# 6. Minimum hours
min_hours = min(study_hours_x)
# 7. Maximum hours
max_hours = max(study_hours_x)



# Manually calculate the range for study hours (difference between max and min)
hours_range = max_hours - min_hours
logger.info(f"Range: {hours_range:.2f}")
logger.info("---------------------------------------")

# Log the calculated statistics
logger.info("---------------------------------------")
logger.info(f"Study Hours -> X Values {study_hours_x}")
logger.info(f"Exam Scores -> Y Values {exam_scores_y}")
logger.info("---------------------------------------")
logger.info("Descriptive statistics for exam scores:")
logger.info(f"Mean: {mean_scores:.2f}")
logger.info(f"Median: {median_scores:.2f}")
logger.info(f"Mode: {mode_scores:.2f}")
logger.info("---------------------------------------")
logger.info(f"Variance: {variance_scores:.2f}")
logger.info(f"Standard Deviation: {std_deviation_scores:.2f}")
logger.info(f"Smallest Score: {min_score:.2f}")
logger.info(f"Largest Score: {max_score:.2f}")

# Manually calculate the range (difference between max and min)
score_range = max_score - min_score
logger.info(f"Range: {score_range:.2f}")
logger.info("---------------------------------------")

# Log the calculated statistics for study hours
logger.info("Descriptive statistics for study hours:")
logger.info(f"Mean: {mean_hours:.2f}")
logger.info(f"Median: {median_hours:.2f}")
logger.info(f"Mode: {mode_hours}")
logger.info(f"Variance: {variance_hours:.2f}")
logger.info(f"Standard Deviation: {std_deviation_hours:.2f}")
logger.info(f"Smallest Hours: {min_hours:.2f}")
logger.info(f"Largest Hours: {max_hours:.2f}")

logger.info("---------------------------------------")

# Calculate and log correlation coefficients
xx_corr = statistics.correlation(study_hours_x, study_hours_x)
xy_corr = statistics.correlation(study_hours_x, exam_scores_y)
logger.info(f"Correlation between study hours and study hours = {xx_corr}")
logger.info(f"Correlation between study hours and exam scores = {xy_corr}")
logger.info("---------------------------------------")

# Calculate and log the slope and intercept using linear regression
slope, intercept = statistics.linear_regression(study_hours_x, exam_scores_y)
logger.info(f"Slope = {slope}")
logger.info(f"Intercept = {intercept}")
logger.info("---------------------------------------")
