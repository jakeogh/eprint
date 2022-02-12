#!/usr/bin/env python3
# -*- coding: utf8 -*-
# tab-width:4
"""
Error Print: eprint()
print() to sys.stderr
"""

import sys


def eprint(*args, **kwargs) -> None:
    """print() to sys.stderr"""
    try:
        kwargs.pop("file")
    except KeyError:
        pass
    print(*args, file=sys.stderr, **kwargs)
