import unittest
import format_price
import locale

class TestClass():
    pass

class TestPriceFormatter(unittest.TestCase):

    def test_correct_price(self):
        self.assertEqual(format_price.format_price('3245.000000'),
                         locale.format_string("%d", float('3245'),
                                              grouping=True)
                         )

    def test_uncorrect_data(self):
        test_data_list = ['dfsd', '123,34', [1, 2, 3], {'key', 'value'}, (1, 2,), TestClass()]
        for test_data in test_data_list:
            with self.assertRaises((TypeError, ValueError, NameError)):
                format_price.format_price(test_data)

if __name__ == '__main__':
    unittest.main()
