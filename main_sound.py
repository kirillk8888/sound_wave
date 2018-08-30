from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys
import wave
import matplotlib.pyplot as plt
import matplotlib.ticker

import matplotlib.ticker as ticker
import struct
import pylab as pl
from design_2 import *
import io
from PIL import Image
import matplotlib.ticker as tkr
from PIL.ImageQt import ImageQt

class MyWindow(QMainWindow):
    def __init__(self, parent=Ui_MainWindow):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.close)
        self.ui.pushButton.clicked.connect(self.on_clicked)
        self.ui.pushButton_2.clicked.connect(self.clear)
        self.ui.action.triggered.connect(self.on_clicked)
        self.ui.action_2.triggered.connect(self.clear)
        self.ui.action_3.triggered.connect(self.close)

        self.ui.action_4.triggered.connect(self.mono)
        self.ui.action_6.triggered.connect(self.build_graph)

    """Функция перевода в моно файл, проверка на соответствие моно/стерео"""
    def mono(self):                     
        f = open(self.d, "rb")
        buf = f.read(44)
        a = struct.unpack("4si4s4sihhiihh4si", buf)
        nchannels = a[6]              #распаковали
        if nchannels == 1:
            print("У вас и так моно файл")
            self.ui.action_4.setEnabled(False)
        else:
            d = open("1.wav", "wb")
            g = open("2.wav", "wb")


            #кортеж в список, чтобы можно было поменять 1 элемент (2 на 1 (стерео на моно)) и не только
            b = list(a)     

            #меняем 1 элемент и не только
            b[6] = 1
            b[8] = b[8] // 2
            b[9] = b[9] // 2
                
            #запаковываем обратно
            b1 = struct.pack("4si4s4sihhiihh4si", b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8], b[9], b[10], b[11], b[12]) 
            # 
            print(b1)

            d.write(b1)
            g.write(b1)
            #проверяем поэлементно соответствие структуре wav файла
            if a[0] != b"RIFF":
                print("Error")
            if a[1] != 88228:
                print("Error")
            if a[2] != b"WAVE":
                print("Error")
            if a[3] != b"fmt ":
                print("Error")
            if a[4] != 16:
                print("Error")
            if a[5] != 1:
                print("Error")
            if a[6] != 2:
                print("Error")
            if a[7] != 44100:
                print("Error")
            if a[8] <=0:
                print("Error")
            if a[9] <=0:
                print("Error")
            if a[10] % 8 != 0:
                print("Error")
            if a[11] != b"data":
                print("Error")
                
            while True:
                buf = f.read(4)
                if not buf:
                    break
                c = struct.unpack("i", buf)[0]
                c1 = struct.pack("i", c)
                d.write(c1)
                
                buf = f.read(4)
                if not buf:
                    break
                e = struct.unpack("i", buf)[0]
                e1 = struct.pack("i", e)
                g.write(e1)

            d.close()
            g.close()


    def stereo(self):
        pass


    def on_clicked(self):
        fl, l = QtWidgets.QFileDialog.getOpenFileUrl(parent=self,
            caption="Открыть файл",
            directory="file:///" + QtCore.QDir.currentPath(),
            filter="All (*);;wav (*.wav)")
        print(fl.toLocalFile())
        self.d = fl.toLocalFile()
       
        if l == "":
            print()
        else:
            self.ui.label.setText(fl.toLocalFile())
            f = open(self.d, "rb")
            buf = f.read(44)
            a = struct.unpack("4si4s4sihhiihh4si", buf)
            nchannels = a[6]              #распаковали
            if nchannels == 1:
                print("У вас и так моно файл")
                self.ui.action_4.setEnabled(False)
                return self.d
            else:
                self.ui.action_5.setEnabled(False)

    
    
    def build_graph(self):        
        def format_time(x, pos=None):       #return self.func(x, pos)
            progress = int(x / float(nframes) * time)
            mins, secs = divmod(progress, 60)
            hours, mins = divmod(mins, 60)
            out = "%d:%02d" % (mins, secs)
            if hours > 0:
                out = "%d:" % hours
            return out

        f = open(self.d, "rb")
        buf = f.read(44)
        a = struct.unpack("4si4s4sihhiihh4si", buf)  #распаковали
        nchannels = a[6]
        framerate = a[7]
        nbytessample = a[9]
        data_area = a[12]
        nframes = data_area // nbytessample
        arr1 = [] 
        while True:
            buf = f.read(4)
            if not buf:
                break
            c = struct.unpack("i", buf)[0]
            arr1.append(c)
        
        time = nframes / framerate
        plt.figure(1, figsize=(10, 5))
        for n in range(nchannels):
            if nchannels == 1:
                axes = plt.subplot(111, facecolor='k')
                axes.plot(arr1, "g")
                plt.grid(True, color="w")
                axes.xaxis.set_major_formatter(ticker.FuncFormatter(format_time))
            else:
                axes = plt.subplot(2, 1, n+1, facecolor='k')
                axes.plot(arr1, "g")
                plt.grid(True, color="w")
                axes.xaxis.set_major_formatter(ticker.FuncFormatter(format_time))
            

        # for n in range(nchannels):
        #     y = arr1
        #     x = [i for i in range(0, len(arr1))]
        #     axes = plt.plot(x, y, 'g')
        #     axes.patch.set_facecolor('black')
        #     # axes.plot(arr1, "g")
        #     # axes.xaxis.set_major_formatter (ticker.FuncFormatter(format_time))
        #     plt.grid(color='black', linestyle=':', linewidth=0.5)
        #     # axes.xaxis.set_major_formatter(ticker.FuncFormatter(format_time))


        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        im = Image.open(buf)
        qimage = ImageQt(im)
                    
        self.ui.label.setText("")
        pixmap = QtGui.QPixmap.fromImage(qimage)
        self.ui.label.setPixmap(pixmap)
        buf.close() 

    def clear(self):
        self.ui.label.setText("")
        pixmap = QtGui.QPixmap()
        self.ui.label.setPixmap(pixmap)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())    



