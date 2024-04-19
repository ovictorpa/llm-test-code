import pytest
from lottie.objects.base import LottieProp, LottieObject, CustomObject

def test_lottie_object_init(runner):
    """Test if LottieObject initializes correctly."""
    obj = LottieObject()
    assert obj is not None

def test_lottie_object_to_dict(runner):
    """Test if LottieObject.to_dict returns an empty dictionary."""
    obj = LottieObject()
    assert obj.to_dict() == {}

def test_lottie_object_from_dict(runner):
    """Test if LottieObject.from_dict correctly sets properties."""
    obj = LottieObject()
    obj.from_dict({"test": 123})
    assert obj.test == 123

def test_lottie_object_clone(runner):
    """Test if LottieObject.clone creates a new instance."""
    obj = LottieObject()
    clone = obj.clone()
    assert clone is not obj

def test_custom_object_init(runner):
    """Test if CustomObject initializes correctly."""
    obj = CustomObject()
    assert obj is not None

def test_custom_object_to_dict(runner):
    """Test if CustomObject.to_dict returns an empty dictionary."""
    obj = CustomObject()
    assert obj.to_dict() == {}

def test_custom_object_from_dict(runner):
    """Test if CustomObject.from_dict correctly sets properties."""
    obj = CustomObject()
    obj.from_dict({"test": 123})
    assert obj.test == 123

def test_custom_object_clone(runner):
    """Test if CustomObject.clone creates a new instance."""
    obj = CustomObject()
    clone = obj.clone()
    assert clone is not obj

def test_lottie_prop_init(runner):
    """Test if LottieProp initializes correctly."""
    prop = LottieProp("test", int, 0)
    assert prop is not None

def test_lottie_prop_load(runner):
    """Test if LottieProp.load correctly sets the value."""
    prop = LottieProp("test", int, 0)
    prop.load(123)
    assert prop.value == 123

def test_lottie_prop_save(runner):
    """Test if LottieProp.save correctly gets the value."""
    prop = LottieProp("test", int, 0)
    prop.load(123)
    assert prop.save() == 123

def test_lottie_prop_clone(runner):
    """Test if LottieProp.clone creates a new instance."""
    prop = LottieProp("test", int, 0)
    clone = prop.clone()
    assert clone is not prop

def test_lottie_prop_repr(runner):
    """Test if LottieProp.__repr__ returns the correct string."""
    prop = LottieProp("test", int, 0)
    assert repr(prop) == "<LottieProp test:0>"

def test_lottie_prop_clone_value(runner):
    """Test if LottieProp.clone_value correctly clones the value."""
    prop = LottieProp("test", list, [1, 2, 3])
    clone = prop.clone_value(prop.value)
    assert clone == [1, 2, 3]
    assert clone is not prop.value
    
def test_basic_to_dict_with_invalid_v(runner):
    """Test if LottieProp._basic_to_dict raises an exception when v is an invalid type."""
    prop = LottieProp("test", int, 0)
    with pytest.raises(Exception):
        prop._basic_to_dict({})

def test_basic_to_dict_with_mixed_list_v(runner):
    """Test if LottieProp._basic_to_dict returns the correct value when v is a list of mixed types."""
    prop = LottieProp("test", int, 0)
    result = prop._basic_to_dict([1, "foo", True])
    assert result == [1, "foo", True]

def test_basic_to_dict_with_list_of_lists_v(runner):
    """Test if LottieProp._basic_to_dict returns the correct value when v is a list of lists."""
    prop = LottieProp("test", int, 0)
    result = prop._basic_to_dict([[1, 2], [3, 4]])
    assert result == [[1, 2], [3, 4]]

def test_clone_value_with_invalid_value(runner):
    """Test if LottieProp.clone_value raises an exception when value is an invalid type."""
    prop = LottieProp("test", int, 0)
    with pytest.raises(Exception):
        prop.clone_value({})

def test_clone_value_with_mixed_list_value(runner):
    """Test if LottieProp.clone_value returns the correct value when value is a list of mixed types."""
    prop = LottieProp("test", int, 0)
    result = prop.clone_value([1, "foo", True])
    assert result == [1, "foo", True]

def test_clone_value_with_list_of_lists_value(runner):
    """Test if LottieProp.clone_value returns the correct value when value is a list of lists."""
    prop = LottieProp("test", int, 0)
    result = prop.clone_value([[1, 2], [3, 4]])
    assert result == [[1, 2], [3, 4]]