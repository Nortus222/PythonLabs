from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.resize(629, 459)

        self.centralwidget = QtWidgets.QWidget(MainWindow)


        self.label_Initials = QtWidgets.QLabel(self.centralwidget)
        self.label_Initials.setGeometry(QtCore.QRect(30, 30, 221, 101))


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 150, 71, 31))


        self.label_Result = QtWidgets.QLabel(self.centralwidget)
        self.label_Result.setGeometry(QtCore.QRect(100, 160, 60, 16))


        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 210, 141, 16))


        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(30, 230, 151, 20))
        self.radioButton.setObjectName("random")
        self.radioButton.setChecked(True)
        self.radioButton.toggled.connect(lambda: self.radioButtonClicked(self.radioButton))


        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(210, 230, 151, 20))
        self.radioButton_2.setObjectName("hands")
        self.radioButton_2.toggled.connect(lambda: self.radioButtonClicked(self.radioButton_2))


        self.labe_InputMessage = QtWidgets.QLabel(self.centralwidget)
        self.labe_InputMessage.setGeometry(QtCore.QRect(200, 370, 201, 16))
        self.labe_InputMessage.setVisible(False)


        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(400, 10, 201, 321))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(5)


        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 181, 31))

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(80, 40, 21, 21))


        self.horizontalSlider = QtWidgets.QSlider(self.frame)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 60, 160, 22))
        self.horizontalSlider.setMaximum(20)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("a")
        self.horizontalSlider.valueChanged.connect(lambda: self.sliderValueChanged(self.horizontalSlider))


        self.label_AOut = QtWidgets.QLabel(self.frame)
        self.label_AOut.setGeometry(QtCore.QRect(80, 90, 60, 16))
        self.label_AOut.setText(str(self.horizontalSlider.value()))


        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(80, 120, 21, 21))


        self.horizontalSlider_2 = QtWidgets.QSlider(self.frame)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(10, 150, 160, 22))
        self.horizontalSlider_2.setMaximum(20)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("b")
        self.horizontalSlider_2.valueChanged.connect(lambda: self.sliderValueChanged(self.horizontalSlider_2))


        self.label_BOut = QtWidgets.QLabel(self.frame)
        self.label_BOut.setGeometry(QtCore.QRect(80, 180, 60, 16))
        self.label_BOut.setText(str(self.horizontalSlider_2.value()))


        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(80, 210, 21, 21))


        self.horizontalSlider_3 = QtWidgets.QSlider(self.frame)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(10, 240, 160, 22))
        self.horizontalSlider_3.setMaximum(20)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("c")
        self.horizontalSlider_3.valueChanged.connect(lambda: self.sliderValueChanged(self.horizontalSlider_3))


        self.label_COut = QtWidgets.QLabel(self.frame)
        self.label_COut.setGeometry(QtCore.QRect(80, 270, 60, 16))
        self.label_COut.setText(str(self.horizontalSlider_3.value()))


        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(200, 260, 161, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setVisible(False)


        self.lineEdit_A = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_A.setGeometry(QtCore.QRect(40, 10, 113, 21))




        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 21, 21))


        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(10, 40, 21, 21))


        self.lineEdit_B = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_B.setGeometry(QtCore.QRect(40, 40, 113, 21))


        self.lineEdit_C = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_C.setGeometry(QtCore.QRect(40, 70, 113, 21))


        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 21, 21))


        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(30, 260, 141, 121))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)


        self.spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox.setGeometry(QtCore.QRect(10, 40, 48, 24))


        self.spinBox_2 = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox_2.setGeometry(QtCore.QRect(10, 90, 48, 24))


        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 60, 16))


        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(10, 0, 121, 21))


        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(10, 70, 60, 16))


        MainWindow.setCentralWidget(self.centralwidget)


        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lab8_Sherstiuk"))
        self.label_Initials.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Шерстюк Ігор Юрійович</span></p><p><span style=\" font-size:18pt;\">Група: ІВ-92</span></p><p><span style=\" font-size:18pt;\">Номер: 9231</span></p><p><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Результат:"))
        self.label_Result.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "Елементи множин"))
        self.radioButton.setText(_translate("MainWindow", "Задання випадково"))
        self.radioButton_2.setText(_translate("MainWindow", "Задання вручну"))
        self.labe_InputMessage.setText(_translate("MainWindow", "Напишіть цифри через кому"))
        self.label_2.setText(_translate("MainWindow", "Кількість єлементів A,B,C"))
        self.label_3.setText(_translate("MainWindow", "A"))

        self.label_4.setText(_translate("MainWindow", "B"))

        self.label_5.setText(_translate("MainWindow", "C"))

        self.label_7.setText(_translate("MainWindow", "A"))
        self.label_8.setText(_translate("MainWindow", "B"))
        self.label_9.setText(_translate("MainWindow", "C"))
        self.label_10.setText(_translate("MainWindow", "Початок"))
        self.label_11.setText(_translate("MainWindow", "Визначте діапазон"))
        self.label_12.setText(_translate("MainWindow", "Кінець"))

    def radioButtonClicked(self, b):
        if b.isChecked():
            if b.objectName() == "random":
                self.frame_2.setVisible(False)
                self.labe_InputMessage.setVisible(False)
                self.frame_3.setVisible(True)
            if b.objectName() == "hands":
                self.frame_3.setVisible(False)
                self.frame_2.setVisible(True)
                self.labe_InputMessage.setVisible(True)

    def sliderValueChanged(self, s):
        if s.objectName() == "a":
            self.label_AOut.setText(str(s.value()))
        elif s.objectName() == "b":
            self.label_BOut.setText(str(s.value()))
        elif s.objectName() == "c":
            self.label_COut.setText(str(s.value()))


def window():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    win = Ui_MainWindow()
    win.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

window()
