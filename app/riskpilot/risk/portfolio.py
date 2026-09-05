from dataclasses import dataclass


@dataclass
class Position:
    symbol: str
    value: float
    weight: float = 0.0


def calculate_weights(positions: list[Position]) -> list[Position]:
    total_value = sum(position.value for position in positions)

    if total_value <= 0:
        return positions

    for position in positions:
        position.weight = position.value / total_value

    return positions
