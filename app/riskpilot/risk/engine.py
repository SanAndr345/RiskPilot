from dataclasses import dataclass

from riskpilot.risk.portfolio import Position, calculate_weights
from riskpilot.risk.risk_limits import (
    MAX_HIGH_RISK_WEIGHT,
    MAX_MEDIUM_RISK_WEIGHT,
)


@dataclass
class RiskResult:
    total_value: float
    largest_position: str
    largest_weight: float
    concentration_risk: str


def assess_concentration(positions: list[Position]) -> RiskResult:
    calculate_weights(positions)

    total_value = sum(position.value for position in positions)

    if not positions or total_value <= 0:
        return RiskResult(
            total_value=total_value,
            largest_position="",
            largest_weight=0.0,
            concentration_risk="LOW",
        )

    largest = max(positions, key=lambda position: position.weight)

    if largest.weight >= MAX_HIGH_RISK_WEIGHT:
        risk = "HIGH"
    elif largest.weight >= MAX_MEDIUM_RISK_WEIGHT:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return RiskResult(
        total_value=total_value,
        largest_position=largest.symbol,
        largest_weight=largest.weight,
        concentration_risk=risk,
    )