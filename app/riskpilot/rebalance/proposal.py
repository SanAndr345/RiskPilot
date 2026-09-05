from dataclasses import dataclass

from riskpilot.risk.portfolio import Position


@dataclass
class RebalanceProposal:
    symbol: str
    current_weight: float
    target_weight: float
    action: str
    value_change: float


def create_rebalance_proposal(
    positions: list[Position],
    target_max_weight: float = 0.50,
) -> list[RebalanceProposal]:
    """
    Create a proposal to reduce positions that exceed the target weight.

    This function does not execute any trade.
    """

    total_value = sum(position.value for position in positions)

    if total_value <= 0:
        return []

    proposals = []

    for position in positions:
        current_weight = position.value / total_value

        if current_weight > target_max_weight:
            target_value = total_value * target_max_weight
            value_change = target_value - position.value

            proposals.append(
                RebalanceProposal(
                    symbol=position.symbol,
                    current_weight=current_weight,
                    target_weight=target_max_weight,
                    action="REDUCE",
                    value_change=value_change,
                )
            )

    return proposals
