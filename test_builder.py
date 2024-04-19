import pytest
from .. import base
from lottie.parsers.sif import api, builder, ast
from lottie import objects
from lottie.nvector import NVector
from lottie.utils.color import Color

class TestSifBuilder(base.TestCase):
    # ... existing tests ...

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

    def test_layer_conversion(self):
        """Test if to_sif correctly converts a Layer."""
        lot = objects.Animation()
        layer = objects.layers.ShapeLayer()
        lot.add_layer(layer)

        sif = builder.to_sif(lot)
        self.assertIsInstance(sif.layers[0], ast.Layer)

    def test_visual_layer_conversion(self):
        """Test if to_sif correctly converts a VisualLayer."""
        lot = objects.Animation()
        layer = objects.layers.VisualLayer()
        lot.add_layer(layer)

        sif = builder.to_sif(lot)
        self.assertIsInstance(sif.layers[0], ast.VisualLayer)

    def test_animation_with_background_color(self):
        """Test if to_sif correctly converts the background color of an Animation."""
        lot = objects.Animation()
        lot.background_color = Color(1, 0, 0)

        sif = builder.to_sif(lot)
        self.assertEqual(sif.background_color, lot.background_color)

    def test_empty_background_color(self):
        """Test if to_sif correctly converts an empty Animation with a background color."""
        lot = objects.Animation()
        lot.background_color = Color(1, 0, 0)

        sif = builder.to_sif(lot)
        self.assertEqual(sif.background_color, lot.background_color)

    def test_empty_layers(self):
        """Test if to_sif correctly converts an empty Animation with layers."""
        lot = objects.Animation()
        layer = objects.layers.ShapeLayer()
        lot.add_layer(layer)

        sif = builder.to_sif(lot)
        self.assertEqual(len(sif.layers), len(lot.layers))

    def test_empty_markers(self):
        """Test if to_sif correctly converts an empty Animation with markers."""
        lot = objects.Animation()
        marker = objects.Marker()
        lot.markers.append(marker)

        sif = builder.to_sif(lot)
        self.assertEqual(len(sif.markers), len(lot.markers))

    def test_empty_assets(self):
        """Test if to_sif correctly converts an empty Animation with assets."""
        lot = objects.Animation()
        asset = objects.assets.ImageAsset()
        lot.assets.append(asset)

        sif = builder.to_sif(lot)
        self.assertEqual(len(sif.assets), len(lot.assets))