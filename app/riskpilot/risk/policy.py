
from dataclasses import dataclass


@dataclass
class RiskPolicy:
    action: str
    reason: str


def determine_policy(concentration_risk: str) -> RiskPolicy:
    if concentration_risk == "HIGH":
        return RiskPolicy(
            action="REDUCE_CONCENTRATION",
            reason="Largest position exceeds the high-risk concentration limit.",
        )

    if concentration_risk == "MEDIUM":
        return RiskPolicy(
            action="MONITOR",
            reason="Portfolio concentration is elevated but within the high-risk threshold.",
        )

    return RiskPolicy(
        action="NO_ACTION",
        reason="Portfolio concentration is within the acceptable range.",
    )