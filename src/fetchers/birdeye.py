from typing import Optional, Dict, Any
from src.fetchers.base_fetcher import DataFetcher


class BirdeyeFetcher(DataFetcher):
    BASE_URL = "https://public-api.birdeye.so/"
    REPONSE_TYPE = "application/json"

    def fetch_data(
            self,
            endpoint: str,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, Any]] = None
    ) -> Optional[Dict[str, Any]]:
        """Fetch data from Birdeye API."""
        if params is None:
            params = {}

        if headers is None:
            headers = {}

        headers.update({"X-API-KEY": self.api_key, "accept":BirdeyeFetcher.REPONSE_TYPE})
        url = f"{self.BASE_URL}/{endpoint}"
        return self._make_request(url, params=params, headers=headers)
