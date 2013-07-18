from PyQt4 import QtCore, QtGui
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        widget = QtGui.QWidget()
        self.setCentralWidget(widget)
        self.setWindowTitle(" для MINI-T400")
        self.resize(600, 300)
        label = QtGui.QLabel('')
        label2 = QtGui.QLabel('')
        #label = QtGui.QLabel('<font color="blue"><center>'+self.TERM('version')+'<center></font>')
        #label2 = QtGui.QLabel(self.TERM('protocol_version'))
        btnQuit = QtGui.QPushButton("&Закрыть окно")
        btnOpen = QtGui.QPushButton("Подключение")
        btnFormat = QtGui.QPushButton("Форматировние")
        vbox1 = QtGui.QVBoxLayout()
        vbox2 = QtGui.QVBoxLayout()
        vbox1.addWidget(label)
        vbox1.addWidget(label2)
        vbox1.addWidget(btnFormat)
        #vbox1.addWidget(btnQuit)
        vbox1.addWidget(btnOpen)
        widget.setLayout(vbox1)
       
        
        QtCore.QObject.connect(btnQuit, QtCore.SIGNAL("clicked()"),QtGui.qApp, QtCore.SLOT("quit()"))
        btnOpen.clicked.connect(self.Open)
        btnFormat.clicked.connect(self.Format)               
    def Open(self):
        err=''
        if self.TERM('privet')!= 'hello':
           err='НЕТ ОТВЕТА ОТ ТЕРМИНАЛА!!!'
        else:
            if  self.TERM('protocol_version')!= '1.08':
                err=('НЕИЗВЕСТНАЯ ВЕРСИЯ ПРОТОКОЛА!!!')
            else:
                # тут распологаются рабочие команды 
                self.TERM('beep')                
        print(err)
        ####################################################################
    def Format(self):
        err=''
        if self.TERM('privet')!= 'hello':
           err='НЕТ ОТВЕТА ОТ ТЕРМИНАЛА!!!'
        else:
            if  self.TERM('protocol_version')!= '1.08':
                err=('НЕИЗВЕСТНАЯ ВЕРСИЯ ПРОТОКОЛА!!!')
            else:
                # тут распологаются рабочие команды 
                self.TERM('beep')
                self.TERM(b'\x66\x6f\x72\x6d\x61\x74\x20\xfb\r\n',1)
                
        print(err)   
                
 ###########################################################################               
    def TERM(self,send,b=0):
        import serial,ctypes,codecs
        import sys,os
        #clear = lambda: os.system('cls')
        #clear()
        #print ("-"*78)
        port = "COM1"
        ser=serial.Serial()
        ser.port=port
        try:
            serial.Serial(port) # test open
        except serial.serialutil.SerialException:
            print ("Ошибка открытия порта. Может занят? (неверный номер порта?) ")
            print ("-"*78)
            return 
            #sys.exit("Ошибка открытия порта. Может занят? (неверный номер порта?) ")
        ser.timeout = 1
        ser.baudrate= "115200"
        #sdata = ctypes.create_string_buffer(1024)
        ser.open()
        #settings=ser.getSettingsDict()
        ser.setDTR(False)
        ser.setRTS(False)
        if b==0:
                ser.write(bytes(send+'\r\n','utf-8'))
                recive = ser.read(1024).decode("utf-8").rstrip("\r\n")
                print('Посыл терминалу: ')
                print (send)
                print ('Ответ терминала: ')
                print (recive)
                print ("-"*78)
        else:
                ser.write(send)
                recive = ser.read(1024)
                print('Посыл терминалу: ')
                print (send)
                print ('Ответ терминала: ')
                print (recive)
                print ("-"*78)
        ser.close()
        return recive
if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
