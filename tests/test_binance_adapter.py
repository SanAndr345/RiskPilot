import unittest

from riskpilot.binance.adapter import BinanceAdapter


class TestBinanceAdapter(unittest.TestCase):

    def test_adapter_returns_empty_balances(self):
        adapter = BinanceAdapter()

        balances = adapter.get_balances()

        self.assertEqual(balances, [])

    def test_parse_spot_account(self):
        adapter = BinanceAdapter()

        response = {
            "balances": [
                {
                    "asset": "BTC",
                    "free": "0.5",
                    "locked": "0.1",
                },
                {
                    "asset": "ETH",
                    "free": "0",
                    "locked": "0",
                },
            ]
        }

        balances = adapter.parse_spot_account(response)

        self.assertEqual(len(balances), 1)
        self.assertEqual(balances[0].asset, "BTC")
        self.assertEqual(balances[0].free, 0.5)
        self.assertEqual(balances[0].locked, 0.1)


if __name__ == "__main__":
    unittest.main()
