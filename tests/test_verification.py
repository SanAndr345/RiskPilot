import unittest

from riskpilot.verification.verifier import verify_execution


class TestVerification(unittest.TestCase):

    def test_matching_value_is_verified(self):
        result = verify_execution(
            symbol="BTC",
            expected_value=-1000.0,
            actual_value=-1000.0,
        )

        self.assertEqual(result.status, "VERIFIED")
        self.assertEqual(result.difference, 0.0)

    def test_small_difference_within_tolerance_is_verified(self):
        result = verify_execution(
            symbol="BTC",
            expected_value=-1000.0,
            actual_value=-1000.005,
            tolerance=0.01,
        )

        self.assertEqual(result.status, "VERIFIED")

    def test_large_difference_fails(self):
        result = verify_execution(
            symbol="BTC",
            expected_value=-1000.0,
            actual_value=-900.0,
        )

        self.assertEqual(result.status, "FAILED")
        self.assertEqual(result.difference, 100.0)


if __name__ == "__main__":
    unittest.main()
