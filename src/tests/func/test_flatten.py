#pylint:disable=wrong-import-position,wrong-import-order,ungrouped-imports,missing-function-docstring,unused-argument,invalid-name,multiple-statements
import pytest

from urtools.func.flatten import (flatten, 
                                  OuterNotSubclassOfIterableError,
                                  OuterTypeIsStrError,
                                  MoreThanOneTypeError, 
                                  InnerNotSubclassOfIterableError)

@pytest.mark.parametrize(('xs', 'expected'),
                         (
                             (['a', 'b', 'c'], 'abc'),
                             ([[1], [], [1, 2]], [1, 1, 2]),
                             (({1, 2, 3}, set(), {1, 2}, {4}), {1, 2, 3, 4}),
                             (({1: 2, 2:3}, {}, {2: 4}), {1: 2, 2: 4}),
                             (((1, 2), (), (2, 3, 4)), (1, 2, 2, 3, 4)),
                             ([], []),
                             ((), ())
                            )

                         )
def test(xs, expected):
    result = flatten(xs)
    assert result == expected


# Test for errrors
@pytest.mark.parametrize('xs',
                         (1, 1., None, True, False, object)
                         )
def test_outer_error(xs):
    with pytest.raises(OuterNotSubclassOfIterableError) as exc_info:
        result = flatten(xs)

# Test for errrors
@pytest.mark.parametrize('xs',
                         ('sssss', 'xxxx   ')
                         )
def test_outer_str_error(xs):
    with pytest.raises(OuterTypeIsStrError) as exc_info:
        result = flatten(xs)

@pytest.mark.parametrize('xs',
                         (
                             [[1, 2], ()],
                             [{2}, {1:2}]
                         ))
def test_more_than_one_type_error(xs):
    with pytest.raises(MoreThanOneTypeError) as exc_info:
        result = flatten(xs)


@pytest.mark.parametrize('xs',
                         (
                             [1, 2, 3],
                             [1., 2., 3., 4.],
                             [None],
                             [True, False, True],
                             
                            )
                         )
def test_inner_error(xs):
    with pytest.raises(InnerNotSubclassOfIterableError) as exc_info:
        result = flatten(xs)

