import unittest
import format_price
import locale


class TestPriceFormatter(unittest.TestCase):

    def test_correct_price(self):
        self.assertEqual(format_price.format_price('3245.000000'),
                         locale.format_string("%d", float('3245'),
                                              grouping=True)
                         )


    def test_uncorrect_data_type(self):
        self.assertIsNone(format_price.format_price(6452.00))


    def test_uncorrect_data_str(self):
        self.assertIsNone(format_price.format_price('This thing'))


if __name__ == '__main__':
    unittest.main()
