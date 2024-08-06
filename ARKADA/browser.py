import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIcon


class BackButton(QToolButton):
    def __init__(self, parent=None):
        super(BackButton, self).__init__(parent)
        self.setIcon(QIcon("back.png"))
        self.setIconSize(QSize(24, 24))
        self.setToolTip("Назад")


class ForwardButton(QToolButton):
    def __init__(self, parent=None):
        super(ForwardButton, self).__init__(parent)
        self.setIcon(QIcon("vper.png"))
        self.setIconSize(QSize(24, 24))
        self.setToolTip("Вперед")


class ReloadButton(QToolButton):
    def __init__(self, parent=None):
        super(ReloadButton, self).__init__(parent)
        self.setIcon(QIcon("reload.png"))
        self.setIconSize(QSize(24, 24))
        self.setToolTip("Перезагрузить")


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://duckduckgo.com/"))

        self.setCentralWidget(self.browser)

        navtb = QToolBar()
        self.addToolBar(navtb)

        back_btn = BackButton()
        back_btn.clicked.connect(self.browser.back)
        navtb.addWidget(back_btn)

        forward_btn = ForwardButton()
        forward_btn.clicked.connect(self.browser.forward)
        navtb.addWidget(forward_btn)

        reload_btn = ReloadButton()
        reload_btn.clicked.connect(self.browser.reload)
        navtb.addWidget(reload_btn)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        self.statusBar().showMessage("https://t.me/arkadasoft")

        self.show()

        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)

        # Установка иконки для приложения
        self.setWindowIcon(QIcon("ikonka.png"))

    def update_title(self):
        self.setWindowTitle("Arkada Browser")

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("https")
        self.browser.setUrl(q)

    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)


app = QApplication(sys.argv)
window = MainWindow()
app.exec_()
