from objp.util import pyref

class PyMain:
    def __init__(self, callback: pyref):
        self.callback = callback
    
    def hello_(self, name: str):
        print("Hello %s!" % name)
        print("Now, let's perform our callback.")
        self.callback.thisIsCalledBackFromPython_('foobar')
