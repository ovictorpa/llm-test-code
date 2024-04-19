import unittest
from click.formatting import measure_table, iter_rows, wrap_text

class TestFormatting(unittest.TestCase):
    # Tests for measure_table
    def test_measure_table(self):
        rows = [('abc', 'def'), ('abcdef', 'gh')]
        self.assertEqual(measure_table(rows), (6, 3))

    def test_measure_table_empty(self):
        rows = []
        self.assertEqual(measure_table(rows), ())

    # Tests for iter_rows
    def test_iter_rows(self):
        rows = [('abc', 'def'), ('abcdef',)]
        self.assertEqual(list(iter_rows(rows, 2)), [('abc', 'def'), ('abcdef', '')])

    def test_iter_rows_empty(self):
        rows = []
        self.assertEqual(list(iter_rows(rows, 2)), [])

    # Tests for wrap_text
    def test_wrap_text(self):
        text = 'abc def ghi'
        self.assertEqual(wrap_text(text, width=5), 'abc \ndef \nghi')

    def test_wrap_text_empty(self):
        text = ''
        self.assertEqual(wrap_text(text, width=5), '')

    def test_wrap_text_initial_indent(self):
        text = 'abc def ghi'
        self.assertEqual(wrap_text(text, width=5, initial_indent='  '), '  abc \ndef \nghi')

    def test_wrap_text_subsequent_indent(self):
        text = 'abc def ghi'
        self.assertEqual(wrap_text(text, width=5, subsequent_indent='  '), 'abc \n  def \n  ghi')

    def test_wrap_text_preserve_paragraphs(self):
        text = 'abc def ghi\n\njkl mno pqr'
        self.assertEqual(wrap_text(text, width=5, preserve_paragraphs=True), 'abc \ndef \nghi\n\njkl \nmno \npqr')

    def test_wrap_text_preserve_paragraphs_with_no_rewrap(self):
        text = 'abc def ghi\n\n\x08jkl mno pqr'
        self.assertEqual(wrap_text(text, width=5, preserve_paragraphs=True), 'abc \ndef \nghi\n\njkl mno pqr')

    def test_wrap_text_width(self):
        text = 'abc def ghi'
        self.assertEqual(wrap_text(text, width=10), 'abc def ghi')

    def test_wrap_text_width_exceeded(self):
        text = 'abc def ghi'
        self.assertEqual(wrap_text(text, width=3), 'abc\ndef\nghi')

    def test_wrap_text_initial_indent_exceeds_width(self):
        text = 'abc def ghi'
        self.assertEqual(wrap_text(text, width=5, initial_indent='     '), '     abc\ndef\nghi')

    def test_wrap_text_subsequent_indent_exceeds_width(self):
        text = 'abc def ghi'
        self.assertEqual(wrap_text(text, width=5, subsequent_indent='     '), 'abc\n     def\n     ghi')

    def test_wrap_text_preserve_paragraphs_with_multiple_paragraphs(self):
        text = 'abc def ghi\n\njkl mno pqr\n\nstu vwx yz'
        self.assertEqual(wrap_text(text, width=5, preserve_paragraphs=True), 'abc \ndef \nghi\n\njkl \nmno \npqr\n\nstu \nvwx \nyz')

    def test_wrap_text_preserve_paragraphs_with_no_rewrap_multiple_paragraphs(self):
        text = 'abc def ghi\n\n\x08jkl mno pqr\n\n\x08stu vwx yz'
        self.assertEqual(wrap_text(text, width=5, preserve_paragraphs=True), 'abc \ndef \nghi\n\njkl mno pqr\n\nstu vwx yz')

if __name__ == '__main__':
    unittest.main()