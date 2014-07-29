import sys

from PyQt4.QtCore import QTimer, SIGNAL
from PyQt4.QtGui import QApplication, QDialog, QHBoxLayout, QVBoxLayout, QTabWidget, \
                            QWidget, QCheckBox, QLabel, QTextBrowser

class AppForm(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle('manualGUI')
        self.resize(600, 400)
        self.create_main_frame()
        print('Start!!!\r\n')
            
    def closeEvent(self, event):
        print('Stop!!!\r\n')
            
    def on_chkLED(self):
        if self.chkLED.checkState():
            print('On\r\n')
        else:
            print('On\r\n')
     
    def timer_tick(self):
        print('Tick!!!\r\n')
    
    def create_main_frame(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_tick)

        self.horizontalLayout = QHBoxLayout(self)
        self.tabs = QTabWidget(self)
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, "t1")
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2, "t2")
        self.horizontalLayout.addWidget(self.tabs)
                
        self.chkLED = QCheckBox("LED", self.tab1)
        self.chkLED.setChecked(False)
        self.connect(self.chkLED, SIGNAL('stateChanged(int)'), self.on_chkLED)
                
        self.labButton = QLabel("Button OFF", self.tab1)
        
        self.memo = QTextBrowser(self.tab1)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.chkLED)
        vbox.addWidget(self.labButton)
        vbox.addWidget(self.memo)
        self.tab1.setLayout(vbox)
        
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)
        self.axes = self.fig.add_subplot(111)
        
        hbox = QVBoxLayout()
        hbox.addWidget(self.canvas)
        self.tab2.setLayout(hbox)        

        self.tabs.setCurrentIndex(1)
                
def main():
    app = QApplication(sys.argv)
    form = AppForm()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()