import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
    CRYPTOQUANT_API_KEY = os.getenv("CRYPTOQUANT_API_KEY")
    BIRDEYE_API_KEY = os.getenv("BIRDEYE_API_KEY")

settings = Settings()