import unittest

from riskpilot.risk.portfolio import Position
from riskpilot.risk.engine import assess_concentration


class TestConcentrationRisk(unittest.TestCase):

    def test_high_risk(self):
        result = assess_concentration([
            Position("BTC", 6000),
            Position("ETH", 4000),
        ])

        self.assertEqual(result.concentration_risk, "HIGH")
        self.assertEqual(result.largest_position, "BTC")
        self.assertEqual(result.largest_weight, 0.6)

    def test_medium_risk(self):
        result = assess_concentration([
            Position("BTC", 4000),
            Position("ETH", 3500),
            Position("SOL", 2500),
        ])

        self.assertEqual(result.concentration_risk, "MEDIUM")
        self.assertEqual(result.largest_weight, 0.4)

    def test_low_risk(self):
        result = assess_concentration([
            Position("BTC", 2500),
            Position("ETH", 2500),
            Position("SOL", 2500),
            Position("BNB", 2500),
        ])

        self.assertEqual(result.concentration_risk, "LOW")
        self.assertEqual(result.largest_weight, 0.25)

    def test_empty_portfolio(self):
        result = assess_concentration([])

        self.assertEqual(result.concentration_risk, "LOW")
        self.assertEqual(result.total_value, 0)

    def test_zero_value_portfolio(self):
        result = assess_concentration([
            Position("BTC", 0),
            Position("ETH", 0),
        ])

        self.assertEqual(result.concentration_risk, "LOW")
        self.assertEqual(result.total_value, 0)


if __name__ == "__main__":
    unittest.main()
