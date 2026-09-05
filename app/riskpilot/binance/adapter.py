from dataclasses import dataclass
from typing import Any

from riskpilot.risk.portfolio import Position

@dataclass
class BinanceBalance:
    asset: str
    free: float
    locked: float


class BinanceAdapter:
    """
    Read-only interface for Binance AgentOS/MCP data.

    This adapter defines the interface RiskPilot expects.
    Actual MCP tool calls are supplied by the connected agent.
    """

    def parse_spot_account(self, response: Any) -> list[BinanceBalance]:
        """
        Convert the Binance spot.getAccount response
        into RiskPilot balance objects.
        """
        balances = response.get("balances", []) if isinstance(response, dict) else []

        return [
            BinanceBalance(
                asset=item["asset"],
                free=float(item["free"]),
                locked=float(item["locked"]),
            )
            for item in balances
            if float(item.get("free", 0)) > 0
            or float(item.get("locked", 0)) > 0
        ]

    def balances_to_positions(
        self, balances: list[BinanceBalance]
    ) -> list[Position]:
        """
        Convert Binance balances into RiskPilot positions.
        """
        return [
            Position(
                symbol=balance.asset,
                value=balance.free + balance.locked,
            )
            for balance in balances
        ]

    def get_balances(self) -> list[BinanceBalance]:
        """
        Placeholder for the actual AgentOS/MCP call.

        The connected agent will call:
        spot.getAccount
        """
        return []
