#! /usr/bin/env python

import json
import click


def randstr(alpha, length):
    try:
        import os
        alpha_size = len(alpha)
        return ''.join(alpha[ord(b) % alpha_size] for b in os.urandom(length))
    except NotImplementedError:
        import random
        return ''.join(random.choice(alpha) for _ in length)


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
