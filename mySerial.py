import Queue #, Empty
from threading import Thread
import serial
 
def pchar(c):
    return c if ord(c)<127 and ord(c)>=32 else "."
    
def printMsg(msg):
    N = 16
    hexa = char = ""
    print("-" * (N*3 + N))
    for i, c in enumerate(msg):
        if i % N == 0:
            if i != 0: print(hexa + char)
            hexa = char = ""
        hexa = hexa + "{:0>2X} ".format(ord(c))
        char = char + pchar(c)           
    print(hexa + "   " * (N-1 - i%N) + char)  
       
def _listMsgs(q):    
    try:
        while True:
            yield q.get_nowait()
    except Queue.Empty:
        raise StopIteration
                    
class mySerial():
    def __init__(self, parent=None):
        self.ser = serial.Serial("COM3", 115200)
        self.fifo = Queue.Queue()
        self._on = True
        self.th = Thread(target=self._th_read)
        self.th.start()
           
    def _th_read(self):
        while self._on:
            msg = self.ser.readline().rstrip('\r\n')
            self.fifo.put(msg)
            if len(msg)>0:
                printMsg(msg)
    
    def readMsg(self):
        return list(_listMsgs(self.fifo))
    
    def writeMsg(self, msg):
        self.ser.write(msg + '\r')

    def stop(self):
        self.ser.close()
        self._on = False
        self.th.join()
        print("Outing!!!")
        