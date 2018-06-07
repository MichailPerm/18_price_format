import unittest
import format_price
import locale


class TestClass():
    pass


class TestPriceFormatter(unittest.TestCase):

    def test_correct_price(self):
        self.assertEqual(
            format_price.format_price('3245.000000'),
            locale.format_string('%.2f', float('3245'),
            grouping=True)
        )

    def test_string_data(self):
        with self.assertRaises(ValueError):
            format_price.format_price('dfsd')

    def test_string_with_comma_data(self):
        with self.assertRaises(ValueError):
            format_price.format_price('123,34')

    def test_list_data(self):
        with self.assertRaises(TypeError):
            format_price.format_price([1, 2, 3])

    def test_dict_data(self):
        with self.assertRaises(TypeError):
            format_price.format_price({'key', 'value'})

    def test_tuple_data(self):
        with self.assertRaises(TypeError):
            format_price.format_price((1, 2,))

    def test_class_data(self):
        with self.assertRaises(TypeError):
            format_price.format_price(TestClass())


if __name__ == '__main__':
    unittest.main()
