#pylint:disable=wrong-import-position,wrong-import-order,ungrouped-imports,missing-function-docstring,unused-argument,invalid-name,multiple-statements

import numpy as np
import pytest


from urtools.dict.dict_nans import filter_dict_nans
@pytest.mark.parametrize(('d', 'expected'),
                         (
                             ({1: None, 2: None, 3: np.nan}, {}),
                             ({2: None, 1: 2}, {1: 2})
                            )
                         )
def test_filtered_as_expected(d: dict, expected: dict):
    assert filter_dict_nans(d) == expected
