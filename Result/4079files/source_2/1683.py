class Command:
    def __init__(self, cmd, bufsize=-1, timeout=5, env=None):
        self.cmd = cmd
        self.bufsize = bufsize
        self.timeout = timeout
        self.env = env
