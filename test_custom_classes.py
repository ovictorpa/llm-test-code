import click
import pytest

def test_custom_context_with_none_formatter_class(runner):
    """Test if CustomContext raises an exception when formatter_class is None."""

    class CustomContext(click.Context):
        formatter_class = None

    with pytest.raises(Exception):
        context = CustomContext(
            click.Command("test", params=[click.Option(["--value"])]), color=True
        )

def test_custom_context_with_invalid_formatter_class(runner):
    """Test if CustomContext raises an exception when formatter_class is an invalid type."""

    class CustomContext(click.Context):
        formatter_class = {}

    with pytest.raises(Exception):
        context = CustomContext(
            click.Command("test", params=[click.Option(["--value"])]), color=True
        )

def test_custom_group_with_none_command_class(runner):
    """Test if CustomGroup raises an exception when command_class is None."""

    class CustomGroup(click.Group):
        command_class = None

    with pytest.raises(Exception):
        group = CustomGroup()

def test_custom_group_with_invalid_command_class(runner):
    """Test if CustomGroup raises an exception when command_class is an invalid type."""

    class CustomGroup(click.Group):
        command_class = {}

    with pytest.raises(Exception):
        group = CustomGroup()

def test_group_command_with_invalid_function(runner):
    """Test if group.command() raises an exception when the function passed as argument is not a function."""

    class CustomCommand(click.Command):
        pass

    class CustomGroup(click.Group):
        command_class = CustomCommand

    group = CustomGroup()

    with pytest.raises(Exception):
        subcommand = group.command()(123)