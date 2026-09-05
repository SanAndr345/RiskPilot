import unittest

from riskpilot.audit.auditor import audit_portfolio
from riskpilot.risk.portfolio import Position


class TestPortfolioAudit(unittest.TestCase):

    def test_high_risk_audit(self):
        positions = [
            Position(symbol="BTC", value=6000),
            Position(symbol="ETH", value=4000),
        ]

        result = audit_portfolio(positions)

        self.assertEqual(result.total_value, 10000)
        self.assertEqual(result.largest_position, "BTC")
        self.assertEqual(result.largest_weight, 0.6)
        self.assertEqual(result.concentration_risk, "HIGH")
        self.assertEqual(result.action, "REDUCE_CONCENTRATION")

    def test_low_risk_audit(self):
        positions = [
            Position(symbol="BTC", value=2500),
            Position(symbol="ETH", value=2500),
            Position(symbol="SOL", value=2500),
            Position(symbol="BNB", value=2500),
        ]

        result = audit_portfolio(positions)

        self.assertEqual(result.total_value, 10000)
        self.assertEqual(result.largest_position, "BTC")
        self.assertEqual(result.largest_weight, 0.25)
        self.assertEqual(result.concentration_risk, "LOW")
        self.assertEqual(result.action, "NO_ACTION")


if __name__ == "__main__":
    unittest.main()
