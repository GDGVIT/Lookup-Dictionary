import sys
sys.path.insert(0, './KeyHandlers')
from KeyListener import KeyListener
from HandleClass import Handler
import pyperclip
import pyautogui
from pynput.keyboard import Key, Controller
sys.path.insert(0, './Ui')
from lookupBox2 import Ui_Form
from PyQt4 import QtGui

error=False
class DictionBox(QtGui.QWidget, Ui_Form):
    global error
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        text = pyperclip.paste()
        self.setupUi(self, text,error)


def StartCopy():
    import sys
    keyboard = Controller()
    with keyboard.pressed(Key.ctrl):
        keyboard.press('c')
        keyboard.release('c')

    app = QtGui.QApplication(sys.argv)
    window = DictionBox()
    window.show()
    app.quit()
    app.exec_()
    while True:
        keylistener = KeyListener()
        keylistener.addKeyListener("L_CTRL+i", StartCopy)
        handle = Handler(keylistener)

try:
    keylistener = KeyListener()
    keylistener.addKeyListener("L_CTRL+i", StartCopy)
    handle = Handler(keylistener)
except:
    error=True
