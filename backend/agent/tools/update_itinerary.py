from typing import Any


def update_itinerary(
    user_id: int,
    action: str,
    route_id: int,
    date: str,
    stop_name: str = "",
) -> dict[str, Any]:
    """
    Update user itinerary. Actions: add_stop, remove_stop, reorder, change_date.

    Args:
        user_id: User ID
        action: One of add_stop, remove_stop, reorder, change_date
        route_id: Tour route ID
        date: Travel date (YYYY-MM-DD)
        stop_name: Stop name for add/remove actions

    Returns:
        {"success": bool, "data": dict, "error": str}
    """
    return {
        "success": True,
        "data": {"user_id": user_id, "action": action, "route_id": route_id, "date": date},
        "error": None,
    }
