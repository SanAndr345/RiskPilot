from dataclasses import dataclass

from riskpilot.risk.portfolio import Position


@dataclass
class StressResult:
    scenario: str
    original_value: float
    stressed_value: float
    loss: float
    loss_percent: float


def run_stress_test(
    positions: list[Position],
    price_drop_percent: float,
) -> StressResult:
    original_value = sum(position.value for position in positions)

    drop_factor = 1 - (price_drop_percent / 100)
    stressed_value = original_value * drop_factor

    loss = original_value - stressed_value

    loss_percent = (
        (loss / original_value) * 100
        if original_value > 0
        else 0.0
    )

    return StressResult(
        scenario=f"All positions drop {price_drop_percent:.1f}%",
        original_value=original_value,
        stressed_value=stressed_value,
        loss=loss,
        loss_percent=loss_percent,
    )
