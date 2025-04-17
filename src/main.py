from argparse import ArgumentParser, Namespace
from config import BELT_COLORS, LIMIT_TIME_SECONDS

import utils


def run(color: str, print_only: bool = False) -> bool:
    calculations_number: int = utils.get_calculations_number(belt_color=color)
    tables_to_do: list[int] = utils.get_tables_to_do(belt_color=color)
    calculations: list[tuple[int, int]] = utils.get_calculations(
        tables=tables_to_do, number=calculations_number
    )

    print(
        f"Belt Color: {utils.get_emoji_color(color=color)} "
        f"({str(color).capitalize()} - {calculations_number} of {sorted(tables_to_do)})"
    )

    if print_only:
        utils.print_calculations(calculations=calculations)
    else:
        return utils.play_game(
            calculations=calculations, limit_seconds=LIMIT_TIME_SECONDS
        )

    return True


def main() -> None:
    parser = ArgumentParser(
        description="ARJ Multiplication Tables Trainer CLI",
    )

    parser.add_argument(
        "--color",
        type=str,
        choices=BELT_COLORS + ["all"],
        default=BELT_COLORS[0],
    )
    parser.add_argument("--print-only", action="store_true")

    args: Namespace = parser.parse_args()

    for color in BELT_COLORS if args.color == "all" else [args.color]:
        if not run(color=color, print_only=args.print_only):
            print("Nope! You failed... 💔")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCanceled... You failed! 👎")
