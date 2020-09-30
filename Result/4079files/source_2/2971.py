"""Screenshot and that kind of stuff."""
import io
from PyQt5.QtCore import QUrl, QIODevice, QBuffer, QByteArray
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Screenshot(QWebEngineView):
    def __init__(self):
        self.app = QApplication([])
        QWebEngineView.__init__(self)
        self._loaded = False
        self.loadFinished.connect(self._load_finished)
        print('--finish init')

    def capture(self, url):
        print('--load')
        self.load(QUrl(url))
        self.wait_load()
        self.show()
        size = self.page().contentsSize()
        self.page().view().resize(*[int(s) for s in [size.width(), size.height()]])
        print('--take image')
        image = QImage(800, 800, QImage.Format_ARGB32)
        painter = QPainter(image)
        print('--render')
        self.page().view().render(painter)
        painter.end()
        print('Saving QImage')
        img_bytes = QByteArray()
        bio = QBuffer(img_bytes)
        bio.open(QIODevice.WriteOnly)
        image.save(bio, 'PNG')
        return img_bytes

    def wait_load(self):
        while not self._loaded:
            self.app.processEvents()
        self._loaded = False

    def _load_finished(self, result):
        self._loaded = True
