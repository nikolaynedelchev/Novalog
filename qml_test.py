from ast import Num
import sys
import os
from tokenize import String
import PySide6.QtQml as QtQml
import PySide6.QtGui as QtGui
import PySide6.QtCore as Qt
import json

class MainBackend(Qt.QObject):
    def __init__(self):
        Qt.QObject.__init__(self)
    signalPrintTxt_Sasho = Qt.Signal(bool)
    signalPrintTxt = Qt.Signal(bool, int, str, list, str)

    @Qt.Slot()
    def printTxt(self):
        print("Hello world from Python backend")
        self.signalPrintTxt_Sasho.emit(True)
        self.signalPrintTxt.emit(False, 666, 'ehoo', ['my list', 12, 'list end'],
        json.dumps(dict({
            "name": "ndn",
            "age": 256
        })))
        print("Hello back from Python backend")


if __name__ == "__main__":
    os.environ["QT_QUICK_BACKEND"] = "software"
    app = QtGui.QGuiApplication(sys.argv)
    engine = QtQml.QQmlApplicationEngine()
    mainBackend = MainBackend()
    engine.rootContext().setContextProperty("backend", mainBackend)
    engine.load('./test.qml')
    if not engine.rootObjects():
        sys.exit(-1)
    try:
        res = app.exec()
        sys.exit(res)
    except:
        pass
    