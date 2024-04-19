import pytest
from lottie.objects.animation import KeyframeBezier, Keyframe, OffsetKeyframe
from lottie.objects.helpers import AnimatableMixin

def test_keyframe_bezier_from_keyframe():
    keyframe = Keyframe()
    keyframe.out_value = 1
    keyframe.in_value = 2
    obj = KeyframeBezier.from_keyframe(keyframe)
    assert obj.h1 == 1
    assert obj.h2 == 2

def test_keyframe_bezier_bezier():
    obj = KeyframeBezier(1, 2)
    bez = obj.bezier()
    assert isinstance(bez, Bezier)

def test_keyframe_bezier_sample_values():
    obj = KeyframeBezier(1, 2)
    assert obj._sample_values is None
    obj.bezier()
    assert obj._sample_values is not None

def test_keyframe_bezier_newton_raphson_iterate():
    obj = KeyframeBezier(1, 2)
    result = obj._newton_raphson_iterate(0.5, 0.5)
    assert isinstance(result, float)

def test_keyframe_bezier_binary_subdivide():
    obj = KeyframeBezier(1, 2)
    result = obj._binary_subdivide(0.5, 0, 1)
    assert isinstance(result, float)

def test_keyframe_bezier_calc_bezier():
    obj = KeyframeBezier(1, 2)
    result = obj._calc_bezier(0.5, 1)
    assert isinstance(result, float)

def test_keyframe_bezier_calc_sample_values():
    obj = KeyframeBezier(1, 2)
    obj._calc_sample_values()
    assert obj._sample_values is not None

def test_keyframe_bezier_get_t_for_x():
    obj = KeyframeBezier(1, 2)
    result = obj._get_t_for_x(0.5)
    assert isinstance(result, float)

def test_keyframe_bezier_get(self):
    obj = KeyframeBezier(1, 2)
    result = obj.get(0.5)
    assert isinstance(result, float)
    
def test_animatable_mixin_clear_animation():
    obj = AnimatableMixin()
    obj.clear_animation(123)
    assert obj.value == 123
    assert obj.animated == False
    assert obj.keyframes == None

def test_animatable_mixin_add_keyframe():
    obj = AnimatableMixin()
    obj.add_keyframe(0, 123)
    assert obj.animated == True
    assert len(obj.keyframes) == 1
    assert obj.keyframes[0].start == 0
    assert obj.keyframes[0].end == None
    assert obj.keyframes[0].value == 123

def test_animatable_mixin_add_keyframe_with_end():
    obj = AnimatableMixin()
    obj.add_keyframe(0, 123, end=1)
    assert obj.animated == True
    assert len(obj.keyframes) == 1
    assert obj.keyframes[0].start == 0
    assert obj.keyframes[0].end == 1
    assert obj.keyframes[0].value == 123

def test_animatable_mixin_add_keyframe_with_args():
    obj = AnimatableMixin()
    obj.add_keyframe(0, 123, "foo", "bar")
    assert obj.animated == True
    assert len(obj.keyframes) == 1
    assert obj.keyframes[0].start == 0
    assert obj.keyframes[0].end == None
    assert obj.keyframes[0].value == 123
    assert obj.keyframes[0].args == ("foo", "bar")

def test_animatable_mixin_add_keyframe_with_kwargs():
    obj = AnimatableMixin()
    obj.add_keyframe(0, 123, foo="bar")
    assert obj.animated == True
    assert len(obj.keyframes) == 1
    assert obj.keyframes[0].start == 0
    assert obj.keyframes[0].end == None
    assert obj.keyframes[0].value == 123
    assert obj.keyframes[0].kwargs == {"foo": "bar"}    