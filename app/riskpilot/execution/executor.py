from dataclasses import dataclass


@dataclass
class ExecutionRequest:
    symbol: str
    action: str
    value: float
    reason: str
    confirmed: bool = False


@dataclass
class ExecutionResult:
    symbol: str
    action: str
    value: float
    status: str
    message: str


def create_execution_request(
    symbol: str,
    action: str,
    value: float,
    reason: str,
) -> ExecutionRequest:
    """
    Create an execution request from a rebalance proposal.

    This function does not execute any trade.
    """
    return ExecutionRequest(
        symbol=symbol,
        action=action,
        value=value,
        reason=reason,
        confirmed=False,
    )


def execute_request(request: ExecutionRequest) -> ExecutionResult:
    """
    Execute a confirmed request.

    Actual Binance execution will be connected later.
    """
    if not request.confirmed:
        return ExecutionResult(
            symbol=request.symbol,
            action=request.action,
            value=request.value,
            status="BLOCKED",
            message="Execution requires user confirmation.",
        )

    return ExecutionResult(
        symbol=request.symbol,
        action=request.action,
        value=request.value,
        status="READY",
        message="Request is confirmed and ready for Binance execution.",
    )
