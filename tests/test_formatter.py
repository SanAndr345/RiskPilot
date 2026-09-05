import unittest

from riskpilot.report.formatter import format_risk_report
from riskpilot.audit.auditor import audit_portfolio
from riskpilot.risk.portfolio import Position
from riskpilot.stress.stress_test import run_stress_test
from riskpilot.rebalance.proposal import create_rebalance_proposal


class TestRiskReportFormatter(unittest.TestCase):

    def setUp(self):
        self.positions = [
            Position("BTC", 6000),
            Position("ETH", 2500),
            Position("SOL", 1500),
        ]

        self.audit = audit_portfolio(self.positions)

    def test_report_contains_risk_information(self):
        report = format_risk_report(self.audit)

        self.assertIn("RISK PILOT REPORT", report)
        self.assertIn("PORTFOLIO RISK", report)
        self.assertIn("BTC", report)
        self.assertIn("60.00%", report)
        self.assertIn("HIGH", report)
        self.assertIn("REDUCE_CONCENTRATION", report)

    def test_report_contains_stress_test(self):
        stress = run_stress_test(self.positions, 20)

        report = format_risk_report(
            self.audit,
            stress,
        )

        self.assertIn("STRESS TEST", report)
        self.assertIn("20.0%", report)
        self.assertIn("$8,000.00", report)
        self.assertIn("$2,000.00", report)

    def test_report_contains_rebalance_proposal(self):
        proposals = create_rebalance_proposal(self.positions)

        report = format_risk_report(
            self.audit,
            proposals=proposals,
        )

        self.assertIn("REBALANCE PROPOSAL", report)
        self.assertIn("BTC", report)
        self.assertIn("REDUCE", report)

    def test_report_without_optional_sections(self):
        report = format_risk_report(self.audit)

        self.assertNotIn("STRESS TEST", report)
        self.assertNotIn("REBALANCE PROPOSAL", report)
        self.assertIn("STATUS: REVIEW REQUIRED", report)


if __name__ == "__main__":
    unittest.main()
