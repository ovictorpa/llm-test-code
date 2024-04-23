import pytest
from lottie.objects.base import LottieProp, LottieObject, CustomObject

def test_lottie_object_init():
    obj = LottieObject()
    assert obj is not None

def test_lottie_object_to_dict():
    obj = LottieObject()
    assert obj.to_dict() == {}


def test_lottie_object_clone():
    obj = LottieObject()
    clone = obj.clone()
    assert clone is not obj

def test_custom_object_init():
    obj = CustomObject()
    assert obj is not None


def test_lottie_prop_init():
    prop = LottieProp("test", int, 0)
    assert prop is not None

    
def test_basic_to_dict_with_invalid_v():
    prop = LottieProp("test", int, 0)
    with pytest.raises(Exception):
        prop._basic_to_dict({})

def test_basic_to_dict_with_mixed_list_v():
    prop = LottieProp("test", int, 0)
    result = prop._basic_to_dict([1, "foo", True])
    assert result == [1, "foo", True]

def test_basic_to_dict_with_list_of_lists_v():
    prop = LottieProp("test", int, 0)
    result = prop._basic_to_dict([[1, 2], [3, 4]])
    assert result == [[1, 2], [3, 4]]

def test_clone_value_with_invalid_value():
    prop = LottieProp("test", int, 0)
    with pytest.raises(Exception):
        prop.clone_value({})

def test_clone_value_with_mixed_list_value():
    prop = LottieProp("test", int, 0)
    result = prop.clone_value([1, "foo", True])
    assert result == [1, "foo", True]

def test_clone_value_with_list_of_lists_value():
    prop = LottieProp("test", int, 0)
    result = prop.clone_value([[1, 2], [3, 4]])
    assert result == [[1, 2], [3, 4]]