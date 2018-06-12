import argparse


def format_price(price):
    if price is True or not price:
        return None
    try:
        price_float = float(price)
        price_comma = '{:,.2f}'.format(
            price_float
        ).rstrip('0').rstrip('.')
        return price_comma.replace(',', ' ')
    except(ValueError, TypeError):
        return None


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
    if not formatted_price:
        exit('Wrong value got from --price parameter')
    exit('Price {} formatted as {}'.format(args.price, formatted_price))
