# Price Formatter

This little project introducing and testing function, formatting
price, according to current locale.

# Quickstart

To launch program, type in console:
```bash
(lenv) E:\lproj\18_price_format>python format_price.py -p 3425.42
Price 3425.42 formatted as 3 425
```

Using it like a module:
```bash
(lenv) E:\lproj\18_price_format>python
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import format_price
>>> format_price.format_price('342134.0000')
'342\xa0134'
>>>
```

In case of testing:
```bash
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

Launch in Linux is the same.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
