#!/usr/bin/python3
for i in [range(ord('a'),ord('e')), range(ord('f'),ord('q')), range(ord('r'),ord('z'))]:
    print('{}'.format(chr(ord('a') + i)), end='')
