def build_trip_prompt(
    start_city,
    budget,
    days,
    travel_style,
    interests,
):
    """Create a travel-planning prompt."""

    return f"""
Plan an India trip.

Starting City: {start_city}

Budget: ₹{budget}

Duration: {days} days

Travel Style: {travel_style}

Interests: {", ".join(interests)}

Generate:
- Day-wise itinerary
- Budget suggestions
- Attractions
- Food recommendations
- Travel tips
"""