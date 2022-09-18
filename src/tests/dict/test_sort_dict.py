#pylint:disable=wrong-import-position,wrong-import-order,ungrouped-imports,missing-function-docstring,unused-argument,invalid-name,multiple-statements

import pytest

from urtools.dict.sort_dict import sort_dict

d1 = {3:3, 1:2, 2:1}

@pytest.mark.parametrize(('d', 'by', 'expected'),
                            ((d1, 'key', {1:2, 2:1, 3:3}),
                            (d1, 'k', {1:2, 2:1, 3:3}),
                            (d1, 'value', {2:1, 1:2, 3:3}),
                            (d1, 'v', {2:1, 1:2, 3:3}),
                            ({}, 'k', {})))
def test(d, by, expected):
    assert sort_dict(d, by) == expected

def test_value_error():
    with pytest.raises(ValueError):
        sort_dict({}, by='x') #type:ignore
