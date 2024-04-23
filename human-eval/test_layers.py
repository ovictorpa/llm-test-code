import pytest
from lottie.objects.layers import Layer, VisualLayer

class TestLayer:
    def test_layer_init(self):
        """Test if Layer initializes correctly."""
        obj = Layer()
        assert obj is not None

    def test_layer_clone(self):
        """Test if Layer.clone creates a new instance."""
        obj = Layer()
        clone = obj.clone()
        assert clone is not obj

    def test_layer_to_dict(self):
        """Test if Layer.to_dict returns a dictionary."""
        obj = Layer()
        assert isinstance(obj.to_dict(), dict)

class TestVisualLayer:
    def test_visual_layer_init(self):
        """Test if VisualLayer initializes correctly."""
        obj = VisualLayer()
        assert obj is not None

    def test_visual_layer_clone(self):
        """Test if VisualLayer.clone creates a new instance."""
        obj = VisualLayer()
        clone = obj.clone()
        assert clone is not obj

    def test_visual_layer_to_dict(self):
        """Test if VisualLayer.to_dict returns a dictionary."""
        obj = VisualLayer()
        assert isinstance(obj.to_dict(), dict)
