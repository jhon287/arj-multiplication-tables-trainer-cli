from random import choice, shuffle


def get_tables_to_do(tables: list[list[int] | int]) -> list[int]:
    tables_to_do: list[int] = []

    for table in tables:
        if isinstance(table, list):
            for t in table:
                tables_to_do.append(t)
        else:
            tables_to_do.append(table)

    return tables_to_do


def get_calculations(tables: list[int], number: int = 10) -> list[str]:
    calculations: list[str] = []

    table_multiplicators: dict[int, list[int]] = {
        table: list(range(0, 11)) for table in tables
    }

    while number > 0:
        random_table: int = choice(list(table_multiplicators.keys()))
        random_multiplicator: int = choice(table_multiplicators[random_table])
        calculations.append(f"{random_multiplicator:>2} x {random_table:>2} =")
        table_multiplicators[random_table].remove(random_multiplicator)
        number = number - 1

    shuffle(calculations)

    return calculations


def print_calculations(calculations: list[str]):
    for calculation in calculations:
        print(calculation)
