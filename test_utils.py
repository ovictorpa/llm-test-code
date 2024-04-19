import unittest
import os
import sys
from click.utils import LazyFile, KeepOpenFile
from click.utils import _posixify, safecall, make_str, make_default_short_help, get_binary_stream, get_text_stream

class TestUtils(unittest.TestCase):
    def test_posixify(self):
        self.assertEqual(_posixify('Test Name'), 'test-name')
        self.assertEqual(_posixify('Another TestName'), 'another-testname')
        self.assertEqual(_posixify('testName'), 'testname')

    def test_safecall(self):
        def func_no_exception():
            return 'No exception'

        def func_with_exception():
            raise Exception('Test exception')

        self.assertEqual(safecall(func_no_exception)(), 'No exception')
        self.assertIsNone(safecall(func_with_exception)())

    def test_make_str(self):
        self.assertEqual(make_str('Test string'), 'Test string')
        self.assertEqual(make_str(b'Test bytes'), 'Test bytes')

    def test_make_default_short_help(self):
        long_help = 'This is a very long help string that goes on and on and on.'
        self.assertEqual(make_default_short_help(long_help, max_length=20), 'This is a very long')
        
class TestLazyFile(unittest.TestCase):
    def setUp(self):
        self.lazy_file = LazyFile('test.txt', 'w')

    def test_write(self):
        self.lazy_file.write('Test')
        self.lazy_file.close()
        with open('test.txt', 'r') as f:
            self.assertEqual(f.read(), 'Test')

    def test_iter(self):
        self.lazy_file.write('Test\nLine2')
        self.lazy_file.close()
        self.lazy_file = LazyFile('test.txt', 'r')
        self.assertEqual(list(self.lazy_file), ['Test\n', 'Line2'])

    def tearDown(self):
        os.remove('test.txt')


class TestKeepOpenFile(unittest.TestCase):
    def setUp(self):
        self.file = open('test.txt', 'w')
        self.keep_open_file = KeepOpenFile(self.file)

    def test_write(self):
        self.keep_open_file.write('Test')
        self.keep_open_file.close()
        with open('test.txt', 'r') as f:
            self.assertEqual(f.read(), 'Test')

    def test_iter(self):
        self.file.write('Test\nLine2')
        self.file.close()
        self.file = open('test.txt', 'r')
        self.keep_open_file = KeepOpenFile(self.file)
        self.assertEqual(list(self.keep_open_file), ['Test\n', 'Line2'])

    def tearDown(self):
        os.remove('test.txt')
        
class TestUtils(unittest.TestCase):
    # Tests for _posixify
    def test_posixify(self):
        self.assertEqual(_posixify('Test Name'), 'test-name')

    def test_posixify_no_spaces(self):
        self.assertEqual(_posixify('TestName'), 'testname')

    def test_posixify_empty(self):
        self.assertEqual(_posixify(''), '')

    # Tests for safecall
    def test_safecall_no_exception(self):
        def func(x):
            return x
        safe_func = safecall(func)
        self.assertEqual(safe_func(1), 1)

    def test_safecall_with_exception(self):
        def func(x):
            raise Exception('Test exception')
        safe_func = safecall(func)
        self.assertIsNone(safe_func(1))

    def test_safecall_with_args(self):
        def func(x, y):
            return x + y
        safe_func = safecall(func)
        self.assertEqual(safe_func(1, 2), 3)

    def test_safecall_with_kwargs(self):
        def func(x, y):
            return x + y
        safe_func = safecall(func)
        self.assertEqual(safe_func(x=1, y=2), 3)

    def test_safecall_with_args_and_exception(self):
        def func(x, y):
            raise Exception('Test exception')
        safe_func = safecall(func)
        self.assertIsNone(safe_func(1, 2))

    def test_safecall_with_kwargs_and_exception(self):
        def func(x, y):
            raise Exception('Test exception')
        safe_func = safecall(func)
        self.assertIsNone(safe_func(x=1, y=2))
        
class TestUtils(unittest.TestCase):
    # Tests for get_binary_stream
    def test_get_binary_stream_stdin(self):
        self.assertEqual(get_binary_stream('stdin'), sys.stdin.buffer)

    def test_get_binary_stream_stdout(self):
        self.assertEqual(get_binary_stream('stdout'), sys.stdout.buffer)

    def test_get_binary_stream_stderr(self):
        self.assertEqual(get_binary_stream('stderr'), sys.stderr.buffer)

    def test_get_binary_stream_invalid(self):
        with self.assertRaises(TypeError):
            get_binary_stream('invalid')

    # Tests for get_text_stream
    def test_get_text_stream_stdin(self):
        self.assertEqual(get_text_stream('stdin'), sys.stdin)

    def test_get_text_stream_stdout(self):
        self.assertEqual(get_text_stream('stdout'), sys.stdout)

    def test_get_text_stream_stderr(self):
        self.assertEqual(get_text_stream('stderr'), sys.stderr)

    def test_get_text_stream_invalid(self):
        with self.assertRaises(TypeError):
            get_text_stream('invalid')

    def test_get_text_stream_stdin_with_encoding(self):
        stream = get_text_stream('stdin', encoding='utf-8')
        self.assertEqual(stream.encoding, 'utf-8')

    def test_get_text_stream_stdout_with_encoding(self):
        stream = get_text_stream('stdout', encoding='utf-8')
        self.assertEqual(stream.encoding, 'utf-8')

    def test_get_text_stream_stderr_with_encoding(self):
        stream = get_text_stream('stderr', encoding='utf-8')
        self.assertEqual(stream.encoding, 'utf-8')

    def test_get_text_stream_stdin_with_errors(self):
        stream = get_text_stream('stdin', errors='ignore')
        self.assertEqual(stream.errors, 'ignore')

    def test_get_text_stream_stdout_with_errors(self):
        stream = get_text_stream('stdout', errors='ignore')
        self.assertEqual(stream.errors, 'ignore')

    def test_get_text_stream_stderr_with_errors(self):
        stream = get_text_stream('stderr', errors='ignore')
        self.assertEqual(stream.errors, 'ignore')


if __name__ == '__main__':
    unittest.main()