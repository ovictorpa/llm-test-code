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

    # Tests for protected_args
    def test_protected_args(self):
        with self.assertWarns(DeprecationWarning):
            self.ctx.protected_args

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

    # Tests for __exit__
    def test_exit(self):
        self.ctx.__enter__()
        self.ctx.__exit__(None, None, None)
        self.assertEqual(self.ctx._depth, 0)

    # Tests for close
    def test_close(self):
        def callback():
            return 'callback'
        self.ctx.call_on_close(callback)
        self.assertEqual(self.ctx.close(), ['callback'])

    # Tests for call_on_close
    def test_call_on_close(self):
        def callback():
            return 'callback'
        self.ctx.call_on_close(callback)
        self.assertEqual(self.ctx._close_callbacks, [callback])

    # Tests for push
    def test_push(self):
        self.ctx.push()
        self.assertEqual(self.ctx._depth, 1)

    # Tests for pop
    def test_pop(self):
        self.ctx.push()
        self.ctx.pop()
        self.assertEqual(self.ctx._depth, 0)

    # Tests for lookup_default
    def test_lookup_default(self):
        self.assertEqual(self.ctx.lookup_default('test_param'), None)

    # Tests for exit
    def test_exit(self):
        with self.assertRaises(SystemExit):
            self.ctx.exit()

    # Tests for abort
    def test_abort(self):
        with self.assertRaises(SystemExit):
            self.ctx.abort()

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