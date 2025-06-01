# Importing necessary modules
import logging  # Import the logging module for logging purposes
import os  # Import the os module for operating system functionalities
from datetime import datetime  # Import datetime module for date and time operations

# Define the log file name based on current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Construct the path to the logs directory and the log file
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the logs directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Define the full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging module
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Specify the log file path
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Specify the log format
    level=logging.INFO,  # Set the logging level to INFO (logs INFO and higher levels)
)
