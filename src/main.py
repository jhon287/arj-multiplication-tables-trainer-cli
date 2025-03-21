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

    args: Namespace = parser.parse_args()

    index: int = config.BELT_COLORS.index(args.color)
    calculations_number: int = config.CALCULATION_NUMBERS[index]
    tables_to_do: list[int] = utils.get_tables_to_do(tables=config.BELTS[0 : index + 1])
    calculations: list[str] = utils.get_calculations(
        tables=tables_to_do, number=calculations_number
    )

    utils.print_calculations(calculations=calculations)


if __name__ == "__main__":
    main()
