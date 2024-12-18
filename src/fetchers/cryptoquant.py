from typing import Optional, Dict, Any
from src.fetchers.base_fetcher import DataFetcher


class CryptoQuantFetcher(DataFetcher):
    BASE_URL = "https://api.cryptoquant.com/v1"

    def fetch_data(
            self,
            endpoint: str,
            function_name: str = None,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, Any]] = None
    ) -> Optional[Dict[str, Any]]:
        """Fetch data from CryptoQuant API."""
        if params is None:
            params = {}

        headers = {'Authorization': 'Bearer ' + self.api_key}
        url = f"{self.BASE_URL}/{endpoint}"
        if function_name:
            url = url+f"/{function_name}?"

        return self._make_request(url, params=params, headers=headers)