def calculate_budget_split(total_budget: float):
    """Return a suggested budget allocation."""

    return {
        "Accommodation": total_budget * 0.40,
        "Food": total_budget * 0.20,
        "Transport": total_budget * 0.20,
        "Activities": total_budget * 0.15,
        "Miscellaneous": total_budget * 0.05,
    }


def calculate_remaining_budget(total_budget, spent):
    """Return remaining budget."""

    return total_budget - spent