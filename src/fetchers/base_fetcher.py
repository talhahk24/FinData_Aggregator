import requests
#import json
import logging
import time
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataFetcher(ABC):
    def __init__(self, api_key: str, max_retries: int = 3, retry_delay: int = 2):
        self.api_key = api_key
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    @abstractmethod
    def fetch_data(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None
        ) -> Optional[Dict[str, Any]]:
        """Fetch data from the API endpoint."""
        pass

    def _make_request(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None
        ) -> Optional[Dict[str, Any]]:
        """Helper method to make HTTP GET requests with retries."""
        for attempt in range(self.max_retries):
            try:
                response = requests.get(url, params=params, headers=headers)
                response.raise_for_status()  # Raise an error for bad status codes
                return response.json()

            except requests.exceptions.RequestException as e:
                logger.error(f"Attempt {attempt + 1} failed: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay * (attempt + 1))  # Exponential backoff
                else:
                    logger.error(f"Max retries reached. Failed to fetch data from {url}")
                    return None