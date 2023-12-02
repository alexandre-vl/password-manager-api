import os
from pathlib import Path
import sys

from PySide6.QtCore import Qt, QUrl
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView

CURRENT_DIRECTORY = Path(__file__).resolve().parent


class webView(QWidget):
    def __init__(self):
        super(webView, self).__init__()

        filename = os.fspath(CURRENT_DIRECTORY / "templates/index.html")
        url = QUrl.fromLocalFile(filename)

        self.webV = QWebEngineView()
        self.webV.load(url)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.webV)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    web = webView()
    web.show()

    sys.exit(app.exec_())
