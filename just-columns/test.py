from wrapper import get, run
import logging
import requests


@get('/')
def f():
    return 'Hello!'

def test():
    run(8888)

def main():
    pass


if __name__ == '__main__':
    test()