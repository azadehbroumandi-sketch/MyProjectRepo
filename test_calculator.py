import unittest

from calculator import add, calculate, divide, multiply, sqrt, subtract


class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(calculate(2, "+", 3), 5)

    def test_subtraction(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertEqual(calculate(7, "-", 4), 3)

    def test_multiplication(self):
        self.assertEqual(multiply(6, 4), 24)
        self.assertEqual(calculate(6, "*", 4), 24)

    def test_division(self):
        self.assertEqual(divide(8, 2), 4)
        self.assertEqual(calculate(8, "/", 2), 4)

    def test_square_root(self):
        self.assertEqual(sqrt(9), 3)
        self.assertEqual(sqrt(0), 0)
        self.assertAlmostEqual(sqrt(2), 2 ** 0.5)

    def test_square_root_rejects_negative_values(self):
        with self.assertRaises(ValueError):
            sqrt(-1)

    def test_square_root_rejects_invalid_values(self):
        with self.assertRaises(ValueError):
            sqrt("nine")
        with self.assertRaises(ValueError):
            sqrt(True)

    def test_decimal_operations(self):
        self.assertAlmostEqual(calculate(0.1, "+", 0.2), 0.3)
        self.assertAlmostEqual(calculate(7.5, "*", 0.4), 3.0)
        self.assertAlmostEqual(calculate(5.5, "/", 2), 2.75)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate(1, "%", 2)

    def test_invalid_operand(self):
        with self.assertRaises(ValueError):
            calculate("one", "+", 2)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
        with self.assertRaises(ZeroDivisionError):
            calculate(10, "/", 0)

    def test_invalid_second_operand(self):
        with self.assertRaises(ValueError):
            calculate(1, "+", "two")

    def test_boolean_operands_are_rejected(self):
        for operation in (add, subtract, multiply, divide):
            with self.subTest(operation=operation.__name__):
                with self.assertRaises(ValueError):
                    operation(True, 1)
                with self.assertRaises(ValueError):
                    operation(1, False)

        with self.assertRaises(ValueError):
            calculate(True, "+", 1)
        with self.assertRaises(ValueError):
            calculate(1, "+", False)

    def test_non_numeric_operands_are_rejected_by_each_operation(self):
        for operation in (add, subtract, multiply, divide):
            with self.subTest(operation=operation.__name__):
                with self.assertRaises(ValueError):
                    operation("one", 1)
                with self.assertRaises(ValueError):
                    operation(1, "one")

    def test_non_string_operator_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate(1, None, 2)


if __name__ == "__main__":
    unittest.main()
