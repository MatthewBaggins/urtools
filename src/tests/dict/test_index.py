#pylint:disable=wrong-import-position,wrong-import-order,ungrouped-imports,missing-function-docstring,unused-argument,invalid-name,multiple-statements,missing-class-docstring
import logging
LOGGER = logging.getLogger(__name__)

import pytest


from urtools.dict.index import (_dict_multindex_prep_keys,
                                DictInvalidKeyError,
                                KeysAndNegKeysAreNoneError,
                                KeysAndNegKeysAreNotNoneError,
                                NoneInKeysError)
# test all errors
class Test__dict_multindex_prep_keys:
    d_1 = {1:1, 2:2, 3:3}
    def test_DictionaryHasInvalidKeyError(self):
        with pytest.raises(DictInvalidKeyError):
            _dict_multindex_prep_keys({**self.d_1, None: 1})

    def test_KeysAndNegKeysAreNoneError(self):
        with pytest.raises(KeysAndNegKeysAreNoneError):
            _dict_multindex_prep_keys(self.d_1, keys=None, neg_keys=None)

    def test_KeysAndNegKeysAreNotNoneError(self):
        with pytest.raises(KeysAndNegKeysAreNotNoneError):
            _dict_multindex_prep_keys(self.d_1, keys=1, neg_keys=2)

    def test_NoneInKeysError_keys(self):
        with pytest.raises(NoneInKeysError) as exc_info:
            _dict_multindex_prep_keys(self.d_1, keys=[None]) #type:ignore

    def test_NoneInKeysError_neg_keys(self):
        with pytest.raises(NoneInKeysError) as exc_info:
            _dict_multindex_prep_keys(self.d_1, neg_keys=[None]) #type:ignore



from urtools.dict.index import dict_multindex
class Test_dict_multindex:
    d_1 = {1: 1, 2: 2, 'key': 'KEY'}
    @pytest.mark.parametrize(('keys', 'expected'),
                             (('key', {'key': 'KEY'}),
                              ([1, 2], {1: 1, 2: 2}),
                              (d_1.keys(), d_1)))
    def test_keys(self, keys, expected: dict):
        result = dict_multindex(self.d_1, keys=keys)
        assert result == expected

    @pytest.mark.parametrize(('neg_keys', 'expected'),
                             ((2, {1: 1, 'key': 'KEY'}),
                              ([1, 3], {2: 2, 'key': 'KEY'}),
                              ([], d_1),
                              (d_1.keys(), {})))
    def test_neg_keys(self, neg_keys, expected):
        result = dict_multindex(self.d_1, neg_keys=neg_keys)
        assert result == expected

from urtools.dict.index import dict_del_keys
class Test_dict_del_keys:
    d_1 = {1: 1, 2: 2, 'a': 'a', 'bb': 'bb'}
    @pytest.mark.parametrize(('del_keys', 'expected'),
                             ((1, {2: 2, 'a': 'a', 'bb': 'bb'}),
                              (d_1.keys(), {}),
                              (list(d_1.keys()) + [3,4,5], {}),
                              ([], d_1)))
    def test(self, del_keys, expected):
        res = dict_del_keys(self.d_1, del_keys)
        assert res == expected
    
from urtools.dict.index import dict_list_index
class Test_dict_list_index:
    dl_1 = [{1: 2}, {1: 3}, {2: 2}]
    @pytest.mark.parametrize(('keys', 'expected'),
                             ((1, [2, 3, None]),
                              (2, [None, None, 2]),
                              ('x', 3*[None])))
    def test(self, keys, expected):
        result = dict_list_index(self.dl_1, keys)
        assert result == expected

from urtools.dict.index import dict_list_multindex
class Test_dict_list_multindex:  
    dl_1 = [{1:1, 2:2, 3:3},
            {3:0, 4:4, 5:5}]
    @pytest.mark.parametrize(('keys', 'expected'),
                             (([1, 2], {1: [1, None], 2: [2, None]}),
                              (1, {1: [1, None]}),
                              ([], {})))
    def test_keys(self, keys, expected):
        result = dict_list_multindex(self.dl_1, keys)
        assert result == expected

    @pytest.mark.parametrize(('neg_keys', 'expected'),
                             (([1,2,3,4,5], {}),
                              ([], {1: [1, None], 2: [2, None], 3: [3, 0], 4: [None, 4], 5: [None, 5]}),
                              ([2, 3], {1: [1, None], 4: [None, 4], 5: [None, 5]})))
    def test_neg_keys(self, neg_keys, expected):
        result = dict_list_multindex(self.dl_1, neg_keys=neg_keys)
        LOGGER.info(f'{result=}')
        assert result == expected
    
