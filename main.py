from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph.exporters

class Ui_Form(object):
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(906, 558)
        Form.setStyleSheet("background-color:rgb(2,10,40);")
        self.i =1
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(260, 0, 651, 531))
        self.stackedWidget.setStyleSheet("background-color:rgb(225,240,240);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setGeometry(QtCore.QRect(160, 190, 281, 181))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(97, 130, 61, 21))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/img/resistor.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(80, 30, 121, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/img/bat.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(12, 42, 68, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setGeometry(QtCore.QRect(200, 42, 68, 16))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame_2)
        self.line_3.setGeometry(QtCore.QRect(12, 50, 3, 93))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame_2)
        self.line_4.setGeometry(QtCore.QRect(266, 50, 3, 93))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.frame_2)
        self.line_5.setGeometry(QtCore.QRect(158, 140, 109, 3))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(6)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.frame_2)
        self.line_6.setGeometry(QtCore.QRect(13, 140, 84, 3))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(8)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(30, 80, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:blue")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.lbl_current = QtWidgets.QLabel(self.frame_2)
        self.lbl_current.setGeometry(QtCore.QRect(150, 80, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_current.setFont(font)
        self.lbl_current.setStyleSheet("color:blue")
        self.lbl_current.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_current.setObjectName("lbl_current")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(210, 37, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background:transparent;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(200, 129, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background:transparent;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(30, 128, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background:transparent;")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(30, 37, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background:transparent;")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.line_7 = QtWidgets.QFrame(self.page)
        self.line_7.setGeometry(QtCore.QRect(290, 130, 3, 93))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.page)
        self.line_8.setGeometry(QtCore.QRect(290, 340, 3, 93))
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(3)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.page)
        self.line_9.setGeometry(QtCore.QRect(290, 430, 84, 3))
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setLineWidth(8)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setObjectName("line_9")
        self.line_19 = QtWidgets.QFrame(self.page)
        self.line_19.setGeometry(QtCore.QRect(290, 130, 84, 3))
        self.line_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_19.setLineWidth(8)
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setObjectName("line_19")
        self.inp_volt = QtWidgets.QLineEdit(self.page)
        self.inp_volt.setGeometry(QtCore.QRect(370, 120, 113, 22))
        self.inp_volt.setAlignment(QtCore.Qt.AlignCenter)
        self.inp_volt.setObjectName("inp_volt")
        self.inp_ohm = QtWidgets.QLineEdit(self.page)
        self.inp_ohm.setGeometry(QtCore.QRect(370, 420, 113, 22))
        self.inp_ohm.setAlignment(QtCore.Qt.AlignCenter)
        self.inp_ohm.setObjectName("inp_ohm")
        self.btn_calc = QtWidgets.QPushButton(self.page)
        self.btn_calc.setGeometry(QtCore.QRect(180, 470, 241, 51))
        self.btn_calc.setStyleSheet("QPushButton{\n"
"background-color: rgba(175,80,180,200);\n"
"color:white;\n"
"border:1px solid rgb(200,200,200);\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"    font: 9pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:Pressed{\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        self.btn_calc.setObjectName("btn_calc")
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(390, 70, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:blue")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(370, 380, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:blue")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_14 = QtWidgets.QLabel(self.page)
        self.label_14.setGeometry(QtCore.QRect(120, 30, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background:transparent;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.tableWidget = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 262, 402))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        self.graph = PlotWidget(self.page_2)
        self.graph.setGeometry(QtCore.QRect(280, 20, 361, 401))
        self.graph.setObjectName("graph")
        self.btn_plot = QtWidgets.QPushButton(self.page_2)
        self.btn_plot.setGeometry(QtCore.QRect(10, 460, 261, 51))
        self.btn_plot.setStyleSheet("QPushButton{\n"
"background-color: rgba(175,80,180,200);\n"
"color:white;\n"
"border:1px solid rgb(200,200,200);\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"    font: 9pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:Pressed{\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        self.btn_plot.setObjectName("btn_plot")
        self.btn_plot_2 = QtWidgets.QPushButton(self.page_2)
        self.btn_plot_2.setGeometry(QtCore.QRect(280, 460, 351, 51))
        self.btn_plot_2.setStyleSheet("QPushButton{\n"
"background-color: rgba(175,80,180,200);\n"
"color:white;\n"
"border:1px solid rgb(200,200,200);\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"    font: 9pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:Pressed{\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        self.btn_plot_2.setObjectName("btn_plot_2")
        self.stackedWidget.addWidget(self.page_2)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 530, 911, 31))
        self.frame.setStyleSheet("background-color:white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 190, 241, 51))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgba(75,80,180,200);\n"
"color:white;\n"
"border:1px solid rgb(200,200,200);\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"    font: 9pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:Pressed{\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 250, 241, 51))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: rgba(75,80,180,200);\n"
"color:white;\n"
"border:1px solid rgb(200,200,200);\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"    font: 9pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:Pressed{\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 10, 100, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/img/ic.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:blue")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QtCore.QRect(700, -10, 221, 41))
        font2 = QtGui.QFont()
        font2.setPointSize(9)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color:blue")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ohm's Law Visualizer"))
        self.label_9.setText(_translate("Form", "I (current) :"))
        self.lbl_current.setText(_translate("Form", "0 mA"))
        self.label_10.setText(_translate("Form", ">"))
        self.label_11.setText(_translate("Form", "<"))
        self.label_12.setText(_translate("Form", "<"))
        self.label_13.setText(_translate("Form", ">"))
        self.btn_calc.setText(_translate("Form", "Calculate"))
        self.label_7.setText(_translate("Form", "V (volt)"))
        self.label_8.setText(_translate("Form", "Ω (ohm)"))
        self.label_14.setText(_translate("Form", "Equation , V = IR"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "V(volts)"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "I(mA)"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("Form", "6"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("Form", "7"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("Form", "8"))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("Form", "9"))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("Form", "10"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.btn_plot.setText(_translate("Form", "Plot Data"))
        self.btn_plot_2.setText(_translate("Form", "Save Graph"))
        self.pushButton.setText(_translate("Form", "Ohm\'s Law Visualize"))
        self.pushButton_2.setText(_translate("Form", "Graph Plotting"))
        self.label_2.setText(_translate("Form", "Ohm\'s Law Visualizer"))
        self.btn_plot.clicked.connect(self.graph_plot)
        self.btn_plot_2.clicked.connect(self.save)
        self.btn_calc.clicked.connect(self.calc_current)
        self.label_5.setText("Developed By Sihab Sahariar")
	

    def graph_plot(self):
        self.graph.clear()
        x = []
        y = []
        for row in range (10):
            try:
                x_val = float(self.tableWidget.item(row,0).text())
            except:
                x_val = 0.0
            try:
                y_val = float(self.tableWidget.item(row,1).text())
            except:
                y_val = 0.0
            x.append(x_val)
            y.append(y_val)
        #print(x,y)
        self.graph.plot(x,y)
            	
    def calc_current(self):
        try:
            v = float(self.inp_volt.text())
        except:
            pass
        try:
            r = float(self.inp_ohm.text())
        except:
            pass
        try:
            I = (v/r)*1000
            self.lbl_current.setText(f"{I:.1f} mA")
        except:
            self.error()

    def error(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Data Error")
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok) 
        returnValue = msgBox.exec()
        self.inp_volt.setText("0")
        self.inp_ohm.setText("0")
        self.lbl_current.setText("0 mA")
    def save(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(f"Saved graph as graph_{self.i}.png")
        msgBox.setWindowTitle("Saved")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok) 
        returnValue = msgBox.exec()

        exporter = pyqtgraph.exporters.ImageExporter( self.graph.plotItem )
        exporter.parameters()['width'] = 400   # (note this also affects height parameter)
        exporter.export(f'graph_{self.i}.png') # save to file
        self.i+=1



from pyqtgraph import PlotWidget
import res

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    #ui.graph.plot([1,2,3],[33,45,66])
    Form.show()
    sys.exit(app.exec_())

