#pylint:disable=wrong-import-position,wrong-import-order,ungrouped-imports,missing-function-docstring,unused-argument,invalid-name,multiple-statements

import logging
LOGGER = logging.getLogger(__name__)

import pytest

########
# map_ #
########

from urtools.func.map_ import map_

def square(x): return x**2
def nextchar(c: str): return chr(ord(c) + 1)

@pytest.mark.parametrize(('f', 'xs', 'expected'),
                         (
                            (square, [1, 2, 3], [1, 4, 9]),
                            (square, (1, 2, 3), (1, 4, 9)),
                            (square, [], []),
                            (square, (), ()),
                            (nextchar, "s", "t"),
                            (nextchar, "", ""),
                            (nextchar, "ast", "btu"),
                            )
                         )
def test(f, xs, expected):
    result = map_(f, xs)
    assert result == expected
