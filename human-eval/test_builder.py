from unittest import *
from lottie.parsers.sif import api, builder, ast
from lottie import objects
from lottie.nvector import NVector
from lottie.utils.color import Color

class TestSifBuilder(TestCase):

    def test_non_empty(self):
        """Test if to_sif correctly converts a non-empty Animation."""
        lot = objects.Animation()
        lot.width = 123
        lot.height = 456
        lot.frame_rate = 69
        lot.in_point = 3
        lot.out_point = 7
        lot.name = "test"

        # Add a layer to the animation
        layer = objects.layers.ShapeLayer()
        lot.add_layer(layer)

        sif = builder.to_sif(lot)
        self.assertEqual(len(sif.layers), 1)


    def test_empty_layers(self):
        """Test if to_sif correctly converts an empty Animation with layers."""
        lot = objects.Animation()
        layer = objects.layers.ShapeLayer()
        lot.add_layer(layer)

        sif = builder.to_sif(lot)
        self.assertEqual(len(sif.layers), len(lot.layers))
