import unittest
import format_price


class TestClass():
    pass


class TestPriceFormatter(unittest.TestCase):

    def test_correct_price(self):
        self.assertEqual(
            format_price.format_price('3245.000000'), '3 245.00'
        )

    def test_string_data(self):
        self.assertIsNone(format_price.format_price('dfsd'))

    def test_string_with_comma_data(self):
        self.assertIsNone(format_price.format_price('123,34'))

    def test_integer_data(self):
        self.assertEqual(
            format_price.format_price(4320984), '4 320 984.00'
        )

    def test_float_data(self):
        self.assertEqual(
            format_price.format_price(-4320984.53), '-4 320 984.53'
        )

    def test_list_data(self):
        self.assertIsNone(format_price.format_price([1, 2, 3]))

    def test_dict_data(self):
        self.assertIsNone(format_price.format_price({'key', 'value'}))

    def test_tuple_data(self):
        self.assertIsNone(format_price.format_price((1, 2,)))

    def test_class_data(self):
        self.assertIsNone(format_price.format_price(TestClass()))

    def test_set_data(self):
        self.assertIsNone(format_price.format_price(set('dfsd')))

    def test_range_data(self):
        self.assertIsNone(format_price.format_price(range(4)))

    def test_false(self):
        self.assertIsNone(format_price.format_price(False))

    def test_true(self):
        self.assertIsNone(format_price.format_price(True))

    def test_none(self):
        self.assertIsNone(format_price.format_price(None))


if __name__ == '__main__':
    unittest.main()
