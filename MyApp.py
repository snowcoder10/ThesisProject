# This is the connection to the unctioning app
# Kevin Castell -- Butson Lab at SCI
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from mainwindow import Ui_MainWindow
import sys
import Process
import WorkingWithNeo4j
import os


class MainWindowUIClass(Ui_MainWindow):
    def __init__(self):
        # intiialize the super class
        super().__init__()

        # variables to hold any entered/changed text as well as boolean for neo4j import
        self.patientInfoText = ""
        self.videoFileLocationText = ""
        self.saveLocationText = ""
        self.importToNeo4jBool = False
        self.saveCheckBoxBool = False

    def setupUi(self, MW):
        # setup the UI of the super
        # add code here that relates to how we want the UI to operate
        super().setupUi(MW)

    def debugPrint(self, msg):
        # use this for debugging the UI by printing the actions of the user
        print(msg)

    #@pyqtSlot()
    def patientTextEntered(self):
        # called when the patient information changes or is entered
        #self.debugPrint("Patient Text changed")
        """place code here if needed"""

    #@pyqtSlot()
    def videoFileSlot(self):
        # called when the video file text is changed
        #self.debugPrint("Video file text changed")
        """place code here if needed"""

    #@pyqtSlot()
    def findVideoFileSlot(self):
        # called when the video file finder button is clicked
        #self.debugPrint("Video file button clicked")

        # opening a file explorer to find the file
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            "All Files (*);;Python Files (*.py)",
            options=options)

        # setting the video file line text
        self.videoFileName.setText(fileName)

    #@pyqtSlot()
    def reportSlot(self):
        # called when the report text is changed.
        # This is where the text will be printed to at end of report.
        #self.debugPrint("Report text changed")
        """place code here if needed"""

    #@pyqtSlot()
    def saveTextEntered(self):
        # this is called when the save location is changed
        #self.debugPrint("Save location changed")
        """place code here if needed"""

    #@pyqtSlot()
    def findFileSlot(self):
        # this is called when the save location button is clicked
        # FIXME: to select a directory not a file
        #self.debugPrint("Save location button clicked")

        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName = QtWidgets.QFileDialog.getExistingDirectory(
            None,
            "QFileDialog.getOpenFileName()",
            "All Files (*);;Python Files (*.py)"
            ,options=options)

        # setting the save file line text
        self.saveLocation.setText(fileName)

    #@pyqtSlot()
    def runSlot(self):
        # this is called when the run button is clicked
        #self.debugPrint("The run button was clicked")

        # get the updated information, and then run the scan
        self.updateInfoForRun()
        
        # call the scan
        # FIXME: This needs fixed if we want the save to be optional

        try:
            # display dialog that the scan is running
            m1 = QtWidgets.QMessageBox()
            m1.setText("Scan is about to start press OK to continue.\n"
                       "Once scan starts please wait this may take a few minutes.\n")
            m1.setIcon(QtWidgets.QMessageBox.Warning)
            m1.setStandardButtons(QtWidgets.QMessageBox.Ok
                                  | QtWidgets.QMessageBox.Cancel)
            m1.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            ret = m1.exec_()
            Process.main(self.videoFileLocationText,self.saveLocationText)
            m1.setText("Scan Complete!")
            ret = m1.exec_()

            # read the data and print to the dialog box
            with open(self.saveLocationText + '/review_settings.csv') as f1:
                s1 = f1.read() + '\n'
            with open(self.saveLocationText + '/patient_limits.csv') as f2:
                s2 = f2.read() + '\n'
            self.reportText.setPlainText(s1 + '\n' + s2)

        except Exception as ex:
            m1.accept()
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            m2 = QtWidgets.QMessageBox()
            m2.setText("Invalid file name!\nCheck the video file and save location.\n"
                       + message)
            m2.setIcon(QtWidgets.QMessageBox.Warning)
            m2.setStandardButtons(QtWidgets.QMessageBox.Ok
                                 | QtWidgets.QMessageBox.Cancel)
            m2.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            ret = m2.exec_()

        # if the import option is selected lets run that
        # the files come from 'Process'
        if self.importToNeo4jBool:
            WorkingWithNeo4j.main(self.patientInfoText, self.saveLocationText + '/review_settings.csv',
                                  self.saveLocationText + '/patient_limits.csv')

        if not self.saveCheckBoxBool:
            os.remove(self.saveLocationText + '/patient_limits.csv')
            os.remove(self.saveLocationText + '/review_settings.csv')

    #@pyqtSlot()
    def importToNeoSlot(self):
        # this is called when the import to neo4j box is clicked
        #self.debugPrint("The import to neo4j box clicked")

        # update the boolean
        if self.importToNeo4jBool:
            self.importToNeo4jBool = False
        else:
            self.importToNeo4jBool = True

    #@pyqtSlot()
    def saveCheckBoxSlot(self):
        # this is called when the save check box is selected
        #self.debugPrint("The save box was clicked")

        # update the boolean
        if self.saveCheckBoxBool:
            self.saveCheckBoxBool = False
        else:
            self.saveCheckBoxBool = True

    def updateInfoForRun(self):
        # when this is called all the entered information is pulled from the GUI
        #self.debugPrint("The Update Completed")
        self.patientInfoText = self.patientText.toPlainText()
        self.videoFileLocationText = self.videoFileName.text()
        self.saveLocationText = self.saveLocation.text()


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUIClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


main()
