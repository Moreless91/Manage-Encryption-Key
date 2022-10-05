import json
import logging
import sys
from pathlib import Path
from datetime import datetime

"""
+------------------------------------------------------------------+
|                         Log Level Chart:                         |
|            DEBUG:    INFO:    WARNING:    ERROR:    CRITICAL:    |
| NOTSET                                                           |
| DEBUG        X         X         X          X          X         |
| INFO                   X         X          X          X         |
| WARNING                          X          X          X         |
| ERROR                                       X          X         |
| CRITICAL                                               X         |
+------------------------------------------------------------------+
"""


def verify_config_exists(settings_location: str) -> None:
    config_path_check = Path(settings_location)
    if config_path_check.is_file():
        return
    else:
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        msg1 = f"{dt_string}: CRITICAL [base_logger.py] - verify_config_exists() :: Cannot find {settings_location}"
        msg2 = f"{dt_string}: CRITICAL [base_logger.py] - verify_config_exists() :: Exiting..."
        # Writing to file
        with open("Logs/app.log", "w") as file1:
            # Writing data to a file
            file1.write(f"{msg1}\n{msg2}")

        # Print to console
        print(f"{msg1}\n{msg2}")
        exit()


def load_user_settings(settings_location: str) -> tuple[str, str, str]:
    """Load User Setting log level"""
    with open(settings_location) as json_data_file:
        config_file = json.load(json_data_file)

    log_level = config_file["logging"]["level"]
    overwrite_log = config_file["logging"]["overwrite_log"]
    log_location = config_file["logging"]["log_location"]

    return log_level, overwrite_log, log_location


def current_log_level(log_level: str) -> int:
    match log_level:
        case "NOTSET":
            logLevel = logging.NOTSET
        case "DEBUG":
            logLevel = logging.DEBUG
        case "INFO":
            logLevel = logging.INFO
        case "WARNING":
            logLevel = logging.WARNING
        case "ERROR":
            logLevel = logging.ERROR
        case "CRITICAL":
            logLevel = logging.CRITICAL

    return logLevel


def overwrite_log_file(overwrite_log: str) -> str:
    if overwrite_log == True:
        logFilemode = "w"
    else:
        logFilemode = "a"

    return logFilemode


# Load User Setting log level:
settings_location = "Settings/config.json"
verify_config_exists(settings_location)
log_level, overwrite_log, log_location = load_user_settings(settings_location)

# Set log file location
logLocation = log_location

# Set Log Level:
logLevel = current_log_level(log_level)

# Set filemode to overwrite or append:
logFilemode = overwrite_log_file(overwrite_log)

# Build log format:
logFormat = "%(asctime)s,%(msecs)d: %(levelname)s [%(filename)s:%(lineno)d] - %(funcName)s() :: %(message)s"

# Setup the File Handler for writing to a .log file:
file_handler = logging.FileHandler(filename=logLocation, mode=logFilemode)

# Setup the Stream Handler for STDOUT to the console/terminal:
stdout_handler = logging.StreamHandler(stream=sys.stdout)

# Create list of Handlers:
# Add 'stdout_handler' to handlers list below to track text in console
handlers = [file_handler]

# Create log config output:
logging.basicConfig(
    format=logFormat,
    level=logLevel,
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=handlers,
)

# Setup variable for import: from Modules.base_logger import logger
logger = logging
