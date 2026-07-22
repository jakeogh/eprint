#!/usr/bin/env python3

import sys


def eprint(*args, **kwargs) -> None:
    assert "file" not in kwargs
    print(*args, file=sys.stderr, **kwargs)
