"""
Unit testing for parts of the editline and _editline modules.
"""
import os
import sys
import unittest
import subprocess
from test.support import import_module

# too bad this thing moved ...
try:
    if sys.version_info[0] >= 3 and sys.version_info[1] >= 5:
        from test.support.script_helper import assert_python_ok
    else:
        from test.script_helper import assert_python_ok
    have_assert_python_ok = True
except ImportError:
    have_assert_python_ok = False
    
def check_test_support():
    return have_assert_python_ok

def check_nose_runner():
    """Certain situations prevent NOSE from running tests -- it appears that nose does
       not allow access to the terminal."""
    return 'nose' not in sys.modules.keys()
    
class TestEditline(unittest.TestCase):

    def load_assert_python_ok(self):
        if sys.version_info[0] >= 3 and sys.version_info[1] >= 5:
            from test.support.script_helper import assert_python_ok
        else:
            from test.script_helper import assert_python_ok
    
    def test_001_import_pkg(self):
        _editline = import_module('editline')

    def test_002_import__el(self):
        _editline = import_module('editline._editline')

    def test_002_import_el(self):
        editline = import_module('editline.editline')

    @unittest.skipUnless(check_nose_runner(), "nose cannot run this test")
    def test_003_build_instance(self):
        editline = import_module('editline.editline')
        el = editline.EditLine("testcase",
                               sys.stdin, sys.stdout, sys.stderr)
        self.assertIsNotNone(el)

    @unittest.skipUnless(check_test_support(), "no script_helper")
    def test_100_import_pkg(self):
        self.load_assert_python_ok()
        #from test.support.script_helper import assert_python_ok
        rc, stdout, stderr = assert_python_ok('-c', 'import editline')
        self.assertEqual(stdout, b'')
        self.assertEqual(rc, 0)
    
    @unittest.skipUnless(check_test_support(), "no script_helper")
    def test_100_import_module(self):
        self.load_assert_python_ok()
        #from test.support.script_helper import assert_python_ok
        rc, stdout, stderr = assert_python_ok(
            '-c', 'from editline import editline')
        self.assertEqual(stdout, b'')
        self.assertEqual(rc, 0)
    
    @unittest.skipUnless(check_test_support(), "no script_helper")
    def test_100_import_class(self):
        self.load_assert_python_ok()
        #from test.support.script_helper import assert_python_ok
        rc, stdout, stderr = assert_python_ok(
            '-c', 'from editline.editline import EditLine')
        self.assertEqual(stdout, b'')
        self.assertEqual(rc, 0)
    
    @unittest.skipUnless(check_test_support(), "no script_helper")
    def test_101_init(self):
        # Issue #19884: Ensure that the ANSI sequence "\033[1034h" is not
        # written into stdout when the readline module is imported and stdout
        # is redirected to a pipe.
        self.load_assert_python_ok()
        #from test.support.script_helper import assert_python_ok
        rc, stdout, stderr = assert_python_ok(
            '-c', 'from editline.editline import EditLine',
            TERM='xterm-256color')
        self.assertEqual(stdout, b'')
        self.assertEqual(rc, 0)

    @unittest.skipUnless(check_nose_runner(), "nose cannot run this test")
    def test_200_terminal_size(self):
        rows = int(subprocess.check_output(['tput', 'lines']).decode())
        columns = int(subprocess.check_output(['tput', 'cols']).decode())

        self.assertNotEqual(columns, 0)

        editline = import_module('editline.editline')
        el = editline.EditLine("testcase",
                               sys.stdin, sys.stdout, sys.stderr)
        el_cols = el.gettc('co')
        self.assertEqual(el_cols, columns)

if __name__ == "__main__":
    unittest.main()
