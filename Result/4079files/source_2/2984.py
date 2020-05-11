#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os
import sys
import subprocess
from shutil import rmtree

from setuptools import find_packages, setup, Command

here = os.path.abspath(os.path.dirname(__file__))

# Package meta-data.
NAME = "slick-app"
DESCRIPTION = "Easy to use secure file sending & chatting"
URL = "https://github.com/joshbuddy/slick"
EMAIL = "joshbuddy@gmail.com"
AUTHOR = "joshbuddy"
REQUIRES_PYTHON = ">=3.7.0"
VERSION = None
EXTRAS = {}
with open(os.path.join(here, "requirements.txt")) as f:
    REQUIRED = list(map(lambda l: l.strip(), f.readlines()))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, "slick", "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        subprocess.check_call(
            [sys.executable, "setup.py", "sdist", "bdist_wheel", "--universal"]
        )

        self.status("Uploading the package to PyPI via Twine…")
        subprocess.check_call(self.twine_command())

        self.status("Pushing git tags…")
        subprocess.check_call(["git", "tag", "v{0}".format(about["__version__"])])
        subprocess.check_call(["git", "push", "--tags"])

        sys.exit()

    def twine_command(self):
        return ["twine", "upload", "dist/*"]


class UploadTestCommand(UploadCommand):
    def twine_command(self):
        return ["twine", "upload", "-r", "pypitest", "dist/*"]


# Where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    entry_points={
        'console_scripts': ['slick=slick.repl:run'],
    },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    # $ setup.py publish support.
    cmdclass={"upload_test": UploadTestCommand, "upload": UploadCommand},
)
