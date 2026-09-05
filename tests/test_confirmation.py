import unittest

from riskpilot.confirmation.gate import (
    confirm_action,
    create_confirmation_request,
)


class TestConfirmationGate(unittest.TestCase):

    def test_request_starts_unconfirmed(self):
        request = create_confirmation_request(
            action="REDUCE",
            description="Reduce BTC concentration from 60% to 50%.",
        )

        self.assertEqual(request.action, "REDUCE")
        self.assertEqual(
            request.description,
            "Reduce BTC concentration from 60% to 50%.",
        )
        self.assertFalse(request.confirmed)

    def test_confirm_action(self):
        request = create_confirmation_request(
            action="REDUCE",
            description="Reduce BTC concentration.",
        )

        confirm_action(request)

        self.assertTrue(request.confirmed)

    def test_confirmation_does_not_change_action(self):
        request = create_confirmation_request(
            action="REDUCE",
            description="Reduce BTC concentration.",
        )

        confirm_action(request)

        self.assertEqual(request.action, "REDUCE")


if __name__ == "__main__":
    unittest.main()
