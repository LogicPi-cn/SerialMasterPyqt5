# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\06LogicPi\04Git_Projects\SerialMaster\drawCurve.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(820, 518)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/曲线.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_Curve = QtWidgets.QGroupBox(Dialog)
        self.groupBox_Curve.setMinimumSize(QtCore.QSize(640, 480))
        self.groupBox_Curve.setObjectName("groupBox_Curve")
        self.gridLayout_2.addWidget(self.groupBox_Curve, 0, 2, 8, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 7, 0, 1, 1)
        self.label_Status = QtWidgets.QLabel(Dialog)
        self.label_Status.setText("")
        self.label_Status.setObjectName("label_Status")
        self.gridLayout_2.addWidget(self.label_Status, 8, 0, 1, 3)
        self.pushButton_Start = QtWidgets.QPushButton(Dialog)
        self.pushButton_Start.setObjectName("pushButton_Start")
        self.gridLayout_2.addWidget(self.pushButton_Start, 0, 0, 1, 1)
        self.pushButton_Stop = QtWidgets.QPushButton(Dialog)
        self.pushButton_Stop.setObjectName("pushButton_Stop")
        self.gridLayout_2.addWidget(self.pushButton_Stop, 0, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_X_Len = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_X_Len.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_X_Len.setObjectName("lineEdit_X_Len")
        self.gridLayout_4.addWidget(self.lineEdit_X_Len, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 1, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setEnabled(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_DataFormat10 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_DataFormat10.setChecked(True)
        self.radioButton_DataFormat10.setObjectName("radioButton_DataFormat10")
        self.gridLayout.addWidget(self.radioButton_DataFormat10, 0, 0, 1, 1)
        self.radioButton_DataFormat16 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_DataFormat16.setObjectName("radioButton_DataFormat16")
        self.gridLayout.addWidget(self.radioButton_DataFormat16, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 2)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setEnabled(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_5.addWidget(self.comboBox, 0, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_5.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_5.addWidget(self.comboBox_3, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_4, 3, 0, 1, 2)
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setEnabled(False)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineEdit_AxisMin = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_AxisMin.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_AxisMin.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_AxisMin.setObjectName("lineEdit_AxisMin")
        self.gridLayout_6.addWidget(self.lineEdit_AxisMin, 1, 1, 1, 1)
        self.radioButton_AxisAuto = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_AxisAuto.setChecked(True)
        self.radioButton_AxisAuto.setObjectName("radioButton_AxisAuto")
        self.gridLayout_6.addWidget(self.radioButton_AxisAuto, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 1, 0, 1, 1)
        self.radioButton_AxisManual = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_AxisManual.setObjectName("radioButton_AxisManual")
        self.gridLayout_6.addWidget(self.radioButton_AxisManual, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_AxisMax = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_AxisMax.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_AxisMax.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_AxisMax.setObjectName("lineEdit_AxisMax")
        self.gridLayout_6.addWidget(self.lineEdit_AxisMax, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_5, 5, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "实时数据显示"))
        self.groupBox_Curve.setTitle(_translate("Dialog", "曲线"))
        self.pushButton_Start.setText(_translate("Dialog", "开始"))
        self.pushButton_Stop.setText(_translate("Dialog", "停止"))
        self.groupBox_3.setTitle(_translate("Dialog", "显示长度"))
        self.lineEdit_X_Len.setText(_translate("Dialog", "100"))
        self.groupBox.setTitle(_translate("Dialog", "数据格式"))
        self.radioButton_DataFormat10.setText(_translate("Dialog", "十进制"))
        self.radioButton_DataFormat16.setText(_translate("Dialog", "十六进制"))
        self.groupBox_4.setTitle(_translate("Dialog", "线条类型"))
        self.label_4.setText(_translate("Dialog", "点颜色"))
        self.label_3.setText(_translate("Dialog", "线条颜色"))
        self.label_5.setText(_translate("Dialog", "柱状颜色"))
        self.groupBox_5.setTitle(_translate("Dialog", "坐标范围"))
        self.radioButton_AxisAuto.setText(_translate("Dialog", "自动"))
        self.label.setText(_translate("Dialog", "Min:"))
        self.radioButton_AxisManual.setText(_translate("Dialog", "手动"))
        self.label_2.setText(_translate("Dialog", "Max:"))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

