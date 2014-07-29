import sys

from PyQt4.QtCore import SIGNAL, QTimer
from PyQt4.QtGui import QApplication, QDialog

# o pyuic cria o script GUI.py com a classe Ui_dlgMain
# dado que designei a janela de dlgMain
from GUI import Ui_dlgMain

import mySerial

# a classe AppForm deve herdar a classe Ui_dlgMain
class AppForm(QDialog, Ui_dlgMain):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        
        # para criar a GUI temos que chamar o metodo setupUi
        self.setupUi(self)
        
        self.setWindowTitle('Main designer GUI')
        self.resize(600, 200)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_tick)
        self.timer.start(100) 

        self.chkLED.setChecked(False)
        self.connect(self.chkLED, SIGNAL('stateChanged(int)'), self.on_chkLED)
        self.butSend.clicked.connect(self.on_butSend)
                 
        self.ser = mySerial.mySerial()
            
    def on_butSend(self):
        self.ser.writeMsg(str(self.edtCmd.text()))

    def closeEvent(self, event):
        self.ser.stop()
         
    def timer_tick(self):
        l = self.ser.readMsg()
        for i in l:
            self.txtLog.append(i)

    def on_chkLED(self):
        if self.chkLED.checkState():
            s = "LED ON"
            self.ser.writeMsg("l1")
        else:
            s = "LED OFF"
            self.ser.writeMsg("l0")
        self.txtLog.append(s)
                     
def main():
    app = QApplication(sys.argv)
    form = AppForm()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()