import unittest

from riskpilot.binance.adapter import BinanceAdapter


class TestBinanceAdapter(unittest.TestCase):

    def test_adapter_returns_empty_balances(self):
        adapter = BinanceAdapter()

        balances = adapter.get_balances()

        self.assertEqual(balances, [])


if __name__ == "__main__":
    unittest.main()
