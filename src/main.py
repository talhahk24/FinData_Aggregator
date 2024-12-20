from src.config.settings import settings
from src.fetchers.alpha_vantage import AlphaVantageFetcher
from src.fetchers.cryptoquant import CryptoQuantFetcher
from src.fetchers.birdeye import BirdeyeFetcher

import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Initialize fetchers
    alpha_vantage_fetcher = AlphaVantageFetcher(settings.ALPHA_VANTAGE_API_KEY)
    crypto_quant_fetcher = CryptoQuantFetcher(settings.CRYPTOQUANT_API_KEY)
    birdeye_fetcher = BirdeyeFetcher(settings.BIRDEYE_API_KEY)

    # Fetch data
    alpha_vantage_params = {
        "symbol": "BTC",
        "market": "USD"
    }
    alpha_vantage_data = alpha_vantage_fetcher.fetch_data(
        endpoint="DIGITAL_CURRENCY_DAILY",
        params=alpha_vantage_params
    )
    logger.info("Alpha Vantage Data: %s", json.dumps(alpha_vantage_data, indent=2))


    crypto_quant_params = {
        "exchange": "binance",
        "window":"day",
        "from":20191001,
        "limit":2
    }
    crypto_quant_data = crypto_quant_fetcher.fetch_data(
        endpoint="btc/exchange-flows",
        function_name="reserve",
        params=crypto_quant_params
    )



    birdeye_data_params = {
        "address": "So11111111111111111111111111111111111111112",
        "check_liquidity":100
    }
    birdeye_headers = {"x-chain": "solana"}
    birdeye_data = birdeye_fetcher.fetch_data(
        endpoint="defi/price",
        params=birdeye_data_params,
        headers=birdeye_headers
    )
    logger.info("Birdeye Data: %s", json.dumps(birdeye_data, indent=2))

