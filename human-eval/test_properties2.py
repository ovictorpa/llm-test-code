import pytest
from lottie.objects.properties import KeyframeBezier, Keyframe, OffsetKeyframe, AnimatableMixin

def test_keyframe_bezier_from_keyframe():
    keyframe = Keyframe()
    keyframe.out_value = 1
    keyframe.in_value = 2
    obj = KeyframeBezier.from_keyframe(keyframe)
    assert obj.h1 == 1
    assert obj.h2 == 2

    
def test_animatable_mixin_clear_animation():
    obj = AnimatableMixin()
    obj.clear_animation(123)
    assert obj.value == 123
    assert obj.animated == False
    assert obj.keyframes == None
