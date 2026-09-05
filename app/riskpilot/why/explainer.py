def explain_concentration_risk(audit):
    """
    Explain why RiskPilot assigned the current concentration risk.
    """

    if audit.concentration_risk == "HIGH":
        return (
            f"{audit.largest_position} represents "
            f"{audit.largest_weight:.2%} of the portfolio. "
            "This exceeds the 50% high-risk concentration limit. "
            "A large allocation to one position can make the portfolio "
            "more vulnerable to a significant loss if that asset declines."
        )

    if audit.concentration_risk == "MEDIUM":
        return (
            f"{audit.largest_position} represents "
            f"{audit.largest_weight:.2%} of the portfolio. "
            "This indicates elevated concentration, but it remains below "
            "the high-risk threshold. RiskPilot recommends monitoring "
            "the position rather than immediately reducing it."
        )

    return (
        f"The largest position is {audit.largest_position or 'N/A'} at "
        f"{audit.largest_weight:.2%} of the portfolio. "
        "The concentration level is within the acceptable range, "
        "so no concentration risk action is required."
    )
