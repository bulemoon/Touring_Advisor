from typing import Any


def update_cart(
    user_id: int,
    action: str,
    product_name: str,
    quantity: int = 1,
) -> dict[str, Any]:
    """
    Update shopping cart. Actions: add, remove, update_quantity.

    Args:
        user_id: User ID
        action: One of add, remove, update_quantity
        product_name: Product name
        quantity: Quantity for add/update actions

    Returns:
        {"success": bool, "data": dict, "error": str}
    """
    return {
        "success": True,
        "data": {"user_id": user_id, "action": action, "product_name": product_name, "quantity": quantity},
        "error": None,
    }
