import PyQt5.QtWidgets
import pyqtgraph as pg
import sys

app = PyQt5.QtWidgets.QApplication(sys.argv)
widget = PyQt5.QtWidgets.QWidget()
graphWidget = pg.PlotWidget()
graphWidget.setBackground('w')
graphWidget.setLabel('left', '<span style=\"font-size:20px\">Amplitude')
graphWidget.setLabel('bottom', '<span style=\"font-size:20px\">Time')
pen = pg.mkPen(color=(108, 140, 245))
graphWidget.plot([1,2,3,4,5])  ## setting pen=None disables line drawing
graphWidget.show()
graphWidget.show()
app.exec()