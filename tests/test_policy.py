import unittest

from riskpilot.risk.policy import determine_policy


class TestRiskPolicy(unittest.TestCase):

    def test_high_risk(self):
        result = determine_policy("HIGH")
        self.assertEqual(result.action, "REDUCE_CONCENTRATION")

    def test_medium_risk(self):
        result = determine_policy("MEDIUM")
        self.assertEqual(result.action, "MONITOR")

    def test_low_risk(self):
        result = determine_policy("LOW")
        self.assertEqual(result.action, "NO_ACTION")


if __name__ == "__main__":
    unittest.main()
