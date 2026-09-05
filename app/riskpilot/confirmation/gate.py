from dataclasses import dataclass


@dataclass
class ConfirmationRequest:
    action: str
    description: str
    confirmed: bool = False


def create_confirmation_request(
    action: str,
    description: str,
) -> ConfirmationRequest:
    """
    Create a confirmation request before a portfolio-changing action.

    This function does not execute any trade.
    """
    return ConfirmationRequest(
        action=action,
        description=description,
        confirmed=False,
    )


def confirm_action(request: ConfirmationRequest) -> ConfirmationRequest:
    """
    Mark an action as confirmed by the user.
    """
    request.confirmed = True
    return request
