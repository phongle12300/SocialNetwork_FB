from facebook_gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.comboBoxYear.currentIndexChanged.connect(self.handleComboBoxYearChanged)
        self.ui.btnOpenCookie.clicked.connect(lambda: self.openFile("btnOpenCookie"))
        self.ui.btnOpenFileProxy.clicked.connect(
            lambda: self.openFile("btnOpenFileProxy")
        )
        self.ui.btnLinkPass.clicked.connect(lambda: self.openFile("btnLinkPass"))

    def handleTextChanged(self, text):
        print(text)

    def handleComboBoxYearChanged(self, value):
        print(self.ui.comboBoxYear.itemText(value))

    def openFile(self, caller):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setNameFilter("Text files (*.txt)")

        if file_dialog.exec_():
            sender_button = self.sender()
            selected_file = file_dialog.selectedFiles()[0]
            if sender_button == self.ui.btnOpenCookie:
                self.ui.txtFileCookie.setText(selected_file)

            elif sender_button == self.ui.btnOpenFileProxy:
                self.ui.txtFileProxy.setText(selected_file)

            elif sender_button == self.ui.btnLinkPass:
                self.ui.txtFileLinkPass.setText(selected_file)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myApp = MyApp()
    sys.exit(app.exec_())
