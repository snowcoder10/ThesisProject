
# Form implementation generated from reading ui file 'mainwindow.ui' created using QT Creator
#
# Created by: PyQt5 UI code generator 5.13.0
# Kevin Castell. Butson Lab. 7/26/2019
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot

class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(856, 442)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 4, 848, 391))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.patientText = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_2)
        self.patientText.setObjectName("patientText")
        self.verticalLayout.addWidget(self.patientText)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.videoFileName = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.videoFileName.setObjectName("videoFileName")
        self.verticalLayout.addWidget(self.videoFileName)
        self.selectVideoFile = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.selectVideoFile.setObjectName("selectVideoFile")
        self.verticalLayout.addWidget(self.selectVideoFile)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.reportText = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_2)
        self.reportText.setObjectName("reportText")
        self.verticalLayout.addWidget(self.reportText)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.saveLocation = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.saveLocation.setObjectName("saveLocation")
        self.verticalLayout.addWidget(self.saveLocation)
        self.selectSaveLocation = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.selectSaveLocation.setObjectName("selectSaveLocation")
        self.verticalLayout.addWidget(self.selectSaveLocation)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.runButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout_2.addWidget(self.runButton)
        self.importCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.importCheckBox.setObjectName("importCheckBox")
        self.horizontalLayout_2.addWidget(self.importCheckBox)
        self.saveCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.saveCheckBox.setObjectName("saveCheckBox")
        self.horizontalLayout_2.addWidget(self.saveCheckBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 856, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.patientText.textChanged.connect(self.patientTextEntered)
        self.videoFileName.editingFinished.connect(self.videoFileSlot)
        self.selectVideoFile.clicked.connect(self.findVideoFileSlot)
        self.reportText.textChanged.connect(self.reportSlot)
        self.saveLocation.editingFinished.connect(self.saveTextEntered)
        self.selectSaveLocation.clicked.connect(self.findFileSlot)
        self.runButton.clicked.connect(self.runSlot)
        self.importCheckBox.clicked['bool'].connect(self.importToNeoSlot)
        self.saveCheckBox.clicked['bool'].connect(self.saveCheckBoxSlot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Use this GUI for reading settings from a screen recording of a DBS programming session."))
        self.label.setText(_translate("MainWindow", "Patient Info (comma separated). Use non-identifiable information only.\nThis is used if choosing to import to Neo4j."))
        self.patientText.setPlainText(_translate("MainWindow", "ID,Dataset,Diagnosis,Gender"))
        self.label_5.setText(_translate("MainWindow", "Select the video file for the screen recording. After choosing file, click \'Run Scan\' to generate report."))
        self.videoFileName.setText(_translate("MainWindow", "FileName"))
        self.selectVideoFile.setText(_translate("MainWindow", "Select Video File"))
        self.label_2.setText(_translate("MainWindow", "Appointment Details"))
        self.reportText.setPlainText(_translate("MainWindow", "The details from recorded settings will appear here. Once visible, edit or delete any msitakes, and copy--paste to your records. If you would like to save the text file, enter the directory and click \'Select Save Location\'."))
        self.saveLocation.setText(_translate("MainWindow", "SaveLocation"))
        self.selectSaveLocation.setText(_translate("MainWindow", "Select Save Location"))
        self.runButton.setText(_translate("MainWindow", "Run Scan"))
        self.importCheckBox.setText(_translate("MainWindow", "Import to Neo4j"))
        self.saveCheckBox.setText(_translate("MainWindow", "Save Scan Results"))

    @pyqtSlot()
    def saveCheckBoxSlot(self):
        pass

    @pyqtSlot()
    def patientTextEntered(self):
        pass

    @pyqtSlot()
    def videoFileSlot(self):
        pass

    @pyqtSlot()
    def findVideoFileSlot(self):
        pass

    @pyqtSlot()
    def reportSlot(self):
        pass

    @pyqtSlot()
    def saveTextEntered(self):
        pass

    @pyqtSlot()
    def findFileSlot(self):
        pass

    @pyqtSlot()
    def runSlot(self):
        pass

    @pyqtSlot()
    def importToNeoSlot(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
