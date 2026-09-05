from riskpilot.binance.adapter import BinanceAdapter
from riskpilot.audit.auditor import PortfolioAudit, audit_portfolio


class AgentOSBridge:
    """
    Bridge between Binance AgentOS/MCP responses
    and the RiskPilot risk engine.

    This bridge does not call Binance directly.
    It receives AgentOS tool responses and converts
    them into RiskPilot portfolio data.
    """

    def __init__(self):
        self.adapter = BinanceAdapter()

    def build_portfolio_audit(
        self,
        account_response,
        ticker_response=None,
    ) -> PortfolioAudit:
        """
        Convert AgentOS account data into a RiskPilot portfolio audit.
        """

        balances = self.adapter.parse_spot_account(account_response)

        if not balances:
            return audit_portfolio([])

        prices = self.adapter.parse_ticker_prices(
            ticker_response or []
        )

        positions = self.adapter.balances_to_positions_with_prices(
            balances,
            prices,
        )

        return audit_portfolio(positions)
