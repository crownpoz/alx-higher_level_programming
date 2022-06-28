#!/usr/bin/python3
for t in range(97, 123):
    if t == 113 or t == 101:
        continue
    else:
        print("{}".format(chr(t)), end="")
