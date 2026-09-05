import unittest

from riskpilot.agentos.bridge import AgentOSBridge


class TestAgentOSBridge(unittest.TestCase):

    def setUp(self):
        self.bridge = AgentOSBridge()

    def test_empty_spot_account(self):
        account_response = {
            "balances": []
        }

        audit = self.bridge.build_portfolio_audit(
            account_response
        )

        self.assertEqual(audit.total_value, 0)
        self.assertEqual(audit.concentration_risk, "LOW")
        self.assertEqual(audit.action, "NO_ACTION")

    def test_build_audit_from_agentos_response(self):
        account_response = {
            "balances": [
                {
                    "asset": "BTC",
                    "free": "0.1",
                    "locked": "0.0",
                },
                {
                    "asset": "ETH",
                    "free": "1.0",
                    "locked": "0.0",
                },
            ]
        }

        ticker_response = [
            {
                "symbol": "BTCUSDT",
                "price": "60000",
            },
            {
                "symbol": "ETHUSDT",
                "price": "4000",
            },
        ]

        audit = self.bridge.build_portfolio_audit(
            account_response,
            ticker_response,
        )

        self.assertEqual(audit.total_value, 10000)
        self.assertEqual(audit.largest_position, "BTC")
        self.assertAlmostEqual(audit.largest_weight, 0.60)
        self.assertEqual(audit.concentration_risk, "HIGH")
        self.assertEqual(audit.action, "REDUCE_CONCENTRATION")

    def test_missing_price_is_ignored(self):
        account_response = {
            "balances": [
                {
                    "asset": "BTC",
                    "free": "0.1",
                    "locked": "0.0",
                },
                {
                    "asset": "XYZ",
                    "free": "100",
                    "locked": "0.0",
                },
            ]
        }

        ticker_response = [
            {
                "symbol": "BTCUSDT",
                "price": "60000",
            },
        ]

        audit = self.bridge.build_portfolio_audit(
            account_response,
            ticker_response,
        )

        self.assertEqual(audit.total_value, 6000)
        self.assertEqual(audit.largest_position, "BTC")


if __name__ == "__main__":
    unittest.main()
