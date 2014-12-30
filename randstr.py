#! /usr/bin/env python

import json
from itertools import repeat
import click

try:
    from os import urandom

    def randchar(alpha):
        b = urandom(1)
        alpha_size = len(alpha)
        try:
            return alpha[ord(b) % alpha_size]
        # with Python 3, `b` is byte
        except TypeError:
            return alpha[b % alpha_size]
except NotImplementedError:
    from random import choice

    def randchar(alpha):
        return choice(alpha)


def randstr(alpha, length):
    return ''.join(randchar(alpha) for _ in repeat(1, length))


@click.command()
@click.option('-l', '--length', default=16)
@click.option('-c', '--count', default=1)
@click.option('-a', '--alphabet', required=True, multiple=True)
@click.option('f', '-f', '--file', type=click.File())
def main(length, count, alphabet, f):
    if f:
        alphabets = json.load(f)
        alpha = ''.join(alphabets[s] for s in alphabet)
    else:
        alpha = ''.join(alphabet)
    for _ in range(count):
        click.echo(randstr(alpha, length))

if __name__ == '__main__':
    main()
