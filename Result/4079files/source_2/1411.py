import os
import shutil
import datetime
import subprocess


def datetime_filename():
    """Returns a date/time string in a format suitable to be used for
    naming a file."""
    return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')


def read_n_lines(f, n):
    assert n > 0, 'Line number must be > 0'
    for ln in f:
        yield ln
        n -= 1
        if n <= 0:
            raise StopIteration()


def mkdir_p(path):
    """Create all directories in the specified path.
    Functionally equivalent to UNIX's mkdir -p.
    Adapted from: http://stackoverflow.com/questions/600268"""
    try:
        os.makedirs(path)
    except FileExistsError:
        pass

    return path


def rm(path):
    """Removes path, where path is either a file or a folder.
    Returns True if the path is removed, False otherwise.
    """
    try:
        try:
            shutil.rmtree(path)
        except NotADirectoryError:
            os.remove(path)
        return True
    except FileNotFoundError:
        return False


def count_lines(fp):
    """Counts the number of lines in file fp"""
    with open(fp) as f:
        return sum(1 for _ in f)


def process_call(cmd, shell=False, ignore_err=False):
    """Execute proces call specified in list cmd"""
    if shell:
        cmd = ' '.join(cmd)

    proc = subprocess.Popen(
        cmd, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    msg_out, msg_err = proc.communicate()

    msg_out = msg_out.decode('utf-8')
    msg_err = msg_err.decode('utf-8')

    if not ignore_err:
        if msg_err:
            err_msg = ('subprocess exited with error: \n%s' %
                       '\n'.join([(' ' * 4 + str(l))
                                  for l in msg_err.split('\n')]))
            raise IOError(err_msg)
        else:
            return msg_out
    else:
        return msg_out, msg_err
