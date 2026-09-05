from dataclasses import dataclass


@dataclass
class VerificationResult:
    symbol: str
    expected_value: float
    actual_value: float
    difference: float
    status: str
    message: str


def verify_execution(
    symbol: str,
    expected_value: float,
    actual_value: float,
    tolerance: float = 0.01,
) -> VerificationResult:
    """
    Verify that the actual portfolio change matches the expected change.

    This function does not execute any trade.
    """

    difference = actual_value - expected_value

    if abs(difference) <= tolerance:
        return VerificationResult(
            symbol=symbol,
            expected_value=expected_value,
            actual_value=actual_value,
            difference=difference,
            status="VERIFIED",
            message="Execution result matches the expected value.",
        )

    return VerificationResult(
        symbol=symbol,
        expected_value=expected_value,
        actual_value=actual_value,
        difference=difference,
        status="FAILED",
        message="Execution result differs from the expected value.",
    )
