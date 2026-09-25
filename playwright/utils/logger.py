import logging
import os


os.makedirs("test-results", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("test-results/test.log"),
        logging.StreamHandler()
    ]
)


logger = logging.getLogger("playwright-tests")