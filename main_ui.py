# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(523, 389)
        MainWindow.setMinimumSize(QtCore.QSize(523, 389))
        MainWindow.setStyleSheet("* {\n"
"background-color:#D8E6E7;\n"
"font-family:Helvetica Neue;\n"
"border-radius: 8px\n"
"/*font-color:#F8FAFF;*/\n"
"}\n"
"\n"
"QGroupBox, QFrame {\n"
"    background:#9DC3C1;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#77AAAD;\n"
"    color:#3E4348 ;\n"
"    border-radius: 3px\n"
"\n"
"}\n"
"QPushButton:pressed,QPushButton:checked{\n"
"    background-color:#ABD0CE;\n"
"    border-radius: 3px\n"
"\n"
"}\n"
"\n"
"QComboBox {\n"
"background:#6E7783;\n"
"border-radius: 8px;\n"
"border: 1px solid #6E7783;\n"
"color:white;\n"
"combobox-popup: 0;\n"
"padding: 1px 0px 1px 3px;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"border-radius: 8px;\n"
"background-color: #D8E6E7;\n"
"color:black;\n"
"}\n"
"QLabel,QPushButton {\n"
"background-color:#9DC3C1;\n"
"color: #3E4348;\n"
"}\n"
"#header_label{\n"
"color: #6E7783;\n"
"font-family:Futura;\n"
"background-color:#D8E6E7\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setContentsMargins(5, 12, 5, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.header_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_label.sizePolicy().hasHeightForWidth())
        self.header_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.header_label.setFont(font)
        self.header_label.setAlignment(QtCore.Qt.AlignCenter)
        self.header_label.setObjectName("header_label")
        self.horizontalLayout_2.addWidget(self.header_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.UpDown_btn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UpDown_btn.sizePolicy().hasHeightForWidth())
        self.UpDown_btn.setSizePolicy(sizePolicy)
        self.UpDown_btn.setCheckable(True)
        self.UpDown_btn.setChecked(False)
        self.UpDown_btn.setObjectName("UpDown_btn")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.UpDown_btn)
        self.verticalLayout.addWidget(self.UpDown_btn)
        self.DownUp_btn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DownUp_btn.sizePolicy().hasHeightForWidth())
        self.DownUp_btn.setSizePolicy(sizePolicy)
        self.DownUp_btn.setCheckable(True)
        self.DownUp_btn.setChecked(False)
        self.DownUp_btn.setObjectName("DownUp_btn")
        self.buttonGroup.addButton(self.DownUp_btn)
        self.verticalLayout.addWidget(self.DownUp_btn)
        self.UpRight_btn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UpRight_btn.sizePolicy().hasHeightForWidth())
        self.UpRight_btn.setSizePolicy(sizePolicy)
        self.UpRight_btn.setCheckable(True)
        self.UpRight_btn.setChecked(False)
        self.UpRight_btn.setObjectName("UpRight_btn")
        self.buttonGroup.addButton(self.UpRight_btn)
        self.verticalLayout.addWidget(self.UpRight_btn)
        self.DownRight_btn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DownRight_btn.sizePolicy().hasHeightForWidth())
        self.DownRight_btn.setSizePolicy(sizePolicy)
        self.DownRight_btn.setCheckable(True)
        self.DownRight_btn.setChecked(False)
        self.DownRight_btn.setObjectName("DownRight_btn")
        self.buttonGroup.addButton(self.DownRight_btn)
        self.verticalLayout.addWidget(self.DownRight_btn)
        self.UpLeft_btn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UpLeft_btn.sizePolicy().hasHeightForWidth())
        self.UpLeft_btn.setSizePolicy(sizePolicy)
        self.UpLeft_btn.setCheckable(True)
        self.UpLeft_btn.setChecked(False)
        self.UpLeft_btn.setObjectName("UpLeft_btn")
        self.buttonGroup.addButton(self.UpLeft_btn)
        self.verticalLayout.addWidget(self.UpLeft_btn)
        self.DownLeft_btn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DownLeft_btn.sizePolicy().hasHeightForWidth())
        self.DownLeft_btn.setSizePolicy(sizePolicy)
        self.DownLeft_btn.setCheckable(True)
        self.DownLeft_btn.setChecked(False)
        self.DownLeft_btn.setObjectName("DownLeft_btn")
        self.buttonGroup.addButton(self.DownLeft_btn)
        self.verticalLayout.addWidget(self.DownLeft_btn)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.actionCombo = QtWidgets.QComboBox(self.groupBox_2)
        self.actionCombo.setObjectName("actionCombo")
        self.actionCombo.addItem("")
        self.actionCombo.addItem("")
        self.actionCombo.addItem("")
        self.actionCombo.addItem("")
        self.actionCombo.addItem("")
        self.actionCombo.addItem("")
        self.actionCombo.addItem("")
        self.verticalLayout_2.addWidget(self.actionCombo)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout_2.addWidget(self.comboBox_3)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 6)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.deviceCombo = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deviceCombo.sizePolicy().hasHeightForWidth())
        self.deviceCombo.setSizePolicy(sizePolicy)
        self.deviceCombo.setFrame(False)
        self.deviceCombo.setObjectName("deviceCombo")
        self.deviceCombo.addItem("")
        self.deviceCombo.addItem("")
        self.verticalLayout_3.addWidget(self.deviceCombo)
        self.enableCheck = QtWidgets.QCheckBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enableCheck.sizePolicy().hasHeightForWidth())
        self.enableCheck.setSizePolicy(sizePolicy)
        self.enableCheck.setObjectName("enableCheck")
        self.verticalLayout_3.addWidget(self.enableCheck)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.trackCheck = QtWidgets.QCheckBox(self.frame)
        self.trackCheck.setObjectName("trackCheck")
        self.verticalLayout_6.addWidget(self.trackCheck)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.mirrorCheck = QtWidgets.QCheckBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mirrorCheck.sizePolicy().hasHeightForWidth())
        self.mirrorCheck.setSizePolicy(sizePolicy)
        self.mirrorCheck.setObjectName("mirrorCheck")
        self.verticalLayout_7.addWidget(self.mirrorCheck)
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        self.gridLayout.addLayout(self.verticalLayout_6, 3, 0, 1, 1)
        self.draw_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.draw_btn.sizePolicy().hasHeightForWidth())
        self.draw_btn.setSizePolicy(sizePolicy)
        self.draw_btn.setObjectName("draw_btn")
        self.gridLayout.addWidget(self.draw_btn, 4, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 3)
        self.gridLayout.setRowStretch(2, 8)
        self.gridLayout.setRowStretch(3, 3)
        self.gridLayout.setRowStretch(4, 1)
        self.horizontalLayout.addWidget(self.frame)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header_label.setText(_translate("MainWindow", "Choose a gesture and assign action"))
        self.UpDown_btn.setText(_translate("MainWindow", "UpDown"))
        self.DownUp_btn.setText(_translate("MainWindow", "DownUp"))
        self.UpRight_btn.setText(_translate("MainWindow", "LeftRight"))
        self.DownRight_btn.setText(_translate("MainWindow", "RightLeft"))
        self.UpLeft_btn.setText(_translate("MainWindow", "Cross"))
        self.DownLeft_btn.setText(_translate("MainWindow", "Circle"))
        self.label_2.setText(_translate("MainWindow", "Select Action"))
        self.actionCombo.setItemText(0, _translate("MainWindow", "None"))
        self.actionCombo.setItemText(1, _translate("MainWindow", "Maximise Window"))
        self.actionCombo.setItemText(2, _translate("MainWindow", "Minimise Window"))
        self.actionCombo.setItemText(3, _translate("MainWindow", "Go Left"))
        self.actionCombo.setItemText(4, _translate("MainWindow", "Go right"))
        self.actionCombo.setItemText(5, _translate("MainWindow", "Esc"))
        self.actionCombo.setItemText(6, _translate("MainWindow", "Play PPT"))
        self.label_4.setText(_translate("MainWindow", "or"))
        self.label_3.setText(_translate("MainWindow", "Using Shortcut"))
        self.label_5.setText(_translate("MainWindow", "Settings"))
        self.deviceCombo.setItemText(0, _translate("MainWindow", "Mouse"))
        self.deviceCombo.setItemText(1, _translate("MainWindow", "Laser Pointer"))
        self.enableCheck.setText(_translate("MainWindow", "Enable"))
        self.trackCheck.setText(_translate("MainWindow", "Real-time"))
        self.mirrorCheck.setText(_translate("MainWindow", "Mirror"))
        self.label.setText(_translate("MainWindow", "Click it if you wanna \n"
" operate facing camera"))
        self.draw_btn.setText(_translate("MainWindow", "Testing"))
