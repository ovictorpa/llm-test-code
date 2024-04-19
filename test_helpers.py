import pytest
from lottie.objects.helpers import Transform, MaskMode, VisualObject, Mask, NVector

def test_to_matrix_with_non_default_anchor_point(runner):
    transform = Transform()
    transform.anchor_point = NVector(1, 2)
    matrix = transform.to_matrix(0)
    assert matrix.m02 == -1
    assert matrix.m12 == -2

def test_to_matrix_with_non_default_scale(runner):
    transform = Transform()
    transform.scale = NVector(200, 300)
    matrix = transform.to_matrix(0)
    assert matrix.m00 == 2
    assert matrix.m11 == 3

def test_to_matrix_with_non_default_skew(runner):
    transform = Transform()
    transform.skew = 45  # degrees
    matrix = transform.to_matrix(0)
    assert matrix.m01 == -1
    assert matrix.m10 == -1

def test_to_matrix_with_non_default_rotation(runner):
    transform = Transform()
    transform.rotation = 90  # degrees
    matrix = transform.to_matrix(0)
    assert matrix.m00 == pytest.approx(0)
    assert matrix.m01 == pytest.approx(1)
    assert matrix.m10 == pytest.approx(-1)
    assert matrix.m11 == pytest.approx(0)

def test_to_matrix_with_non_default_position(runner):
    transform = Transform()
    transform.position = NVector(1, 2)
    matrix = transform.to_matrix(0)
    assert matrix.m02 == 1
    assert matrix.m12 == 2


def test_transform_init(runner):
    obj = Transform()
    assert obj is not None

def test_transform_to_dict(runner):
    obj = Transform()
    assert obj.to_dict() == {}

def test_transform_from_dict(runner):
    obj = Transform()
    obj.from_dict({"test": 123})
    assert obj.test == 123

def test_transform_clone(runner):
    obj = Transform()
    clone = obj.clone()
    assert clone is not obj

def test_mask_mode_init(runner):
    obj = MaskMode()
    assert obj is not None

def test_mask_mode_to_dict(runner):
    obj = MaskMode()
    assert obj.to_dict() == {}

def test_mask_mode_from_dict(runner):
    obj = MaskMode()
    obj.from_dict({"test": 123})
    assert obj.test == 123

def test_mask_mode_clone(runner):
    obj = MaskMode()
    clone = obj.clone()
    assert clone is not obj

def test_visual_object_init(runner):
    obj = VisualObject()
    assert obj is not None

def test_visual_object_to_dict(runner):
    obj = VisualObject()
    assert obj.to_dict() == {}

def test_visual_object_from_dict(runner):
    obj = VisualObject()
    obj.from_dict({"test": 123})
    assert obj.test == 123

def test_visual_object_clone(runner):
    obj = VisualObject()
    clone = obj.clone()
    assert clone is not obj

def test_mask_init(runner):
    obj = Mask()
    assert obj is not None

def test_mask_to_dict(runner):
    obj = Mask()
    assert obj.to_dict() == {}

def test_mask_from_dict(runner):
    obj = Mask()
    obj.from_dict({"test": 123})
    assert obj.test == 123

def test_mask_clone(runner):
    obj = Mask()
    clone = obj.clone()
    assert clone is not obj