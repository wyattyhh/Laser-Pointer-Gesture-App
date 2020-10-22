import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from action_handler import actionToSys
from init_ml import initML_main
from painting_win import paintingWindow
from RecordLaser import RecordLaser, RealTimeWindow
from RecordMouse import RecordMouse
from main_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def openDrawWindow(self):
        self.draw_window = paintingWindow()
        self.draw_window.show()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.setupUi(self)
        self.setWindowTitle('Gesture App')
        self.draw_btn.clicked.connect(self.openDrawWindow)  # open drawing window
        self.mouseMoveEnabled = False
        self.selectedBtn = None
        self.ges_dict = dict.fromkeys(self.buttonGroup.buttons(), None)  # init gestures and actions
        self.buttonGroup.buttonClicked.connect(self.btn_click)  # refresh button clicked information
        self.mouse_recording = RecordMouse()  # create mouse monitoring thread
        self.laser_recording = RecordLaser()  # create laser pointer monitoring thread
        self.actionCombo.activated.connect(self.combo_click)  # create a dictionary to stored bonding actions
        self.deviceCombo.activated.connect(self.reset_checkBox)  # reset function check boxes every time change a device
        self.enableCheck.stateChanged.connect(self.enableAction)  # recording start or stop via enable check box
        self.trackCheck.stateChanged.connect(self.realTime)  # show real-time camera tracking window
        self.mirrorCheck.stateChanged.connect(self.mirror)  # mirror the gesture recording
        self.mouse_recording.gesSignal.connect(actionToSys)  # apply system operation via gestures
        self.laser_recording.gesSignal.connect(actionToSys)  # apply system operation via gestures
        self.hidingSetting()

    def hidingSetting(self):
        self.trackCheck.hide()
        self.mirrorCheck.hide()
        self.label.hide()

    def showingSetting(self):
        self.trackCheck.show()
        self.mirrorCheck.show()
        self.label.show()

    def btn_click(self, btn):
        self.mouseMoveEnabled = True
        self.selectedBtn = btn
        # update bonded actions in action combo box
        if self.ges_dict.get(btn) and self.ges_dict.get(btn) != 0:
            self.actionCombo.setCurrentIndex(self.ges_dict.get(btn))
        else:
            self.actionCombo.setCurrentIndex(0)


    def combo_click(self, index):
        # sync the selected gesture and selected action
        ges_btn = self.selectedBtn
        self.ges_dict[ges_btn] = index
        self.reset_checkBox()

    def reset_checkBox(self):
        self.enableCheck.setChecked(False)
        self.mirrorCheck.setChecked(False)
        self.trackCheck.setChecked(False)
        if self.mouse_recording.listener:
            print('stop mouse recording')
            self.mouse_recording.stop()
        if self.laser_recording.timer:
            print('stop laser pointer recording')
            self.laser_recording.stop()
        if self.deviceCombo.currentText() == 'Mouse':
            self.hidingSetting()
        if self.deviceCombo.currentText() == 'Laser Pointer':
            self.showingSetting()

    def realTime(self):
        if self.trackCheck.isChecked():
            if self.laser_recording.timer:
                self.laser_recording.stop()
            self.real_window = RealTimeWindow()
            self.real_window.setWindowFlag(Qt.FramelessWindowHint)
            self.laser_recording.frameCaptured.connect(self.real_window.myLabel.setPixmap)
            if self.enableCheck.isChecked():
                print(1)
                self.laser_recording.start()
                self.real_window.show()
        else:
            self.real_window.close()

    def mirror(self):
        print('clicked mirror')
        if self.mirrorCheck.isChecked():
            if self.laser_recording.timer:
                self.laser_recording.stop()
            self.laser_recording.set_mirror = True
            print(self.laser_recording.set_mirror)
            if self.enableCheck.isChecked():
                self.laser_recording.start()
        else:
            if self.laser_recording.timer:
                self.laser_recording.stop()
            self.laser_recording.set_mirror = False
            print(self.laser_recording.set_mirror)
            if self.enableCheck.isChecked():
                self.laser_recording.start()

    def enableAction(self):
        if self.enableCheck.isChecked():
            # check if any gestures were assigned
            dict_keys = [*self.ges_dict.values()]
            action_assigned = False
            for item in dict_keys:
                if item and item > 0:
                    action_assigned = True
                    break
            # if yes, enable mouse monitoring
            if action_assigned:
                # check if Mouse or Razor pointer was enabled
                # for mouse:
                if self.deviceCombo.currentText() == 'Mouse':
                    # initialize gesture model data
                    a,b = initML_main(self.ges_dict)
                    print('initialize data!!!')
                    self.mouse_recording.pass_data(a,b)
                    # Not using threadPool right here cuz it can not be stop.
                    self.mouse_recording.start()

                # for laser pointer
                if self.deviceCombo.currentText() == 'Laser Pointer':
                    a, b = initML_main(self.ges_dict)
                    print('initialize data!!!')
                    self.laser_recording.pass_data(a , b)
                    self.laser_recording.start()
                else:
                    self.hidingSetting()
            else:
                QMessageBox.critical(self, 'Error', 'You have not assigned any actions.')
                self.reset_checkBox()
        else:
            self.reset_checkBox()


if __name__ == '__main__':
    # create QApplication class
    app = QApplication(sys.argv)
    form = MainWindow()

    form.show()

    # enter main loop and make sure app ending safely by exit function
    sys.exit(app.exec_())
