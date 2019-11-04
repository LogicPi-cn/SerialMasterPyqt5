# -*- coding: utf-8 -*-

"""
Module implementing dialogDrawCurve.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Ui_drawCurve import Ui_Dialog

from serial_ctrl import *
from SettingCtrl import *

import numpy as np
import random

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
import matplotlib
import matplotlib.cbook as cbook

class ReceiveThread(QThread):
    finishSignal = pyqtSignal(bytes)
    def __init__(self, parent=None):
        super(ReceiveThread, self).__init__(parent)

    def run(self):

        global g_rec_run, g_serial

        while g_rec_run:
            data = None
            try:
                data = g_serial.read_all()
            except Exception():
                pass
            if data is not  None:
                self.finishSignal.emit(data)

class Figure_Canvas(FigureCanvas):
    def __init__(self,parent=None, dpi=100):
        self.fig=Figure(dpi=100)
        super(Figure_Canvas,self).__init__(self.fig)
        self.ax=self.fig.add_subplot(111)

class dialogDrawCurve(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(dialogDrawCurve, self).__init__(parent)
        self.setupUi(self)

        # 变量控制
        self.params = SettingCtrl()
        self.load_params()

        # 参数传递
        self.port = ""
        self.bps = 9600

        # y轴范围
        if self.radioButton_AxisAuto.isChecked():
            self.axis_y_auto = True
        if self.radioButton_AxisManual.isChecked():
            self.axis_y_auto = False

        # 10/16 进制
        if self.radioButton_DataFormat10.isChecked():
            self.data_as_hex = False
        if self.radioButton_DataFormat16.isChecked():
            self.data_as_hex = True
        
        # 曲线窗口初始化
        self.DrawCurveInit()

    def load_params(self):
        """
        参数读取
        """
        try:
            self.x_len = int(self.params.load("curve", "x_len"))
        except Exception:
            self.x_len = 100
            self.params.save("curve", "x_len", "100")

        self.lineEdit_X_Len.setText(str(self.x_len))

    def DrawCurveInit(self):
        """
        画布初始化
        """

        self.x01 = np.arange(0, self.x_len)
        self.y01 = np.zeros(self.x_len)

        self.LineFigure01 = Figure_Canvas()
        self.LineFigureLayout01 = QGridLayout(self.groupBox_Curve)
        self.LineFigureLayout01.addWidget(self.LineFigure01)
        # self.LineFigure01.ax.set_xlim(0, self.x_len)
        # self.LineFigure01.ax.set_ylim(emit=True, auto=True)
        self.line01 = Line2D(self.x01, self.y01)
        self.LineFigure01.ax.add_line(self.line01)

    def UpdateArray(self, y, lastData):
        """
        更新Array函数, rolling模式
        """
        result = y
        result[:-1] = result[1:]
        result[-1] = lastData
        return result

    def UpdateCurve(self, raw_data):
        """
        刷新数据
        """
        # 如果没有数据，就不要麻烦下面的操作了
        if len(raw_data) == 0:
            return

        try:
            in_data = float(raw_data)
        except Exception:
            in_data = 0

        self.UpdateArray(self.y01, in_data)
        self.line01.set_ydata(self.y01)

        self.LineFigure01.ax.relim()
        self.LineFigure01.ax.autoscale_view()
        self.LineFigure01.draw()
    
    @pyqtSlot()
    def on_pushButton_Start_clicked(self):
        """
        开始按钮
        """
        global g_serial, g_rec_run, g_port_is_open

        if g_port_is_open:

            # 关闭接收线程
            g_rec_run = False
            # 全部变量关闭
            g_port_is_open = False

            close_port(g_serial)
            self.label_Status.setText("关闭串口")
            self.pushButton_Start.setText("打开")

        else:

            g_serial = open_port(self.port, self.bps)

            if g_serial is not None:

                g_port_is_open = True

                self.label_Status.setText("打开串口成功")
                self.pushButton_Start.setText("关闭")

                # 接收线程启动
                self.t_rec = ReceiveThread()
                self.t_rec.finishSignal.connect(self.UpdateCurve)
                self.t_rec.start()
                g_rec_run = True

            else:
                self.label_Status.setText("打开串口失败")
    
    @pyqtSlot(bool)
    def on_radioButton_DataFormat10_toggled(self, checked):
        """
        十进制
        """
        self.data_as_hex = False
    
    @pyqtSlot(bool)
    def on_radioButton_DataFormat16_toggled(self, checked):
        """
        16进制
        """
        self.data_as_hex = True
        
    @pyqtSlot(bool)
    def on_radioButton_AxisAuto_toggled(self, checked):
        """
        自动范围
        """
        if checked:
            self.axis_y_auto = True
            self.label_Status.setText("自动范围")
    
    @pyqtSlot(bool)
    def on_radioButton_AxisManual_toggled(self, checked):
        """
        手动范围
        """
        if checked:
            self.axis_y_auto = False
            self.label_Status.setText("手动范围")
    
    @pyqtSlot(str)
    def on_lineEdit_X_Len_textChanged(self, p0):
        """
        X轴长度
        """
        try:
            self.x_len = int(p0)
        except Exception:
            self.x_len = 100
        
        self.params.save("curve", "x_len", str(self.x_len))
        self.label_Status.setText("请关闭窗口后重新打开")