def format_risk_report(audit, stress=None, proposals=None):
    """
    Format RiskPilot results into a clean human-readable report.
    """

    lines = [
        "╔══════════════════════════════════════╗",
        "║          RISK PILOT REPORT           ║",
        "╚══════════════════════════════════════╝",
        "",
        "PORTFOLIO RISK",
        f"Total Value       : ${audit.total_value:,.2f}",
        f"Largest Position : {audit.largest_position or 'N/A'}",
        f"Largest Weight    : {audit.largest_weight:.2%}",
        f"Risk Level        : {audit.concentration_risk}",
        f"Recommended Action: {audit.action}",
    ]

    if stress is not None:
        lines.extend([
            "",
            "STRESS TEST",
            f"Scenario          : {stress.scenario}",
            f"Stressed Value    : ${stress.stressed_value:,.2f}",
            f"Potential Loss    : ${stress.loss:,.2f}",
            f"Loss              : {stress.loss_percent:.2f}%",
        ])

    if proposals:
        lines.extend([
            "",
            "REBALANCE PROPOSAL",
        ])

        for proposal in proposals:
            lines.append(
                f"- {proposal.symbol}: "
                f"{proposal.current_weight:.2%} -> "
                f"{proposal.target_weight:.2%} "
                f"({proposal.action})"
            )

    lines.extend([
        "",
        "STATUS: REVIEW REQUIRED",
    ])

    return "\n".join(lines)
