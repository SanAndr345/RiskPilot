from dataclasses import dataclass

from riskpilot.risk.engine import assess_concentration
from riskpilot.risk.portfolio import Position


@dataclass
class PortfolioAudit:
    total_value: float
    largest_position: str
    largest_weight: float
    concentration_risk: str
    action: str


def audit_portfolio(positions: list[Position]) -> PortfolioAudit:
    result = assess_concentration(positions)

    if result.concentration_risk == "HIGH":
        action = "REDUCE_CONCENTRATION"
    elif result.concentration_risk == "MEDIUM":
        action = "MONITOR"
    else:
        action = "NO_ACTION"

    return PortfolioAudit(
        total_value=result.total_value,
        largest_position=result.largest_position,
        largest_weight=result.largest_weight,
        concentration_risk=result.concentration_risk,
        action=action,
    )
