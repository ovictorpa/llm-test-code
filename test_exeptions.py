import unittest
from click import UsageError, BadParameter, MissingParameter
from click import Context, Command, Parameter

class TestUsageError(unittest.TestCase):
    def setUp(self):
        self.command = Command(name='test_command')
        self.ctx = Context(self.command, info_name='test_info')

    # Tests for __init__
    def test_init(self):
        error = UsageError('Test error', self.ctx)
        self.assertEqual(error.message, 'Test error')
        self.assertEqual(error.ctx, self.ctx)

    # Tests for __str__
    def test_str(self):
        error = UsageError('Test error', self.ctx)
        self.assertEqual(str(error), 'Test error')

    # Tests for show
    def test_show(self):
        error = UsageError('Test error', self.ctx)
        with self.assertRaises(SystemExit):
            error.show()

    # Tests for format_message
    def test_format_message(self):
        error = UsageError('Test error', self.ctx)
        self.assertEqual(error.format_message(), 'Test error')

class TestBadParameter(unittest.TestCase):
    def setUp(self):
        self.command = Command(name='test_command')
        self.ctx = Context(self.command, info_name='test_info')
        self.param = Parameter('test_param')

    # Tests for __init__
    def test_init(self):
        error = BadParameter('Test error', self.ctx, self.param)
        self.assertEqual(error.message, 'Test error')
        self.assertEqual(error.ctx, self.ctx)
        self.assertEqual(error.param, self.param)

    # Tests for __str__
    def test_str(self):
        error = BadParameter('Test error', self.ctx, self.param)
        self.assertEqual(str(error), 'Test error: test_param')

    # Tests for show
    def test_show(self):
        error = BadParameter('Test error', self.ctx, self.param)
        with self.assertRaises(SystemExit):
            error.show()

    # Tests for format_message
    def test_format_message(self):
        error = BadParameter('Test error', self.ctx, self.param)
        self.assertEqual(error.format_message(), 'Test error: test_param')
class TestMissingParameter(unittest.TestCase):
    def setUp(self):
        self.command = Command(name='test_command')
        self.ctx = Context(self.command, info_name='test_info')
        self.param = Parameter('test_param')

    # Tests for __init__
    def test_init(self):
        error = MissingParameter(ctx=self.ctx, param=self.param)
        self.assertEqual(error.ctx, self.ctx)
        self.assertEqual(error.param, self.param)

    # Tests for format_message
    def test_format_message(self):
        error = MissingParameter(ctx=self.ctx, param=self.param)
        self.assertEqual(error.format_message(), 'Missing parameter: test_param')

class TestBadParameter(unittest.TestCase):
    def setUp(self):
        self.command = Command(name='test_command')
        self.ctx = Context(self.command, info_name='test_info')
        self.param = Parameter('test_param')

    # Tests for __init__
    def test_init(self):
        error = BadParameter('Test error', self.ctx, self.param)
        self.assertEqual(error.message, 'Test error')
        self.assertEqual(error.ctx, self.ctx)
        self.assertEqual(error.param, self.param)

    # Tests for __str__
    def test_str(self):
        error = BadParameter('Test error', self.ctx, self.param)
        self.assertEqual(str(error), 'Test error: test_param')

    # Tests for show
    def test_show(self):
        error = BadParameter('Test error', self.ctx, self.param)
        with self.assertRaises(SystemExit):
            error.show()

    # Tests for format_message
    def test_format_message(self):
        error = BadParameter('Test error', self.ctx, self.param)
        self.assertEqual(error.format_message(), 'Test error: test_param')

if __name__ == '__main__':
    unittest.main()