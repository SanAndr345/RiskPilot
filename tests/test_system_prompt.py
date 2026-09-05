import unittest

from riskpilot.system_prompt import SYSTEM_PROMPT


class TestSystemPrompt(unittest.TestCase):

    def test_prompt_exists(self):
        self.assertTrue(SYSTEM_PROMPT.strip())

    def test_prompt_contains_risk_rules(self):
        self.assertIn("risk assessment", SYSTEM_PROMPT)
        self.assertIn("REDUCE_CONCENTRATION", SYSTEM_PROMPT)
        self.assertIn("MONITOR", SYSTEM_PROMPT)
        self.assertIn("NO_ACTION", SYSTEM_PROMPT)

    def test_prompt_requires_confirmation(self):
        self.assertIn("Ask for confirmation", SYSTEM_PROMPT)


if __name__ == "__main__":
    unittest.main()
