import builtins
from random import randint
from unittest import TestCase, mock

import utils


class TestUtils(TestCase):
    def test_check_answer(self):
        for _ in range(5):
            nbr_1: int = randint(0, 10)
            nbr_2: int = randint(0, 10)
            self.assertTrue(
                expr=utils.check_answer(a=nbr_1, b=nbr_2, anwser=nbr_1 * nbr_2)
            )

    def test_check_elapsed_time(self):
        self.assertTrue(expr=utils.check_elapsed_time(elapsed=10, limit=60))
        self.assertTrue(expr=utils.check_elapsed_time(elapsed=60, limit=60))
        self.assertFalse(expr=utils.check_elapsed_time(elapsed=61, limit=60))

    def test_get_emoji_color(self):
        self.assertEqual(first=utils.get_emoji_color(color="white"), second="⚪️")
        self.assertEqual(first=utils.get_emoji_color(color="orange"), second="🟠")
        self.assertEqual(first=utils.get_emoji_color(color="brown"), second="🟤")

    def test_get_calculations_number(self):
        self.assertEqual(
            first=utils.get_calculations_number(belt_color="white"), second=8
        )
        self.assertEqual(
            first=utils.get_calculations_number(belt_color="orange"), second=8
        )
        self.assertEqual(
            first=utils.get_calculations_number(belt_color="brown"), second=20
        )

    def test_get_tables_to_do(self):
        self.assertEqual(
            first=utils.get_tables_to_do(belt_color="white"), second=[2, 10]
        )
        self.assertEqual(
            first=utils.get_tables_to_do(belt_color="orange"), second=[2, 3, 5, 10]
        )
        self.assertEqual(
            first=utils.get_tables_to_do(belt_color="brown"),
            second=[2, 3, 4, 5, 6, 7, 8, 9, 10],
        )

    def test_get_calculations(self):
        tables: list[int] = [2, 3, 5, 10]
        number: int = 22
        calculations: list[tuple[int, int]] = utils.get_calculations(
            tables=tables, number=number
        )
        calculation_tables: set[int] = set([table for _, table in calculations])

        self.assertEqual(first=len(calculations), second=number)
        self.assertEqual(first=sorted(list(calculation_tables)), second=sorted(tables))

    def test_ask_answer(self):
        nbr_1: int = 2
        nbr_2: int = 3
        with mock.patch.object(builtins, "input", lambda _: "6"):
            self.assertEqual(
                first=utils.ask_answer(a=nbr_1, b=nbr_2), second=nbr_1 * nbr_2
            )

    def test_prompt_calculation(self):
        nbr_1: int = 2
        nbr_2: int = 3
        with mock.patch.object(builtins, "input", lambda _: "6"):
            self.assertTrue(expr=utils.prompt_calculation(a=nbr_1, b=nbr_2))
            self.assertFalse(expr=utils.prompt_calculation(a=1, b=3))
