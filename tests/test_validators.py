"""Pruebas de las validaciones de reglas de negocio."""

import unittest
from datetime import date
from decimal import Decimal

from vepo.utils.validators import (
    calculate_closing_total,
    validate_amount,
    validate_period,
    validate_username,
)


class ValidatorsTest(unittest.TestCase):
    def test_amount_must_be_positive(self):
        self.assertEqual(validate_amount(Decimal("40")), Decimal("40"))
        for bad in (Decimal("0"), Decimal("-5")):
            with self.assertRaises(ValueError):
                validate_amount(bad)

    def test_username_format(self):
        self.assertEqual(validate_username("  empleado2 "), "empleado2")
        for bad in ("abc", "Mayus1", "con espacio", "x" * 31):
            with self.assertRaises(ValueError):
                validate_username(bad)

    def test_period_order(self):
        validate_period(date(2026, 10, 1), date(2026, 10, 15))
        validate_period(date(2026, 10, 1), date(2026, 10, 1))
        with self.assertRaises(ValueError):
            validate_period(date(2026, 10, 16), date(2026, 10, 15))

    def test_closing_total_is_window_plus_route(self):
        total = calculate_closing_total(Decimal("1160.00"), Decimal("895.00"))
        self.assertEqual(total, Decimal("2055.00"))
        with self.assertRaises(ValueError):
            calculate_closing_total(Decimal("-1"), Decimal("0"))


if __name__ == "__main__":
    unittest.main()
