import unittest

from riskpilot.execution.executor import (
    create_execution_request,
    execute_request,
)


class TestExecution(unittest.TestCase):

    def test_execution_request_starts_unconfirmed(self):
        request = create_execution_request(
            symbol="BTC",
            action="REDUCE",
            value=-1000.0,
            reason="Reduce BTC concentration from 60% to 50%.",
        )

        self.assertEqual(request.symbol, "BTC")
        self.assertEqual(request.action, "REDUCE")
        self.assertEqual(request.value, -1000.0)
        self.assertFalse(request.confirmed)

    def test_unconfirmed_request_is_blocked(self):
        request = create_execution_request(
            symbol="BTC",
            action="REDUCE",
            value=-1000.0,
            reason="Reduce BTC concentration.",
        )

        result = execute_request(request)

        self.assertEqual(result.status, "BLOCKED")

    def test_confirmed_request_is_ready(self):
        request = create_execution_request(
            symbol="BTC",
            action="REDUCE",
            value=-1000.0,
            reason="Reduce BTC concentration.",
        )

        request.confirmed = True

        result = execute_request(request)

        self.assertEqual(result.status, "READY")
        self.assertEqual(result.symbol, "BTC")
        self.assertEqual(result.action, "REDUCE")


if __name__ == "__main__":
    unittest.main()
