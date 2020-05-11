#!/usr/bin/env python3
import unittest
import backend

class TestBuffer(unittest.TestCase):
    # Columns should always be pos in line + 1

    #col: 1                        26                       51 # maxcol = 52
    t1 = "0 some random text  and  25 and some more  text   50" # maxpos = 51 || len = 52
    t2 = "0 some random test with  25\n new line and more\nlines after\n62" # maxpos = 61 "" len = 62
    t3 = "123456789"
    tnull = " "

    def setUp(self):
        self.buf1    = backend.Buffer(text = self.t1)
        self.buf2    = backend.Buffer(text = self.t2)
        self.buf3    = backend.Buffer(text = self.t3)
        self.bufnull = backend.Buffer(text = self.tnull)

    def test_text(self):
        self.assertEqual(self.buf1.text, self.t1)
        self.assertEqual(self.bufnull.text, " ")

        newstr = "polompos pok"
        self.buf1.text = newstr
        self.assertEqual(self.buf1.text, newstr)

    def test_pos_get(self):
        self.assertEqual(self.buf1.pos, 0)
        self.assertEqual(self.bufnull.pos, 0)

    def test_pos_set(self):
        self.buf1.pos = 0
        self.assertEqual(self.buf1.line, 1)
        self.assertEqual(self.buf1.column, 1)

        self.buf3.pos = 5
        self.assertEqual(self.buf3.line, 1)
        self.assertEqual(self.buf3.column, 6)

        self.buf1.pos = 99999999
        self.assertEqual(self.buf1.line, 1)
        self.assertEqual(self.buf1.column, len(self.t1))

        self.buf2.pos = 25
        self.assertEqual(self.buf2.line, 1)
        self.assertEqual(self.buf2.column, 26)

        self.buf2.pos = 27
        self.assertEqual(self.buf2.line, 1)
        self.assertEqual(self.buf2.column, 28)

        self.buf2.pos = 99999999
        self.assertEqual(self.buf2.line, 4)
        self.assertEqual(self.buf2.column, 2)
        self.assertEqual(self.buf2.pos, len(self.t2) - 1)

        self.bufnull.pos = 99999999
        self.assertEqual(self.bufnull.line, 1)
        self.assertEqual(self.bufnull.column, 1)
        self.assertEqual(self.bufnull.pos, len(self.tnull) - 1)

        self.buf2.pos = -1234556
        self.assertEqual(self.buf2.pos, 0)

        self.bufnull.pos = -124324
        self.assertEqual(self.bufnull.pos, 0)

        self.buf2.pos = 3.14
        self.assertEqual(self.buf2.pos, 3)

    def test_numlines(self):
        self.assertEqual(self.buf1.num_lines, 1)
        self.assertEqual(self.buf2.num_lines, 4)
        self.assertEqual(self.buf3.num_lines, 1)

        buf_ends_newline = backend.Buffer(text = self.t2[:-2])
        self.assertEqual(buf_ends_newline.num_lines, 4)

    def test_line_get(self):
        self.assertEqual(self.buf1.line, 1)
        self.assertEqual(self.buf2.line, 1)
        self.assertEqual(self.buf3.line, 1)
        self.assertEqual(self.bufnull.line, 1)

    def test_line_set(self):
        oldcol1 = self.buf1.column
        self.buf1.line = 2
        self.assertEqual(self.buf1.line, 1)
        self.assertEqual(self.buf1.column, oldcol1)

        self.buf2.pos = 35
        self.assertEqual(self.buf2.line, 2)
        oldcolumn = self.buf2.column
        self.buf2.line = 3
        self.assertEqual(self.buf2.line, 3)
        self.assertEqual(self.buf2.column, oldcolumn)



    def test_column(self):
        pass

    def test_cur_line_length(self):
        pass

    def test_line_and_column(self):
        pass

    def test_update_line_col(self):
        pass

    def test_update_pos(self):
        pass

    def test_num_lines(self):
        pass

    def test_ms_char(self):
        pass

    def test_ms_word(self):
        pass

    def test_ms_line(self):
        pass

    def test_ms_sentence(self):
        pass

    def test_ms_paragraph(self):
        pass

    def test_ms_class(self):
        pass

    def test_ms_fullfile(self):
        pass

    def test_empty_selections(self):
        pass

    def test_update_column(self):
        pass

    def previous_newline_pos(self):
        pass




    # def test_ms_fullfile(self) -> None:
        # b = backend.Buffer(t1)
        # self.assertEqual(
