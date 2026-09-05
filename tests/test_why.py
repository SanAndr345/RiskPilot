import unittest

from riskpilot.why.explainer import explain_concentration_risk
from riskpilot.audit.auditor import audit_portfolio
from riskpilot.risk.portfolio import Position


class TestWhyExplainer(unittest.TestCase):

    def test_explains_high_risk(self):
        positions = [
            Position("BTC", 6000),
            Position("ETH", 2500),
            Position("SOL", 1500),
        ]

        audit = audit_portfolio(positions)
        explanation = explain_concentration_risk(audit)

        self.assertIn("BTC", explanation)
        self.assertIn("60.00%", explanation)
        self.assertIn("50%", explanation)
        self.assertIn("high-risk", explanation)

    def test_explains_medium_risk(self):
        positions = [
            Position("BTC", 4000),
            Position("ETH", 3500),
            Position("SOL", 2500),
        ]

        audit = audit_portfolio(positions)
        explanation = explain_concentration_risk(audit)

        self.assertIn("BTC", explanation)
        self.assertIn("40.00%", explanation)
        self.assertIn("elevated concentration", explanation)

    def test_explains_low_risk(self):
        positions = [
            Position("BTC", 2500),
            Position("ETH", 2500),
            Position("SOL", 2500),
            Position("BNB", 2500),
        ]

        audit = audit_portfolio(positions)
        explanation = explain_concentration_risk(audit)

        self.assertIn("25.00%", explanation)
        self.assertIn("acceptable range", explanation)

    def test_explains_empty_portfolio(self):
        audit = audit_portfolio([])
        explanation = explain_concentration_risk(audit)

        self.assertIn("N/A", explanation)
        self.assertIn("acceptable range", explanation)


if __name__ == "__main__":
    unittest.main()
