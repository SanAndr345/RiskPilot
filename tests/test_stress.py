import unittest

from riskpilot.risk.portfolio import Position
from riskpilot.stress.stress_test import run_stress_test


class TestStressTest(unittest.TestCase):

    def test_ten_percent_drop(self):
        positions = [
            Position(symbol="BTC", value=6000),
            Position(symbol="ETH", value=4000),
        ]

        result = run_stress_test(positions, 10)

        self.assertEqual(result.original_value, 10000)
        self.assertEqual(result.stressed_value, 9000)
        self.assertEqual(result.loss, 1000)
        self.assertEqual(result.loss_percent, 10)
        self.assertEqual(result.scenario, "All positions drop 10.0%")

    def test_zero_value_portfolio(self):
        result = run_stress_test([], 20)

        self.assertEqual(result.original_value, 0)
        self.assertEqual(result.stressed_value, 0)
        self.assertEqual(result.loss, 0)
        self.assertEqual(result.loss_percent, 0)


if __name__ == "__main__":
    unittest.main()
