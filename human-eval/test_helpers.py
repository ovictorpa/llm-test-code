import pytest
from lottie.objects.helpers import Transform, MaskMode, VisualObject, Mask, NVector


def test_transform_init():
    obj = Transform()
    assert obj is not None


def test_transform_clone():
    obj = Transform()
    clone = obj.clone()
    assert clone is not obj


def test_visual_object_init():
    obj = VisualObject()
    assert obj is not None

def test_visual_object_to_dict():
    obj = VisualObject()
    assert obj.to_dict() == {}


def test_visual_object_clone():
    obj = VisualObject()
    clone = obj.clone()
    assert clone is not obj


def test_mask_init():
    obj = Mask()
    assert obj is not None


def test_mask_clone():
    obj = Mask()
    clone = obj.clone()
    assert clone is not obj