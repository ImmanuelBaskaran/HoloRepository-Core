import logging
import os
import sys

from dotenv import load_dotenv

# Load data from .env file (will not override actual env variables if set)
load_dotenv(verbose=True)

# Application
FLASK_ENV = os.getenv("FLASK_ENV")
APP_PORT = os.getenv("APP_PORT")

# Settings for processing etc.
INPUT_RESOLUTION_MAX = os.getenv("INPUT_RESOLUTION_MAX", 256)

# Jobs
NUM_OF_WORKER_PROCESSES = os.getenv("NUMBER_OF_WORKER_PROCESSES", 4)
KEEP_ALL_FILES = os.getenv("KEEP_ALL_FILES", False)
KEEP_ALL_LOG_FILES = os.getenv("KEEP_ALL_LOG_FILES", False)
GARBAGE_COLLECTION_INTERVAL_SECS = os.getenv("GARBAGE_COLLECTION_INTERVAL_SECS", 30)
GARBAGE_COLLECTION_INACTIVE_JOB_TTL_SECS = os.getenv(
    "GARBAGE_COLLECTION_INACTIVE_JOB_TTL_SECS", 1800
)

# Models
NIFTYNET_MODEL_TIMEOUT = os.getenv("NIFTYNET_MODEL_TIMEOUT", 300)
MODEL_ABDOMINAL_SEGMENTATION_HOST = os.getenv("MODEL_ABDOMINAL_SEGMENTATION_HOST")
MODEL_ABDOMINAL_SEGMENTATION_PORT = os.getenv("MODEL_ABDOMINAL_SEGMENTATION_PORT")

# Other service endpoints
HOLOSTORAGE_ACCESSOR_HOST = os.getenv("HOLOSTORAGE_ACCESSOR_HOST")
HOLOSTORAGE_ACCESSOR_PORT = os.getenv("HOLOSTORAGE_ACCESSOR_PORT")

if not all(
    [
        FLASK_ENV,
        APP_PORT,
        INPUT_RESOLUTION_MAX,
        NUM_OF_WORKER_PROCESSES,
        KEEP_ALL_FILES,
        KEEP_ALL_LOG_FILES,
        GARBAGE_COLLECTION_INTERVAL_SECS,
        GARBAGE_COLLECTION_INACTIVE_JOB_TTL_SECS,
        NIFTYNET_MODEL_TIMEOUT,
        MODEL_ABDOMINAL_SEGMENTATION_HOST,
        MODEL_ABDOMINAL_SEGMENTATION_PORT,
        HOLOSTORAGE_ACCESSOR_HOST,
        HOLOSTORAGE_ACCESSOR_PORT,
    ]
):
    logging.error("Fatal error: Not all required environment variables are set")
    # Note: This return code is kind of a hack. When invoked through gunicorn,
    # any other return code seems to restart the server, which is usually good.
    # In this case however, it is preferable to error out immediately.
    sys.exit(4)
