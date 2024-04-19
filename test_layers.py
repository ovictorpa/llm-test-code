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

    def test_layer_from_dict(self):
        """Test if Layer.from_dict correctly sets properties."""
        obj = Layer()
        obj.from_dict({"threedimensional": True})
        assert obj.threedimensional == True

    def test_layer_get_time(self):
        """Test if Layer.get_time returns the correct time."""
        obj = Layer()
        obj.start_time = 1
        obj.in_point = 2
        obj.out_point = 3
        assert obj.get_time(0) == 1
        assert obj.get_time(1) == 2
        assert obj.get_time(2) == 3

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

    def test_visual_layer_from_dict(self):
        """Test if VisualLayer.from_dict correctly sets properties."""
        obj = VisualLayer()
        obj.from_dict({"threedimensional": True})
        assert obj.threedimensional == True

    def test_visual_layer_get_time(self):
        """Test if VisualLayer.get_time returns the correct time."""
        obj = VisualLayer()
        obj.start_time = 1
        obj.in_point = 2
        obj.out_point = 3
        assert obj.get_time(0) == 1
        assert obj.get_time(1) == 2
        assert obj.get_time(2) == 3