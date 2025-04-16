from argparse import ArgumentParser, Namespace

import config
import utils


def run(color: str, print_only: bool = False) -> bool:
    index: int = config.BELT_COLORS.index(color)
    calculations_number: int = config.CALCULATION_NUMBERS[index]
    tables_to_do: list[int] = utils.get_tables_to_do(tables=config.BELTS[0 : index + 1])
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
            calculations=calculations, limit_seconds=config.LIMIT_TIME_SECONDS
        )

    return True


def main() -> None:
    parser = ArgumentParser(
        description="ARJ Multiplication Tables Trainer CLI",
    )

    parser.add_argument(
        "--color",
        type=str,
        choices=config.BELT_COLORS + ["all"],
        default=config.BELT_COLORS[0],
    )
    parser.add_argument("--print-only", action="store_true")

    args: Namespace = parser.parse_args()

    for color in config.BELT_COLORS if args.color == "all" else [args.color]:
        if not run(color=color, print_only=args.print_only):
            print("Nope! You failed... 💔")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCanceled... You failed! 👎")
