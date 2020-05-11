#!/usr/bin/env python3
# FIXME: disable asserts when not in debug mode, some are expensive
# FIXME: decide if (param=value) or (param = value)
import sys, os
from enum import Enum, unique
from collections import namedtuple
from blist import blist
from typing import Tuple

@unique
class Subject(Enum):
    Char      = 1
    Word      = 2
    Line      = 3
    Sentence  = 4
    Paragraph = 5
    Function  = 6
    Class     = 7
    FullFile  = 8

@unique
class Direction(Enum):
    Forward  = 1
    Backward = 2


Selection = namedtuple('Selection', ['start', 'end'])

class BufferInitializeException(Exception): pass

class Buffer:
    """
    self._pos is 0 based
    self._line and self._column is 1 based
    """
    def __init__(self, filepath: str = None, text: str = None) -> None:
        if not filepath and text is None:
            raise BufferInitializeException('Buffer must be instantiated with a filepath'
                                            'or a text')
        if filepath:
            with open(filepath, 'r') as f:
                self.textl = blist(f.read())
        else:
            self.textl = blist(text)

        # Fixme: there three must be properties and update toghether on write
        self._pos        = 0
        self._line       = 1
        self._column     = 1

        self.selections = [] # type: List[Selection]

        self.moveselect_method = {
            Subject.Char      : self.ms_char,
            Subject.Word      : self.ms_word,
            Subject.Line      : self.ms_line,
            Subject.Sentence  : self.ms_sentence,
            Subject.Paragraph : self.ms_paragraph,
            Subject.Function  : self.ms_function,
            Subject.Class     : self.ms_class,
            Subject.FullFile  : self.ms_fullfile
        }

    @property
    def text(self) -> str:
        return ''.join(self.textl)

    @text.setter
    def text(self, text: str) -> None:
        self.textl = blist(text)

    @property
    def pos(self) -> int:
        return self._pos

    @pos.setter
    def pos(self, newpos: int) -> None:
        if newpos == self._pos:
            return

        newpos2 = max(0, min(int(newpos), len(self.textl) - 1))
        if newpos2 == self._pos:
            return

        self._pos = newpos2
        self.update_line_col()

    @property
    def line(self) -> int:
        return self._line

    @line.setter
    def line(self, newline: int) -> None:
        if newline == self._line:
            return

        newline2 = min(int(newline), self.num_lines)
        if newline2 == self._line:
            return

        self._line = newline2
        if self._column > self.cur_line_length:
            self._column = self.cur_line_length
        # column doest change
        # FIXME: it should be max(
        self.update_pos()

    @property
    def column(self) -> int:
        return self._column

    @column.setter
    def column(self, newcolumn: int) -> None:
        if newcolumn == self._column:
            return

        self._column = min(int(newcolumn), self.cur_line_length)
        self.update_pos()

    @property
    def cur_line_length(self) -> int:
        # FIXME: esto esta mal, tiene que contar de \n a \n
        pass

    @property
    def line_and_column(self) -> Tuple[int, int]:
        return self._line, self._column

    @line_and_column.setter
    def line_and_column(self, linecolumn: Tuple[int, int]) -> None:
        self._line   = min(linecolumn[0], self.num_lines)
        self._column = min(linecolumn[1], self.cur_line_length)
        self.update_pos()

    def update_line_col(self) -> None:
        prev_text = self.textl[:self._pos + 1]

        self._line = prev_text.count('\n')
        if prev_text[self._pos] != '\n':
            self._line += 1

        self.update_column()

    def update_pos(self) -> None:
        assert self._line <= self.num_lines

        lines_found = 0
        current_pos = -1

        while lines_found < self._line:
            nextline = self.textl.index('\n', current_pos + 1)
            lines_found += 1
            current_pos = nextline + 1

        self._pos = current_pos + self._column

    @property
    def num_lines(self) -> int:
        return self.textl.count('\n') + 1


    def process_subject(self, count: int, subject: Subject, direction: Direction) -> None:
        # TODO: allow extending selections
        self.empty_selections()

        if subject == Subject.FullFile:
            count = 1

        for i in range(count):
            self.moveselect_method[subject](direction)


    def ms_char(self, direction: Direction) -> None:
        pass
    def ms_word(self, direction: Direction) -> None:
        pass
    def ms_line(self, direction: Direction) -> None:
        pass
    def ms_sentence(self, direction: Direction) -> None:
        pass
    def ms_paragraph(self, direction: Direction) -> None:
        pass
    def ms_function(self, direction: Direction) -> None:
        pass
    def ms_class(self, direction: Direction) -> None:
        pass

    def ms_fullfile(self, direction: Direction) -> None:
        if self.pos == len(self.textl)- 1 and direction == Direction.Forward or\
           self.pos == 0 and direction == Direction.Backward:
                return

        if direction == Direction.Forward:
            if self.pos == len(self.textl) - 1:
                return

            self.selections.append(Selection(self.pos, len(self.textl) - 1))
            self.pos = len(self.textl) - 1

        else: # Backward
            if self.pos == 0:
                return

            self.selections.append(Selection(0, self.pos))
            self.pos = 0

    def empty_selections(self) -> None:
        del self.selections[:]
        # TODO: emit

    def update_column(self) -> int:
        prev_newline_pos = self.previous_newline_pos()
        self._column = self._pos - prev_newline_pos

        if prev_newline_pos == 0:
            self._column += 1

    def previous_newline_pos(self) -> int:
        currentpos = self._pos

        if self.textl[currentpos] == '\n':
            currentpos -= 1

        while True:
            if currentpos == 0:
                return 0

            if self.textl[currentpos] == '\n':
                break

            currentpos -= 1

        return currentpos


def main() -> None:
    if len(sys.argv) < 2:
        print('Need a file argument')
        exit(1)

    fpath = sys.argv[1]

    if not os.path.exists(fpath):
        print('Cannot find file')
        exit(2)

    buffer = Buffer(filepath=fpath)
    buffer.process_subject(2, Subject.Word, Direction.Forward)


if __name__ == '__main__':
    main()
