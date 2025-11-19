#!/usr/bin/python3

print(''.join(
    chr(c)
    for r in [range(ord('a'), ord('e')),
              range(ord('f'), ord('q')),
              range(ord('r'), ord('z'))]
    for c in r
))

