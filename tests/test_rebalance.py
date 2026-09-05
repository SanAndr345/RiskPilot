import unittest

from riskpilot.rebalance.proposal import create_rebalance_proposal
from riskpilot.risk.portfolio import Position


class TestRebalanceProposal(unittest.TestCase):

    def test_reduce_concentrated_position(self):
        positions = [
            Position(symbol="BTC", value=6000),
            Position(symbol="ETH", value=4000),
        ]

        proposals = create_rebalance_proposal(positions)

        self.assertEqual(len(proposals), 1)

        proposal = proposals[0]

        self.assertEqual(proposal.symbol, "BTC")
        self.assertEqual(proposal.current_weight, 0.6)
        self.assertEqual(proposal.target_weight, 0.5)
        self.assertEqual(proposal.action, "REDUCE")
        self.assertEqual(proposal.value_change, -1000)

    def test_no_rebalance_needed(self):
        positions = [
            Position(symbol="BTC", value=2500),
            Position(symbol="ETH", value=2500),
            Position(symbol="SOL", value=2500),
            Position(symbol="BNB", value=2500),
        ]

        proposals = create_rebalance_proposal(positions)

        self.assertEqual(proposals, [])

    def test_empty_portfolio(self):
        proposals = create_rebalance_proposal([])

        self.assertEqual(proposals, [])


if __name__ == "__main__":
    unittest.main()
