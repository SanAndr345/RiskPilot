from riskpilot.risk.portfolio import Position
from riskpilot.audit.auditor import audit_portfolio
from riskpilot.stress.stress_test import run_stress_test
from riskpilot.rebalance.proposal import create_rebalance_proposal
from riskpilot.confirmation.gate import create_confirmation_request, confirm_action
from riskpilot.execution.executor import create_execution_request, execute_request
from riskpilot.verification.verifier import verify_execution


def main():
    positions = [
        Position(symbol="BTC", value=6000),
        Position(symbol="ETH", value=2500),
        Position(symbol="SOL", value=1500),
    ]

    print("=== RiskPilot Demo ===")

    audit = audit_portfolio(positions)

    print("\n[1] RISK AUDIT")
    print(f"Total value: ${audit.total_value:,.2f}")
    print(f"Largest position: {audit.largest_position}")
    print(f"Largest weight: {audit.largest_weight:.2%}")
    print(f"Concentration risk: {audit.concentration_risk}")
    print(f"Action: {audit.action}")

    print("\n[2] STRESS TEST")
    stress = run_stress_test(positions, price_drop_percent=20)

    print(f"Scenario: {stress.scenario}")
    print(f"Original value: ${stress.original_value:,.2f}")
    print(f"Stressed value: ${stress.stressed_value:,.2f}")
    print(f"Loss: ${stress.loss:,.2f}")
    print(f"Loss percent: {stress.loss_percent:.2f}%")

    print("\n[3] REBALANCE PROPOSAL")
    proposals = create_rebalance_proposal(
        positions,
        target_max_weight=0.50,
    )

    for proposal in proposals:
        print(
            f"{proposal.symbol}: "
            f"{proposal.current_weight:.2%} -> "
            f"{proposal.target_weight:.2%}, "
            f"action={proposal.action}, "
            f"value_change=${proposal.value_change:,.2f}"
        )

    if not proposals:
        print("No rebalance required.")
        return

    proposal = proposals[0]

    print("\n[4] CONFIRMATION GATE")
    confirmation = create_confirmation_request(
        action=proposal.action,
        description=(
            f"Reduce {proposal.symbol} by "
            f"${abs(proposal.value_change):,.2f}"
        ),
    )

    print(f"Action: {confirmation.action}")
    print(f"Description: {confirmation.description}")
    print(f"Confirmed: {confirmation.confirmed}")

    confirmation = confirm_action(confirmation)

    print(f"Confirmed: {confirmation.confirmed}")

    print("\n[5] EXECUTION")
    execution = create_execution_request(
        symbol=proposal.symbol,
        action=proposal.action,
        value=proposal.value_change,
        reason="Reduce portfolio concentration risk.",
    )

    execution.confirmed = confirmation.confirmed

    result = execute_request(execution)

    print(f"Status: {result.status}")
    print(f"Message: {result.message}")

    print("\n[6] VERIFICATION")
    verification = verify_execution(
        symbol=proposal.symbol,
        expected_value=proposal.value_change,
        actual_value=proposal.value_change,
    )

    print(f"Status: {verification.status}")
    print(f"Expected value: ${verification.expected_value:,.2f}")
    print(f"Actual value: ${verification.actual_value:,.2f}")
    print(f"Difference: ${verification.difference:,.2f}")
    print(f"Message: {verification.message}")

    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()
