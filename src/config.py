from typing import Final

TABLES: Final[list[list[int] | int]] = [[2, 10], 5, 3, 4, 6, 7, 8, 9]
LIMIT_TIME_SECONDS: Final[int] = 60
CALCULATION_NUMBERS: Final[list[int]] = [
    8,
    8,
    8,
    10,
    12,
    15,
    18,
    20,
]

BELT_EMOJI_COLORS: Final[dict[str, str]] = {
    "white": "⚪️",
    "yellow": "🟡",
    "orange": "🟠",
    "pink": "🩷",
    "green": "🟢",
    "blue": "🔵",
    "purple": "🟣",
    "brown": "🟤",
}

BELT_COLORS: Final[list[str]] = list(BELT_EMOJI_COLORS.keys())
