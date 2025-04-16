from random import choice, shuffle
from time import perf_counter
from config import BELT_EMOJI_COLORS


def get_tables_to_do(tables: list[list[int] | int]) -> list[int]:
    tables_to_do: list[int] = []

    for table in tables:
        if isinstance(table, list):
            tables_to_do += table
            # for t in table:
            #     tables_to_do.append(t)
        else:
            tables_to_do.append(table)

    return tables_to_do


def get_calculations(tables: list[int], number: int = 10) -> list[tuple[int, int]]:
    calculations: list[tuple[int, int]] = []

    table_multiplicators: dict[int, list[int]] = {
        table: list(range(0, 11)) for table in tables
    }

    while number > 0:
        random_table: int = choice(list(table_multiplicators.keys()))
        random_multiplicator: int = choice(table_multiplicators[random_table])
        calculations.append((random_multiplicator, random_table))
        table_multiplicators[random_table].remove(random_multiplicator)
        number = number - 1

    shuffle(calculations)

    return list(set(calculations))


def print_calculations(calculations: list[tuple[int, int]], egal_sign: bool = True):
    for calculation in calculations:
        multiplicator, table = calculation
        print(f"{multiplicator:>2} x {table:>2}{' =' if egal_sign else ''}")


def ask_answer(a: int, b: int) -> int:
    return int(input(f"{a:>2} x {b:>2} = ").strip())


def check_answer(a: int, b: int, anwser: int) -> bool:
    return a * b == anwser


def prompt_calculation(a: int, b: int) -> bool:
    return check_answer(a=a, b=b, anwser=ask_answer(a=a, b=b))


def check_elapsed_time(elapsed: int, limit: int) -> bool:
    return elapsed <= limit


def print_result(
    ok: list[tuple[int, int]], nok: list[tuple[int, int]], time: int, limit_seconds: int
) -> None:
    nbr_ok: int = len(ok)
    nbr_nok: int = len(nok)
    nbr_total: int = nbr_ok + nbr_nok

    print(30 * "-")
    print(f"Result: {nbr_ok}/{nbr_total} ({(nbr_ok / nbr_total):.2%})")
    print(
        f"Time: {time}s of {limit_seconds}s ({'OK' if check_elapsed_time(elapsed=time, limit=limit_seconds) else 'NOK'})"
    )

    if nbr_ok == nbr_total and check_elapsed_time(elapsed=time, limit=limit_seconds):
        print("You win! 🏆🎉")

    if len(nok) > 0:
        print("NOK:")
        for calculation in nok:
            a, b = calculation
            print(f"  {a:>2} x {b:>2}")


def play_game(calculations: list[tuple[int, int]], limit_seconds: int) -> None:
    ok: list[tuple[int, int]] = []
    nok: list[tuple[int, int]] = []

    start: float = perf_counter()

    for calculation in calculations:
        multiplicator, table = calculation
        if prompt_calculation(a=multiplicator, b=table):
            ok.append(calculation)
        else:
            nok.append(calculation)

    end: float = perf_counter()

    elaspsed_time: int = int(round(number=abs(start - end), ndigits=0))

    print_result(ok=ok, nok=nok, time=elaspsed_time, limit_seconds=limit_seconds)


def get_emoji_color(color: str) -> str:
    return BELT_EMOJI_COLORS[color]
