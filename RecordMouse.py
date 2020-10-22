from PyQt5.QtCore import QThread, pyqtSignal, QObject
from pynput.mouse import Button, Listener

from action_handler import handle_actions
from Classifier import Classifier


def downsizing(list):
    while len(list) > 100:
        list = [list[i] for i in range(len(list)) if i % 2 == 0]
    return list


class RecordMouse(QThread):
    gesSignal = pyqtSignal(object)
    # Here i use QThread rather than QRunnable.
    # Because QRunnable and QThreadPool can not be stop mid-processing.
    def __init__(self, *args, **kwargs):
        super(RecordMouse, self).__init__()

        # Store constructor arguments (re-used for processing)

        self.args = args
        self.kwargs = kwargs

        # initialize some arguments
        self.btn_pressed = False
        self.points = []
        self.ges_dict = None
        self.all_models = None
        self.final_ges = None
        self.current_action = None
        self._stopped = True
        self.listener = None

    def __del__(self):
        self.wait()

    def on_move(self, x, y):
        if self.btn_pressed:
            x = int(x)
            y = int(y)
            self.points.append([x, y])

    def on_click(self, x, y, button, pressed):
        if button == Button.middle and pressed:
            self.btn_pressed = True
        else:
            self.btn_pressed = False
            if len(self.points) > 0:
                # downsizing the list of points
                self.points = downsizing(self.points)
                self.classify(self.all_models, self.points)
                current_action = handle_actions(self.ges_dict, self.final_ges)
                # ------------
                self.gesSignal.emit(current_action)

            self.points.clear()

    def Listen(self):
        with Listener(on_move=self.on_move, on_click=self.on_click) as self.listener:
            self.listener.join()

    def pass_data(self, ges_dict, all_models):

        self.ges_dict = ges_dict
        self.all_models = all_models

    def classify(self, all_models, points):
        classifier = Classifier(all_models, points)
        self.final_ges = classifier.ges

    def print_ges(self):
        if self.final_ges:
            print('what you draw is ' + self.final_ges)
        else:
            print('no gesture for you')

    def stop(self):
        # stopping listener
        self._stopped = True
        self.listener.stop()

    def run(self):
        self._stopped = False
        while True:
            self.Listen()
            # stop listener when stop function was called
            if self._stopped:
                break
            else:
                break


