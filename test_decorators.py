import unittest
from click.decorators import pass_context, pass_obj
from click import Context, Command

class TestDecorators(unittest.TestCase):
    def setUp(self):
        self.command = Command(name='test_command')
        self.ctx = Context(self.command, info_name='test_info')

    # Tests for pass_context
    def test_pass_context_success(self):
        @pass_context
        def func(ctx):
            return ctx
        self.assertEqual(func(), self.ctx)

    def test_pass_context_failure(self):
        @pass_context
        def func(ctx):
            return ctx.command
        with self.assertRaises(AttributeError):
            func()

    def test_pass_context_with_args(self):
        @pass_context
        def func(ctx, arg1, arg2):
            return arg1 + arg2
        self.assertEqual(func(1, 2), 3)

    def test_pass_context_with_kwargs(self):
        @pass_context
        def func(ctx, arg1, arg2):
            return arg1 + arg2
        self.assertEqual(func(arg1=1, arg2=2), 3)

    def test_pass_context_with_args_and_kwargs(self):
        @pass_context
        def func(ctx, arg1, arg2, arg3=0):
            return arg1 + arg2 + arg3
        self.assertEqual(func(1, 2, arg3=3), 6)

    # Tests for pass_obj
    def test_pass_obj_success(self):
        self.ctx.obj = 'test_obj'
        @pass_obj
        def func(obj):
            return obj
        self.assertEqual(func(), 'test_obj')

    def test_pass_obj_failure(self):
        self.ctx.obj = None
        @pass_obj
        def func(obj):
            return obj
        with self.assertRaises(TypeError):
            func()

    def test_pass_obj_with_args(self):
        self.ctx.obj = 'test_obj'
        @pass_obj
        def func(obj, arg1, arg2):
            return obj, arg1 + arg2
        self.assertEqual(func(1, 2), ('test_obj', 3))

    def test_pass_obj_with_kwargs(self):
        self.ctx.obj = 'test_obj'
        @pass_obj
        def func(obj, arg1, arg2):
            return obj, arg1 + arg2
        self.assertEqual(func(arg1=1, arg2=2), ('test_obj', 3))

    def test_pass_obj_with_args_and_kwargs(self):
        self.ctx.obj = 'test_obj'
        @pass_obj
        def func(obj, arg1, arg2, arg3=0):
            return obj, arg1 + arg2 + arg3
        self.assertEqual(func(1, 2, arg3=3), ('test_obj', 6))

if __name__ == '__main__':
    unittest.main()
