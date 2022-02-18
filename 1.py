import sys  # sys нужен для передачи argv в QApplication
import obspy
from PyQt5 import QtWidgets, Qt
import matplotlib.pyplot as plt
import pyqtgraph as pg
from obspy.io.segy.segy import _read_segy
from obspy.io.segy.segy import iread_segy
from obspy.core.util import get_example_file
from segpy.reader import create_reader
from segpy.writer import write_segy
import numpy as np
from PyQt5.QtWidgets import QFileDialog
import segyio
from segyio import SegyFile
import tensorflow as tf
import design

matrixIn = []
matrixOut = []


class Before(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.graphWidget.setBackground('w')
        self.graphWidget.setLabel('left', '<span style=\"font-size:20px\">Amplitude')
        self.graphWidget.setLabel('bottom', '<span style=\"font-size:20px\">Time')
        pen = pg.mkPen(color=(108, 140, 245))
        self.graphWidget.plot(matrixIn[0], pen=pen)  ## setting pen=None disables line drawing


class After(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.graphWidget.setBackground('w')
        self.graphWidget.setLabel('left', '<span style=\"font-size:20px\">Amplitude')
        self.graphWidget.setLabel('bottom', '<span style=\"font-size:20px\">Time')
        pen = pg.mkPen(color=(108, 140, 245))
        self.graphWidget.plot(matrixOut[0], pen=pen)  ## setting pen=None disables line drawing


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    count = 0

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        #layout = Qt.QVBoxLayout(self)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.ButtonLoad.clicked.connect(self.button_load)
        self.ButtonBefore.clicked.connect(self.button_before)
        self.ButtonAfter.clicked.connect(self.button_after)

        #self.view = view = pg.PlotWidget()
        #self.curve = view.plot()
        #layout.addWidget(self.view)

    def get_seis(self, in_file, out_file):
        seis = segyio.open(in_file, ignore_geometry=True)
        model = tf.keras.models.load_model("new_СDNN.hdf5")
        trace = []
        for i in range(len(seis.trace)):
            trace.append(seis.trace[i])

        matrix = np.stack(trace, axis=0)

        new_matrix = np.ndarray(matrix.shape)

        for i in range(len(matrix[:, 0])):
            trace = matrix[i, :]
            trace = np.reshape(trace, trace.shape + (1,))
            trace = trace.T
            trace = np.reshape(trace, trace.shape + (1,))
            result = model.predict(x=trace, verbose=1)
            new_matrix[i, :] = result[0, :].flatten()

        a, b = matrix.shape
        spec = segyio.spec()
        spec.sorting = 1
        spec.format = 5
        spec.tracecount = a
        spec.samples = np.arange(1, b + 1, 1)
        spec.iline = 1
        spec.xline = 1

        seg2 = segyio.create(out_file, spec)

        for i in range(a):
            seg2.trace[i] = np.float32(new_matrix[i, :])

        seg2.header = seis.header
        seg2.flush()

        return seg2

    def get_matrix_from_segy(self, seis):
        self.Sx = []
        self.Sy = []
        self.Rx = []
        self.Ry = []
        self.OFF = []
        self.FFID = []
        self.SDatum = []
        self.RDatum = []
        trace = []
        for i in range(len(seis.trace)):
            trace.append(seis.trace[i])
            self.Sx.append(seis.header[i][segyio.TraceField.SourceX])
            self.Sy.append(seis.header[i][segyio.TraceField.SourceY])
            self.Rx.append(seis.header[i][segyio.TraceField.GroupX])
            self.Ry.append(seis.header[i][segyio.TraceField.GroupY])
            self.OFF.append(seis.header[i][segyio.TraceField.offset])
            self.FFID.append(seis.header[i][segyio.TraceField.FieldRecord])
            self.SDatum.append(seis.header[i][segyio.TraceField.SourceDatumElevation])
            self.RDatum.append(seis.header[i][segyio.TraceField.ReceiverDatumElevation])
        matrix = np.stack(trace, axis=0)
        return matrix

    def button_load(self):
        #self.listWidget.clear()  # На случай, если в списке уже есть элементы
        #directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        SEG_Y = QtWidgets.QFileDialog.getOpenFileName()[0]
        seis = segyio.open(SEG_Y, ignore_geometry=True)
        #print(type(seis))

        # self.Sx = []
        # self.Sy = []
        # self.Rx = []
        # self.Ry = []
        # self.OFF = []
        # self.FFID = []
        # self.SDatum = []
        # self.RDatum = []
        # trace = []
        # for i in range(len(seis.trace)):
        #     trace.append(seis.trace[i])
        #     self.Sx.append(seis.header[i][segyio.TraceField.SourceX])
        #     self.Sy.append(seis.header[i][segyio.TraceField.SourceY])
        #     self.Rx.append(seis.header[i][segyio.TraceField.GroupX])
        #     self.Ry.append(seis.header[i][segyio.TraceField.GroupY])
        #     self.OFF.append(seis.header[i][segyio.TraceField.offset])
        #     self.FFID.append(seis.header[i][segyio.TraceField.FieldRecord])
        #     self.SDatum.append(seis.header[i][segyio.TraceField.SourceDatumElevation])
        #     self.RDatum.append(seis.header[i][segyio.TraceField.ReceiverDatumElevation])
        # self.matrixI = np.stack(trace, axis=0)

        self.matrixIn = self.get_matrix_from_segy(seis)
        #print((self.matrixIn).dtype())
        out_file = "out_file" + str(self.count) + ".segy"
        #print(out_file)
        self.matrixOut = self.get_matrix_from_segy(self.get_seis(str(SEG_Y), str(out_file)))
        self.count += 1

    def button_before(self):
        #self.curve.setData(self.matrix.T[0])
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground('w')
        self.graphWidget.setLabel('left', '<span style=\"font-size:20px\">Amplitude')
        self.graphWidget.setLabel('bottom', '<span style=\"font-size:20px\">Time, ms')
        pen = pg.mkPen(width=3, color=(108, 140, 245))
        self.graphWidget.plot(self.matrixIn[0], pen=pen)  ## setting pen=None disables line drawing
        self.graphWidget.show()

    def button_after(self):
        self.graphWidget = pg.PlotWidget()
        #self.setCentralWidget(self.graphWidget)
        self.graphWidget.setBackground('w')
        self.graphWidget.setLabel('left', '<span style=\"font-size:20px\">Amplitude')
        self.graphWidget.setLabel('bottom', '<span style=\"font-size:20px\">Time, ms')
        pen = pg.mkPen(width=3, color=(108, 140, 245))
        self.graphWidget.plot(self.matrixOut[0], pen=pen)  # setting pen=None disables line drawing
        self.graphWidget.show()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()