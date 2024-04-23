import unittest
import click
from click.core import Context, Command

class TestContext(unittest.TestCase):
    def setUp(self):
        self.command = Command(name='test_command')
        self.ctx = Context(self.command, info_name='test_info')

    # Tests for __init__
    def test_init(self):
        self.assertEqual(self.ctx.command, self.command)
        self.assertEqual(self.ctx.info_name, 'test_info')


    # Tests for to_info_dict
    def test_to_info_dict(self):
        info_dict = self.ctx.to_info_dict()
        self.assertEqual(info_dict['command'], self.command.to_info_dict(self.ctx))
        self.assertEqual(info_dict['info_name'], 'test_info')
        self.assertEqual(info_dict['allow_extra_args'], False)
        self.assertEqual(info_dict['allow_interspersed_args'], True)
        self.assertEqual(info_dict['ignore_unknown_options'], False)
        self.assertEqual(info_dict['auto_envvar_prefix'], None)

    # Tests for __enter__
    def test_enter(self):
        self.ctx.__enter__()
        self.assertEqual(self.ctx._depth, 1)


    # Tests for lookup_default
    def test_lookup_default(self):
        self.assertEqual(self.ctx.lookup_default('test_param'), None)


    # Tests for fail
    def test_fail(self):
        with self.assertRaises(click.ClickException):
            self.ctx.fail('Test failure')

    # Tests for invoke
    def test_invoke(self):
        def callback():
            return 'callback'
        self.assertEqual(self.ctx.invoke(callback), 'callback')

    # Tests for forward
    def test_forward(self):
        @click.command()
        def cli():
            pass
        self.ctx.forward(cli)

if __name__ == '__main__':
    unittest.main()
