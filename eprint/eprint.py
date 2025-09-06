#!/usr/bin/env python3
# -*- coding: utf8 -*-
# tab-width:4
"""
Error Print: eprint()
print() to sys.stderr with a print() compatible API
"""

import sys


def eprint(*args, **kwargs) -> None:
    """print() to sys.stderr"""
    kwargs.pop("file", None)
    print(*args, file=sys.stderr, **kwargs)
