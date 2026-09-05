from dataclasses import dataclass


@dataclass
class BinanceBalance:
    asset: str
    free: float
    locked: float


class BinanceAdapter:
    """
    Read-only interface for Binance account data.

    Execution methods will be added in later phases.
    """

    def get_balances(self) -> list[BinanceBalance]:
        """
        Return Binance account balances.

        This is intentionally not connected to Binance yet.
        The real AgentOS/MCP integration will be wired in later.
        """
        return []
