"""
Module providing support to create more interactive PTY sessions.
"""

import sys
import os
import time
from errno import EIO
import pty
import subprocess
import selectors

class PtyTimeoutError(Exception):
    pass

class InteractivePTY(object):
    """Class implementation of a PTY interface to an interactive interpreter.
    This is used to provide tool automation in a more simplistic form.
    """

    def __init__(self, tool, prompt, exit_cmd, args=[], encoding='UTF-8'):
        """Create an interactive PTY session
        tool     - full name of the executable to run
        prompt   - token to treat as the interpreter's prompt
        exit_cmd - command to tell the interpreter to exit cleanly
        args     - extra arguments (list) to pass to launcher (def: [])
        encoding - downstream interpreter's encoding (def: UTF-8)
        """
        if not os.path.exists(tool):
            raise ValueError("'{}' is not found".format(tool))

        if prompt == '':
            raise ValueError("prompt must be a valid string")

        self._tool = tool
        self._tool_args = args
        self._prompt = prompt
        self._encoding = encoding
        self._exit_cmd = exit_cmd

        # where to accumulate incoming data
        self._raw_buffer = b''

        # cook up a PTY
        self.master, self.slave = pty.openpty()

        # hook it up to a subprocess
        args = [self._tool] + self._tool_args
        self.proc = subprocess.Popen(args,
                                     stdin=self.slave,
                                     stdout=self.slave,
                                     stderr=self.slave)
        self.proc_rc = None

        # register a selector manager
        self.sel = selectors.SelectSelector()
        self.sel.register(self.master,
                          selectors.EVENT_READ | selectors.EVENT_WRITE)

        # try to avoid os interference
        if sys.version_info[0] >= 3 and sys.version_info[1] >= 5:
            os.set_blocking(self.master, False)
        else:
            import fcntl
            flag = fcntl.fcntl(self.master, fcntl.F_GETFL)
            fcntl.fcntl(self.master, fcntl.F_SETFL, flag | os.O_NONBLOCK)

    def __del__(self):
        """Normally, this is not necessary, but this class could have
        a bunch of dangling resources, in particular the subprocess.
        If it is not dead, it is killed off here for sure.
        """
        if self.proc:
            try:
                self.proc.kill()
            except ProcessLookupError:
                # Workaround for Open/Net BSD bug (Issue 16762)
                pass
        if self.master:
            os.close(self.master)
        if self.slave:
            os.close(self.slave)

    def close(self):
        """Shut down the interpreter cleanly, waiting for it to exit.
        This routine requires 'exit_cmd' to be set in the constructor
        as it is issued here to try to get the interpreter to close-out
        naturally.
          Attribute proc_rc is set with the result of the wait.
        """
        self.cmd(self._exit_cmd, marker='\n')
        self.proc_rc = self.proc.wait()

    def get_data(self, marker='\n', timeout=0):
        """Collect the output of the interpreter.

        marker - token to identify the end of the output ('\n')
        timeout - seconds to keep looking for the marker before giving up (0)

        Returns tuple: (tok, predata)
           tok     - the matched marker
           predata - everything read up until marker was found
        """

        # the data is managed as bytes
        marker = marker.encode(self._encoding)

        # do we already have it?
        tok, predata, self._raw_buffer = self._parse_marker(marker,
                                                            self._raw_buffer)
        if tok == marker:
            return tok.decode(self._encoding), predata.decode(self._encoding)

        # remember when we begin
        end_time = time.time() + timeout

        # nope, rummage for more data
        while True:
            for [_, events] in self.sel.select(timeout):
                if events & selectors.EVENT_READ:
                    try:
                        chunk = os.read(self.master, 0x10000)
                    except OSError as err:
                        # Linux raises EIO when slave is closed (Issue 5380)
                        if err.errno != EIO:
                            raise
                        chunk = b""

                    if chunk is None:
                        continue

                    elif chunk == b'':
                        continue

                    else:
                        # remember it
                        self._raw_buffer += chunk  #.decode(self._encoding)

                        # check for the marker
                        tok, predata, self._raw_buffer = \
                            self._parse_marker(marker, self._raw_buffer)
                        if tok == marker:
                            return (
                                tok.decode(self._encoding),
                                predata.decode(self._encoding)
                                )
                else:
                    # bailout if the timeout has exceeded
                    if end_time < time.time():
                        raise PtyTimeoutError("Timeout")

    @staticmethod
    def _parse_marker(marker, data):
        """Snoop through the given data looking for the marker.

        marker - token to look for
        data - data to be acted on

        Note: both arguments must match in type! (str,str) or (bytes,bytes)

        Return the found marker, the data preceding it and the data following.
        If the returned marker is None, it was not found and predata is also
        None.
        """
        try:
            predata, data = data.split(marker, 1)
        except ValueError:
            # no marker ...
            marker = None
            predata = None

        return marker, predata, data

    def send_data(self, data, add_crlf=True):
        """Issue data to the interpreter.

        data - str containing the info to send
        add_crlf - add a 'return' to the end of the data (default: True)

        It is not advised to use this externally, but it can be
        handy in certain cases.
        """
        retries = 5

        # most interpreters want a newline
        if add_crlf:
            data += '\n'

        # switch to the target encoding
        bdata = data.encode(self._encoding)

        # chug until we've written our data
        while True:
            for [_, events] in self.sel.select():
                if events & selectors.EVENT_WRITE:
                    try:
                        bdata = bdata[os.write(self.master, bdata):]
                    except OSError as err:
                        # Apparently EIO means the slave was closed
                        if err.errno != EIO:
                            raise

                    # return unwritten data. '' means everything went...
                    return bdata.decode(self._encoding)
                else:
                    # try a bit harder -- wait a bit for the buffer to drain
                    if len(bdata) > 0 and retries > 0:
                        time.sleep(0.1)
                        retries -= 1
                        continue

                    # bail out, can write no more
                    return ''

    def first_prompt(self):
        """Collect the initial start-up output generated from the interpreter
        and return it to the user.  Searches for self._prompt as the indication
        the interpreter is ready to go.
        """

        # collect initial output
        prompt, data = self.get_data(self._prompt, 1)

        # got it...
        if prompt is not None:
            return data

        # no prompt? snooze a bit and retry
        time.sleep(0.1)
        prompt, data = self.get_data(self._prompt, 1)
        return data

    def sync_prompt(self):
        """Try to coax the interpreter back in to a clean state.

        Returns True if it succeeds.
        """

        self._raw_buffer = b''

        # poke it a few times...
        tries = 5
        while tries > 0:
            tries -= 1
            self.send_data('\n')
            (prompt, _) = self.get_data(self._prompt, 0.1)
            if prompt == self._prompt:
                return True

        # hmm. dead?
        return False


    def cmd(self, cmd, marker=None, as_string=False,
            timeout=1, trim_cmd=True, add_crlf=True):
        """Issue a command-string to the underlying interpreter
        then collect and return any generated output until a marker/prompt
        is seen.

        cmd - the single-line command string to execute
        marker - prompt or token to declare the command is done
                  (default self._prompt)
        as_string - prefer the response to be one big str
        timeout - seconds of delay before declaring that the interpreter wedged
        trim_cmd - remove the 'echo' of the command string from output
                   (default: True)
        add_crlf - append a CR/LF combination to complete the cmd
                   (default: True)
        """

        # make sure a marker is set
        if marker is None:
            marker = self._prompt

        # clear out any accumulated cruft
        try:
            while True:
                prompt, data = self.get_data(marker, timeout=0.1)
                if prompt is None:
                    break
        except PtyTimeoutError:
            pass   # nothing relevant available

        # fire off the instruction
        self.send_data(cmd, add_crlf)

        # collect the result
        prompt, data = self.get_data(marker, timeout=timeout)

        # return it as requested
        if as_string:
            return data

        if data is None:
            return []

        lines = data.splitlines()
        if trim_cmd:
            lines.pop(0)

        return lines

    def run_script(self, script):
        """Issue a sequence of commands (script) to the interpreter, then
        collect all generated output and return it.

        script - [str|list] sequence of commands to run

        Note: will split 'str' based on os.linesep.
        """

        # scripts should be run one line at a time
        if isinstance(script, str):
            cmds = script.split(os.linesep)
        else:
            cmds = script

        # want to collect all the output in one go
        output = []

        # iterate them
        for cmd in cmds:
            cmd_output = self.cmd(cmd)
            output.extend(cmd_output)

        # done
        return output


# bootstrap
if __name__ == '__main__':
    tool = InteractivePTY(sys.executable, '>>>', 'exit()')
    cruft = tool.first_prompt()
    print('First Prompt:', os.linesep, cruft)

    try:
        cruft = tool.cmd(tool._exit_cmd)
    except PtyTimeoutError:
        cruft = '<timeout>'
    finally:
        print('Exit:', os.linesep, cruft)
        print('Exit:', os.linesep, cruft)
    
