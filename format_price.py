import argparse
import locale


def format_price(price):
    locale.setlocale(locale.LC_ALL, '')
    return locale.format_string("%d", float(price), grouping=True)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p',
        '--price',
        help='Price to be formatted',
        required=True
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    formatted_price = format_price(args.price)
    print('Price {} formatted as {}'.format(args.price, formatted_price))
