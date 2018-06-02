import re
import argparse
import locale


def format_price(price):
    price_template = re.compile(r'^\d+.\d+$')
    if type(price) != str:
        return None
    if not price_template.search(price):
        return None
    locale.setlocale(locale.LC_ALL, '')
    return locale.format_string("%d", float(price), grouping=True)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p',
                        '--price',
                        help='Price to be formatted')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    formatted_price = format_price(args.price)
    if not formatted_price:
        exit('Incorrect price argument was passed!')
    print('Price {} formatted as {}'.format(args.price, formatted_price))
