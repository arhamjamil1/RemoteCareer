import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_URL = os.getenv("PLAYWRIGHT_BASE_URL")
    TEST_USERNAME = os.getenv("TEST_USERNAME")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD")