from __future__ import print_function

import os
import sys
import time
import logging
import tempfile
import traceback
import subprocess

from shutil import disk_usage, rmtree

try:
    import pathlib
    import importlib.util
except ImportError:
    pass


class PIP(object):
    """ TODO """
    @classmethod
    def run(cls, command, check_output=False):
        """ TODO """
        if not cls.works():
            raise RuntimeError("Could not import pip.")

        try:
            return PIP.run_python_m(*command.split(),
                                    check_output=check_output)
        except subprocess.CalledProcessError as error:
            return error.returncode
        except:
            traceback.print_exc()
            print("Error using -m method")

    @classmethod
    def run_python_m(cls, *args, **kwargs):
        """ TODO """
        check_output = kwargs.pop('check_output', False)
        check = subprocess.check_output if check_output \
            else subprocess.check_call
        return check([sys.executable, '-m', 'pip'] + list(args))

    @classmethod
    def run_pip_main(cls, *args, **kwargs):
        """ TODO """
        import pip

        args = list(args)
        check_output = kwargs.pop('check_output', False)

        if check_output:
            from io import StringIO

            out = StringIO()
            sys.stdout = out

            try:
                pip.main(args)
            except:
                traceback.print_exc()
            finally:
                sys.stdout = sys.__stdout__

                out.seek(0)
                pipdata = out.read()
                out.close()

                print(pipdata)
                return pipdata
        else:
            return pip.main(args)

    @classmethod
    def run_install(cls, cmd, quiet=False, check_output=False):
        """ TODO """
        return cls.run(
            "install %s%s" % ('-q ' if quiet else '', cmd), check_output)

    @classmethod
    def run_show(cls, cmd, check_output=False):
        """ TODO """
        return cls.run("show %s" % cmd, check_output)

    @classmethod
    def works(cls):
        """ TODO """
        try:
            import pip
            return True
        except ImportError:
            return False

    # noinspection PyTypeChecker
    @classmethod
    def get_module_version(cls, mod):
        """ TODO """
        try:
            out = cls.run_show(mod, check_output=True)

            if isinstance(out, bytes):
                out = out.decode()

            datas = out.replace('\r\n', '\n').split('\n')
            expectedversion = datas[3]

            if expectedversion.startswith('Version: '):
                return expectedversion.split()[1]
            else:
                return [x.split()[1] for x in datas
                        if x.startswith("Version: ")][0]
        except:
            pass

    @classmethod
    def get_requirements(cls, file='requirements.txt'):
        """ TODO """
        from pip.req import parse_requirements
        return list(parse_requirements(file))


# Setup initial loggers
TMPFILE = tempfile.TemporaryFile('w+', encoding='utf8')
LOG = logging.getLogger('launcher')
LOG.setLevel(logging.DEBUG)

sh = logging.StreamHandler(stream=sys.stdout)
sh.setFormatter(logging.Formatter(
    fmt="[%(levelname)s] %(name)s: %(message)s"
))

sh.setLevel(logging.INFO)
LOG.addHandler(sh)

tfh = logging.StreamHandler(stream=TMPFILE)
tfh.setFormatter(
    logging.Formatter(fmt="[%(relativeCreated).9f] %(asctime)s \
    - %(levelname)s - %(name)s: %(message)s"))
tfh.setLevel(logging.DEBUG)
LOG.addHandler(tfh)


def finalize_logging():
    """ TODO """
    if os.path.isfile("logs/musicbot.log"):
        LOG.info("Moving old musicbot log")
        try:
            if os.path.isfile("logs/musicbot.log.last"):
                os.unlink("logs/musicbot.log.last")
            os.rename("logs/musicbot.log", "logs/musicbot.log.last")
        except:
            pass

    with open("logs/musicbot.log", 'w', encoding='utf8') as file_:
        TMPFILE.seek(0)
        file_.write(TMPFILE.read())
        TMPFILE.close()

        file_.write('\n')
        file_.write(" PRE-RUN SANITY CHECKS PASSED ".center(80, '#'))
        file_.write('\n\n')

    global tfh
    LOG.removeHandler(tfh)
    del tfh

    fh = logging.FileHandler("logs/musicbot.log", mode='a')
    fh.setFormatter(logging.Formatter(
        fmt="[%(relativeCreated).9f] %(name)s-%(levelname)s: %(message)s"
    ))
    fh.setLevel(logging.DEBUG)
    LOG.addHandler(fh)

    sh.setLevel(logging.INFO)

    dlog = logging.getLogger('discord')
    dlh = logging.StreamHandler(stream=sys.stdout)
    dlh.terminator = ''
    dlh.setFormatter(logging.Formatter('.'))
    dlog.addHandler(dlh)


def bugger_off(msg="Press enter to continue . . .", code=1):
    """ TODO """
    input(msg)
    sys.exit(code)


# TODO: all of this
def sanity_checks(optional=True):
    """ TODO """
    LOG.info("Starting sanity checks")
    # Required

    # Make sure we are on python3.5+
    req_ensure_py3()

    # Fix windows encoding issues
    req_ensure_encoding()

    # Make sure we're in a writeable env
    req_ensure_env()

    # Make our folders if needed
    req_ensure_folders()

    # Optional
    if not optional:
        return

    # check disk usage
    opt_check_disk_space()

    LOG.info("Checks passed.")


def req_ensure_py3():
    """ TODO """
    LOG.info("Checking for python 3.5+")

    if sys.version_info < (3, 5):
        LOG.warning("Python 3.5+ is required. This version is %s",
                    sys.version.split()[0])
        LOG.warning("Attempting to locate python 3.5...")

        pycom = None

        if sys.platform.startswith('win'):
            LOG.info('Trying "py -3.5"')
            try:
                subprocess.check_output('py -3.5 -c "exit()"', shell=True)
                pycom = 'py -3.5'
            except:

                LOG.info('Trying "python3"')
                try:
                    subprocess.check_output('python3 -c "exit()"', shell=True)
                    pycom = 'python3'
                except:
                    pass

            if pycom:
                LOG.info("Python 3 found.  Launching bot...")
                pyexec(pycom, 'run.py')

                # I hope ^ works
                os.system('start cmd /k %s run.py' % pycom)
                sys.exit(0)

        else:
            LOG.info('Trying "python3.5"')
            try:
                pycom = subprocess.check_output(
                    'python3.5 -c "exit()"'.split()).strip().decode()
            except:
                pass

            if pycom:
                LOG.info(
                    "\nPython 3 found.  Re-launching bot using: %s run.py\n",
                    pycom)
                pyexec(pycom, 'run.py')

        LOG.critical(
            "Could not find python 3.5. Please run the bot using python 3.5")
        bugger_off()


def req_ensure_encoding():
    """ TODO """
    LOG.info("Checking console encoding")

    if sys.platform.startswith('win') or \
            sys.stdout.encoding.replace('-', '').lower() != 'utf8':
        LOG.info("Setting console encoding to UTF-8")

        import io
        sys.stdout = io.TextIOWrapper(
            sys.stdout.detach(), encoding='utf8', line_buffering=True)
        # only slightly evil
        sys.__stdout__ = sh.stream = sys.stdout

        if os.environ.get('PYCHARM_HOSTED', None) not in (None, '0'):
            LOG.info("Enabling colors in pycharm pseudoconsole")
            sys.stdout.isatty = lambda: True


def req_ensure_env():
    """ TODO """
    LOG.info("Ensuring we are in the right folder")

    try:
        assert os.path.isdir('config'), 'folder "config" not found'
        assert os.path.isdir('musicbot'), 'folder "musicbot" not found'
        assert os.path.isfile(
            'musicbot/__init__.py'), 'musicbot folder is not a python module'

        assert importlib.util.find_spec(
            'musicbot'), "musicbot module is not importable"
    except AssertionError as error:
        LOG.critical("Failed environment check, %s", error)
        bugger_off()

    try:
        os.mkdir('musicbot-test-folder')
    except Exception:
        LOG.critical("Current working directory does not seem to be writable")
        LOG.critical("Please move the bot to a writable one")
        bugger_off()
    finally:
        rmtree('musicbot-test-folder', True)

    if sys.platform.startswith('win'):
        LOG.info("Adding local bins/ folder to path")
        os.environ['PATH'] += ';' + os.path.abspath('bin/')
        sys.path.append(os.path.abspath('bin/'))  # might as well


def req_ensure_folders():
    """ TODO """
    pathlib.Path('logs').mkdir(exist_ok=True)
    pathlib.Path('data').mkdir(exist_ok=True)


def opt_check_disk_space(warnlimit_mb=200):
    """ TODO """
    if disk_usage('.').free < warnlimit_mb * 1024 * 2:
        LOG.warning("""Less than %sMB of free space remains
            on this device""", warnlimit_mb)


def ensure_files():
    """ TODO """
    if os.path.isfile('config/config.ini') is False and \
     os.path.isfile('config/permissions.ini') is False:
        LOG.critical("""MISSING config/config.ini and config/permissions.ini!\n
            Either cp the config folder into the container or mount is as a volume!""")
        return True

#################################################

def pyexec(pycom, *args, pycom2=None):
    """ TODO """
    pycom2 = pycom2 or pycom
    os.execlp(pycom, pycom2, *args)


def restart(*args):
    """ TODO """
    pyexec(sys.executable, *args, *sys.argv, pycom2='python')


def main():
    """ TODO """
    # TODO: *actual* argparsing

    if '--no-checks' not in sys.argv:
        sanity_checks()

    finalize_logging()

    import asyncio

    tried_requirementstxt = False
    tryagain = True

    loops = 0
    max_wait_time = 60

    while tryagain:
        if ensure_files():
            tryagain = False
            break

        # Maybe I need to try to import stuff first, then actually import stuff
        # It'd save me a lot of pain with all that awful exception type
        # checking

        mbot = None
        try:
            from musicbot import MusicBot
            mbot = MusicBot()

            sh.terminator = ''
            LOG.info("Connecting")
            sh.terminator = '\n'

            mbot.run()

        except SyntaxError:
            LOG.exception("Syntax error (this is a bug, not your fault)")
            break

        except ImportError:
            # TODO: if error module is in pip or dpy requirements...

            if not tried_requirementstxt:
                tried_requirementstxt = True

                LOG.exception("Error starting bot")
                LOG.info("Attempting to install dependencies...")

                err = PIP.run_install('--upgrade -r requirements.txt')

                # TODO: add the specific error check back as
                # not to always tell users to sudo it
                if err:
                    print()
                    LOG.critical(
                        "You may need to %s to install dependencies." %
                        ['use sudo', 'run as admin']
                        [sys.platform.startswith('win')])
                    break
                else:
                    print()
                    LOG.info("Ok lets hope it worked")
                    print()
            else:
                LOG.exception("Unknown ImportError, exiting.")
                break

        except Exception as error:
            if hasattr(error, '__module__') and \
                    error.__module__ == 'musicbot.exceptions':
                if error.__class__.__name__ == 'HelpfulError':
                    LOG.info(error.args[0])
                    break

                elif error.__class__.__name__ == "TerminateSignal":
                    break

                elif error.__class__.__name__ == "RestartSignal":
                    restart()
            else:
                LOG.exception("Error starting bot")

        finally:
            if not mbot or not mbot.init_ok:
                if any(sys.exc_info()):
                    # How to log this without redundant messages...
                    traceback.print_exc()
                break

            asyncio.set_event_loop(asyncio.new_event_loop())
            loops += 1

        sleeptime = min(loops * 2, max_wait_time)
        if sleeptime:
            LOG.info("Restarting in %s seconds...", loops * 2)
            time.sleep(sleeptime)

    print()
    LOG.info("All done.")


if __name__ == '__main__':
    main()
