"""
Editline:
   Module to provide higher level functionality access to libedit.
"""

import sys
import os
from editline import _editline

class EditLine(_editline.EditLineBase):
    """Editline High Level Support

    Provides the usable interface to the _editline compiled module. This class
    is derived from the compiled module and it provides functionality which
    is best implemented in python code -- not C.

    Args:
        name: a name for the instance to identify it
        in_stream:  input file-like object
        out_stream: output file-like object
        err_stream: error file-like object

    Returns:
        EditLine class instance.

    """

    IMPORTANT_VARIABLE = 12

    def __init__(self, name: str, in_stream: object,
                 out_stream: object, err_stream: object):
        #print("EL.__init__: begin")

        # verify streams have fileno()
        if ("fileno" not in dir(in_stream) or
                "fileno" not in dir(out_stream) or
                "fileno" not in dir(err_stream)):
            raise Exception("Streams must have fileno()")

        # setup the parent
        super().__init__(name, in_stream, out_stream, err_stream)

        # hooks
        self.completer = self._basic_completer
        self.display_matches = self._display_matches

        # command infra
        self.command_token = ':'
        self.commands = {}
        self.add_command('history', self.show_history)

        # tools
        self.keymap = {
            'tab': ['^I'],
        }


    def parse_and_bind(self, cmd: str) -> None:
        """Create the translation between "readline" and "bind"

        Args:
            cmd: a GNU style configuration command

        Returns:
            Nothing

        Build this out to eventually be able to remap the 'readline'
        commands into their libedit equivalents

        """
        key, routine = cmd.split(':')

        if key not in self.keymap:
            self.keymap[key] = routine


    def add_command(self, tag: str, fcn: callable):
        """Add a custom command to the list.

        Args:
            tag: the token to match on the command line
            fcn: callable to run when requested

        Returns:
            Nothing

        """
        if tag in self.commands:
            raise ValueError("Command '{0}' already is registered.".format(tag))

        if fcn is None or not callable(fcn):
            raise ValueError("Callback is invalid.")

        self.commands[tag] = fcn


    def _basic_completer(self, text: str) -> list:
        """Very basic completion support.

        This routine should be replaced by a better one.

        Args:
            text: python code line to be completed

        Returns:
            List of matching commands.

        """
        _ = text
        return []


    def _completer(self, text: str) -> list:
        """Intermediate completer.

        Handles the variations between the readline-way of doing things
        and just handing back the strings.

        Args:
            text: python code line to be completed

        Returns:
            List of matching commands.

        """

        # run the completion support
        matches = self.completer(text)

        # did something bad happen or just nothing to display?
        if not matches:
            return _editline.CC_REFRESH

        # locked down on a single item
        if len(matches) == 1:
            self.insert_text(matches[0][len(text):])
            return _editline.CC_REDISPLAY

        # a selection...
        self.display_matches(matches)

        # find longest common prefix
        prefix = os.path.commonprefix(matches)
        plen = len(prefix)

        # may need to wedge in a couple chars
        if plen > len(text):
            self.insert_text(matches[0][len(text):plen])

        return _editline.CC_REDISPLAY


    def _display_matches(self, matches: list) -> None:
        """Basic utility to display matches for user.

        Args:
            matches: list of matching strings

        Returns:
            Nothing

        """
        self.out_stream.write('\n')

        # alphebetize them...
        matches.sort()

        # find the longest one
        maxlength = -1
        for match in matches:
            if len(match) > maxlength:
                maxlength = len(match)

        # figure out how many to put on a terminal line...
        per_line = self.gettc('co') // (maxlength + 2)

        # floor this to make sure it does not give issues below
        if per_line <= 0:
            per_line = 1

        # draw the table.
        for idx, match in enumerate(matches):
            extra = '  '
            if (idx % per_line) == per_line-1:
                extra = '\n'
            self.out_stream.write(
                "{0:{width}}{1}".format(match, extra, width=maxlength))
        self.out_stream.write('\n')


    def show_history(self, args=None) -> None:
        """Print a list of historical commands.

        Args:
            args: optional parameters from command-line

        Returns:
            Nothing

        This routine is called internally.

        """
        # collect the current valid range
        first_ev = self.history(self.H_FIRST)
        last_ev = self.history(self.H_LAST)

        # we'll always finish here...
        finish = first_ev[0]

        # start?  assume "the beginning"
        idx = last_ev[0]

        # check the arg to see if it is a count of how many to display
        if args is not None and args.isnumeric():
            cnt = int(args)
            if cnt < first_ev[0]-last_ev[0]:
                idx = finish - cnt + 1

        # iterate through the list 'backwards' so the newest
        #   cmds are at the bottom
        while idx <= finish:
            try:
                event = self.history(self.H_PREV_EVENT, idx)
                print("{0:3d}  {1}".format(event[0], event[1].rstrip()))
            except ValueError:
                pass    # probably should handle this better
            finally:
                idx += 1

        # nothing for the parser to do
        return None


    def _run_command(self, cmd: str) -> (str, None):
        """Run a 'private' command.

        Args:
            cmd: private command to execute.

        Is called from the C code upon completion of a line. Check
        for the existance of a "custom" command to implement

        """
        # bail out immediately if no key
        if not cmd.startswith(self.command_token):
            return cmd

        # ok, it is one of the custom items

        # trim it
        cmd = cmd.replace(self.command_token, '', 1).rstrip()

        # split it into a base-cmd + args
        parts = cmd.split(maxsplit=1)
        base_cmd = parts[0]
        args = ''
        if len(parts) > 1:
            args = parts[1]

        # a short-hand history cmd?
        if base_cmd.isnumeric():
            idx = int(base_cmd)
            #print("CMD: {:d}".format(idx))

            # get the valid range
            first_ev = self.history(self.H_FIRST)
            last_ev = self.history(self.H_LAST)

            # make sure the requested history item is possible
            if first_ev[0] >= idx >= last_ev[0]:

                # look up the historic command by number
                event = self.history(self.H_PREV_EVENT, idx)
                if event is None:
                    return None

                # extract the cmd and return it.
                return event[1]

            # improper index
            print("Invalid history id: {:d}. Range is {:d} -> {:d}"
                  .format(idx, first_ev[0], last_ev[0]))

        # command decode...
        elif base_cmd in self.commands:
            routine = self.commands[base_cmd]
            return routine(args)

        # hmm. if we get here, it is an unknown infra cmd
        #   Error?  Certainly mark that it is consumed
        print("Invalid line-editor command.")
        return None


if __name__ == '__main__':
    import lineeditor
    ELINE = EditLine("tester", sys.stdin, sys.stdout, sys.stderr)
    LINE_ED = lineeditor.EditlineCompleter(subeditor=ELINE)
    ELINE.completer = LINE_ED.complete
    ELINE.readline()
