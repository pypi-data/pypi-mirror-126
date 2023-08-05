# my-first-python-package

This is an example project demonstrating how to publish a python module in PyPI.

'''python
pip install helloworld
'''

## Usage

'''python
from helloworld import say_hello

# Generate "Hello, World!"
say_hello()

# Generate "Hello, Everybody!"
say_hello("Everybody")
'''

# Developoing the Hello World

To install helloworld, along with the tools you need to develop and run tests, run the following
in you virutalenv:

'''bash
$ pip install -e .[dev]
'''