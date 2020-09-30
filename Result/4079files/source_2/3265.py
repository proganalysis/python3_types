"""Displays text as is on the display.

Can be used interactively or one-time through the command line.
"""
from typing import List

import sys
import time
import controller


class Writer:
    """Manages all interactivity or one-time display.
    """
    # === Private Attributes ===
    # _display:
    #   the lcd display controller
    # _delay:
    #   buffer time until accepting a new button press
    #   after receiving one

    def __init__(self, delay: int = 0.1) -> None:
        """Initializes the writer.
        """
        self._display = controller.Display()
        self._delay = delay

    def show(self, lines: List[str]) -> None:
        """Shows the list <lines> to screen in order.
        """
        for line in lines:
            self._display.write(line)

    def _check_plate_input(self) -> None:
        """Checks plate input and reacts accordingly by scrolling
        or other functionality.
        """
        button = self._display.check_pressed()
        if button == "":
            return
        elif button == "select":
            self._display.set_default()
        elif button == "left":
            self._display.side_scroll(1)
        elif button == "up":
            self._display.scroll(-1)
        elif button == "down":
            self._display.scroll(1)
        elif button == "right":
            self._display.side_scroll(-1)
        time.sleep(self._delay)

    def start_interactive(self, num_inputs: int = 0,
                                stop_keyword: str = "__END__") -> None:
        """Begins the interactive display.

        Stops after a number of inputs <num_inputs> (default 0 for no end)
        and/or when a <stop_keyword> is typed (default '__END__').
        """
        num = 0
        message = ""

        with controller.Input() as _input:
            while num_inputs == 0 or num < num_inputs:
                read = _input.read()
                
                # No input
                if read == '':
                    pass

                # Backspace
                elif read == '\b':
                    message = message[:-1]

                # Enter
                elif read == '\n':
                    num += 1

                    # Raise an error to stop the interactivity if
                    # the stop keyword was typed
                    if message == stop_keyword:
                        raise KeyboardInterrupt

                    self.show([message])
                    message = ""
                
                # Other
                else:
                    message += read

                self._check_plate_input()

    def start_headless(self, buf: List[str]) -> None:
        """Begins a headless version of the interactive display.

        Instead of waiting for user input, gets input from <buf> and displays
        whatever is in that.
        """
        while True:
            if len(buf) > 0:
                # Print out the messages to terminal
                for msg in buf:
                    print(msg)

                # Show the messages on the display and remove from buffer
                self.show(buf)
                while len(buf) > 0:
                    buf.pop()

            self._check_plate_input()


if __name__ == "__main__":
    # Initializes a new writer when the module is called
    writer = Writer()

    # Checks if there are any arguments (other than the file itself)
    if len(sys.argv) > 1:
        # If the first real argument is the headless tag,
        # run the Writer headlessly with the list coming
        # after the headless tag
        if sys.argv[1] == "--headless":
            writer.start_headless(sys.argv[2:])
        # Otherwise just show whatever the arguments were
        else:
            writer.show(sys.argv[1:])

    # If there are no real arguments,
    # then just start the writer interactively
    else:
        writer.start_interactive()
