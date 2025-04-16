from argparse import ArgumentParser, Namespace

import config
import utils


def main():
    parser = ArgumentParser(
        description="ARJ Multiplication Tables Trainer CLI",
    )

    parser.add_argument(
        "--color", type=str, choices=config.BELT_COLORS, default=config.BELT_COLORS[0]
    )
    parser.add_argument("--print-only", action="store_true")

    args: Namespace = parser.parse_args()

    index: int = config.BELT_COLORS.index(args.color)
    calculations_number: int = config.CALCULATION_NUMBERS[index]
    tables_to_do: list[int] = utils.get_tables_to_do(tables=config.BELTS[0 : index + 1])
    calculations: list[tuple[int, int]] = utils.get_calculations(
        tables=tables_to_do, number=calculations_number
    )

    print(
        f"Belt Color: {utils.get_emoji_color(color=args.color)} "
        f"({str(args.color).capitalize()} - {calculations_number} of {sorted(tables_to_do)})"
    )

    if args.print_only:
        utils.print_calculations(calculations=calculations)
    else:
        utils.play_game(
            calculations=calculations, limit_seconds=config.LIMIT_TIME_SECONDS
        )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCanceled... You failed! 👎")
