def basic_packing_list(season: str):
    """Return a simple packing checklist based on season."""

    common = [
        "Phone Charger",
        "Identity Card",
        "Power Bank",
        "Wallet",
        "Medicines",
        "Toiletries",
    ]

    if season.lower() == "winter":
        return common + [
            "Jacket",
            "Sweater",
            "Thermal Wear",
            "Gloves",
        ]

    if season.lower() == "summer":
        return common + [
            "Cotton Clothes",
            "Sunglasses",
            "Hat",
            "Sunscreen",
        ]

    if season.lower() == "monsoon":
        return common + [
            "Umbrella",
            "Raincoat",
            "Waterproof Shoes",
        ]

    return common