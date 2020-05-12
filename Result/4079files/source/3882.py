"""Controls all basic functionality of the Raspberry Pi 3
like initialization, information display, and input.
"""
from typing import Tuple

import curses
import Adafruit_CharLCD as LCD


class Display:
    """Manages all display functionality regarding the 16x2 LCD display.
    """
    # === Private Attributes ===
    # _lcd:
    #   the lcd display
    # _log:
    #   list of all strings displayed
    # _cur_index:
    #   where we are currently displaying in the log
    # _cur_side_index:
    #   where we are currently in each line

    def __init__(self, initializers: Tuple[str, str] = ("", "")) -> None:
        """Initializes the display.
        """
        self._lcd = LCD.Adafruit_CharLCDPlate()
        self._log = list(initializers)
        self._cur_index = 1
        self._cur_side_index = 0
        self.clear()
        self.show()

    def clear(self) -> None:
        """Clears the display.
        """
        self._lcd.clear()

    def get_on_screen(self) -> Tuple[str, str]:
        """Returns a tuple of the currently on-screen strings.
        """
        return (self._log[self._cur_index - 1].rstrip(),
                self._log[self._cur_index].rstrip())

    def _put(self, line1: str, line2: str) -> None:
        """Puts each line onto the screen.
        """
        self._lcd.message(line1 + "\n" + line2)

    def show(self) -> None:
        """Shows the current messages from the log.
        """
        self.clear()
        line1 = self._log[self._cur_index - 1]
        line2 = self._log[self._cur_index]
        self._put(line1[self._cur_side_index:] + line1[:self._cur_side_index],
                  line2[self._cur_side_index:] + line2[:self._cur_side_index])

    def write(self, message: str) -> None:
        """Displays <message> at the bottom of the screen and appends
        it to <_log>.
        """
        # Splits up the message into equal parts
        message_parts = []
        num_message_parts = (len(message) // 39) + 1
        part_length = len(message) // num_message_parts
        for i in range(num_message_parts):
            if i == num_message_parts - 1:
                message_parts.append(message[i * part_length:])
                break
            message_parts.append(message[i * part_length:(i + 1) * part_length])
        
        # Shows each part
        for message_part in message_parts:
            # Pads the message with spaces if it less than 16 chars
            # then adds an extra two spaces of padding
            while len(message_part) < 16:
                message_part += " "
            message_part += "  "

            self._log.append(message_part)
            self._cur_index += 1
        self.show()

    def scroll(self, displacement: int) -> None:
        """Scrolls through the log by <displacement>.
        Negative upwards, positive downwards.
        """
        self._cur_index = (displacement + self._cur_index) % len(self._log)
        self.show()

    def side_scroll(self, displacement: int) -> None:
        """Scrolls through the all the log horizontally by <displacement>.
        Negative left, positive right.
        """
        _len = max(len(self._log[self._cur_index - 1]),
                   len(self._log[self._cur_index]))
        self._cur_side_index = (displacement + self._cur_side_index) % _len
        self.show()

    def set_default(self) -> None:
        """Reverts all scrolling and sets the display back to the most recent.
        """
        self._cur_index = len(self._log) - 1
        self._cur_side_index = 0
        self.show()

    def check_pressed(self) -> str:
        """Checks if any button has been pressed and returns a string
        representation of the button. If there is no button returns an
        empty string.
        """
        buttons = ((LCD.SELECT, "select"),
                   (LCD.LEFT,   "left"  ),
                   (LCD.UP,     "up"    ),
                   (LCD.DOWN,   "down"  ),
                   (LCD.RIGHT,  "right" ))
        
        for button in buttons:
            if self._lcd.is_pressed(button[0]):
                return button[1]
        return ""


class Input:
    """Manages all input using <curses>.
    """
    # === Private Attributes ===
    # _window:
    #   the curses window, only initialized when <start> is called

    def __enter__(self) -> 'Input':
        """Called when using the <with-as> syntax.

        Starts the input manager and returns the started instance.
        """
        self.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """Called when exiting the <with-as> syntax.
        
        Used to catch errors and make sure the console is not
        going to messed up by curses.

        Swallows the error if it is a KeyboardInterrupt
        """
        self.stop()
        return exc_type == KeyboardInterrupt

    def start(self) -> None:
        """Starts the input structure.
        """
        self._window = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self._window.nodelay(True)

    def read(self) -> chr:
        """Gets the character input from the user and returns it.
        """
        get_chr = self._window.getch()
        # No character
        if get_chr == -1:
            return ''

        # Backspace
        if get_chr == 127:
            y, x = self._window.getyx()
            if x > 0:
                self._window.move(y, x - 1)
                self._window.delch(y, x - 1)
            return '\b'

        # Other
        self._window.addch(get_chr)
        return chr(get_chr)

    def stop(self) -> None:
        """Stops the curses input handler.
        """
        curses.echo()
        curses.nocbreak()
        curses.endwin()
