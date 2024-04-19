import pytest
from lottie.objects.animation import KeyframeBezier, Keyframe, OffsetKeyframe
from lottie.objects.helpers import AnimatableMixin

def test_keyframe_bezier_init():
    obj = KeyframeBezier()
    assert obj is not None

def test_keyframe_bezier_clone():
    obj = KeyframeBezier()
    clone = obj.clone()
    assert clone is not obj

def test_keyframe_init():
    obj = Keyframe()
    assert obj is not None

def test_keyframe_clone():
    obj = Keyframe()
    clone = obj.clone()
    assert clone is not obj

def test_offset_keyframe_init():
    obj = OffsetKeyframe()
    assert obj is not None

def test_offset_keyframe_clone():
    obj = OffsetKeyframe()
    clone = obj.clone()
    assert clone is not obj

def test_animatable_mixin_init():
    obj = AnimatableMixin()
    assert obj is not None

def test_animatable_mixin_clone():
    obj = AnimatableMixin()
    clone = obj.clone()
    assert clone is not obj

def test_keyframe_bezier_to_dict():
    obj = KeyframeBezier()
    assert obj.to_dict() == {}

def test_keyframe_to_dict():
    obj = Keyframe()
    assert obj.to_dict() == {}

def test_offset_keyframe_to_dict():
    obj = OffsetKeyframe()
    assert obj.to_dict() == {}

def test_animatable_mixin_to_dict():
    obj = AnimatableMixin()
    assert obj.to_dict() == {}

def test_keyframe_bezier_from_dict():
    obj = KeyframeBezier()
    obj.from_dict({"test": 123})
    assert obj.test == 123

def test_keyframe_from_dict():
    obj = Keyframe()
    obj.from_dict({"test": 123})
    assert obj.test == 123

def test_offset_keyframe_from_dict():
    obj = OffsetKeyframe()
    obj.from_dict({"test": 123})
    assert obj.test == 123

def test_animatable_mixin_from_dict():
    obj = AnimatableMixin()
    obj.from_dict({"test": 123})
    assert obj.test == 123