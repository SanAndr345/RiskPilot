import unittest

from riskpilot.binance.adapter import BinanceAdapter, BinanceBalance

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

    def test_balances_to_positions(self):
        adapter = BinanceAdapter()

        balances = [
            BinanceBalance(
                asset="BTC",
                free=0.5,
                locked=0.1,
            ),
            BinanceBalance(
                asset="ETH",
                free=1.0,
                locked=0.5,
            ),
        ]

        positions = adapter.balances_to_positions(balances)

        self.assertEqual(len(positions), 2)
        self.assertEqual(positions[0].symbol, "BTC")
        self.assertEqual(positions[0].value, 0.6)
        self.assertEqual(positions[1].symbol, "ETH")
        self.assertEqual(positions[1].value, 1.5)

    def test_balances_to_positions_risk_engine(self):
        adapter = BinanceAdapter()

        balances = [
            BinanceBalance(
                asset="BTC",
                free=6.0,
                locked=0.0,
            ),
            BinanceBalance(
                asset="ETH",
                free=4.0,
                locked=0.0,
            ),
        ]

        positions = adapter.balances_to_positions(balances)

        from riskpilot.risk.engine import assess_concentration

        result = assess_concentration(positions)

        self.assertEqual(result.total_value, 10.0)
        self.assertEqual(result.largest_position, "BTC")
        self.assertEqual(result.largest_weight, 0.6)
        self.assertEqual(result.concentration_risk, "HIGH")

    def test_balances_to_positions_with_prices(self):
        adapter = BinanceAdapter()

        balances = [
            BinanceBalance(
                asset="BTC",
                free=0.5,
                locked=0.1,
            ),
            BinanceBalance(
                asset="ETH",
                free=1.0,
                locked=0.5,
            ),
        ]

        prices = {
            "BTC": 100000.0,
            "ETH": 4000.0,
        }

        positions = adapter.balances_to_positions_with_prices(
            balances,
            prices,
        )

        self.assertEqual(len(positions), 2)

        self.assertEqual(positions[0].symbol, "BTC")
        self.assertEqual(positions[0].value, 60000.0)

        self.assertEqual(positions[1].symbol, "ETH")
        self.assertEqual(positions[1].value, 6000.0)

if __name__ == "__main__":
    unittest.main()
