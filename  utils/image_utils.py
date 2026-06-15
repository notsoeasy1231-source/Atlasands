from pathlib import Path
import random


def get_random_hero_image():
    """Return a random hero image path."""
    hero_dir = Path("assets/hero")

    if not hero_dir.exists():
        return None

    images = (
        list(hero_dir.glob("*.jpg"))
        + list(hero_dir.glob("*.jpeg"))
        + list(hero_dir.glob("*.png"))
    )

    if not images:
        return None

    return str(random.choice(images))


def get_destination_image(destination_name: str):
    """
    Return the expected image path for a destination.
    """
    return f"assets/destinations/{destination_name}.jpg"