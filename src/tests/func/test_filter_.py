#pylint:disable=wrong-import-position,wrong-import-order,ungrouped-imports,missing-function-docstring,unused-argument,invalid-name,multiple-statements

import logging
LOGGER = logging.getLogger(__name__)

import pytest

from urtools.func.filter_ import filter_

def even(x): return x % 2 == 0
def odd(x): return x % 2 == 1

@pytest.mark.parametrize(('f', 'xs', 'expected'),
                         (
                            (even, [1, 2, 3], [2]),
                            (odd, [1, 2, 3], [1, 3]),
                            (even, [1, 1, 1], []),
                            (even, (1, 2, 3), (2,)),
                            (str.isupper, "AaBbbC", "ABC"),
                            (str.isalnum, "A1#", "A1"),
                            (str.isalnum, "@#$%^&*(", ""),
                            (str.isalnum, "", "")
                            )
                         )
def test(f, xs, expected):
    result = filter_(f, xs)
    assert result == expected
