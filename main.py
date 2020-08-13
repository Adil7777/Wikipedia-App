from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
import sys
from wiki import get_page


class WikiApp(QMainWindow):
    def __init__(self):
        super(WikiApp, self).__init__()
        loadUi('C:\Рабочий стол\wikiapp\wiki.ui', self)
        self.Return = 0

        self.button.clicked.connect(self.loadResult)
        self.show()

    @pyqtSlot()
    def loadResult(self):
        try:
            search = self.Edit.text()
        except:
            search = 'pls edit smth'

        self.Result.setText(str(get_page(search)))


app = QApplication(sys.argv)
window = WikiApp()
try:
    sys.exit(app.exec_())
except:
    print('exit')
