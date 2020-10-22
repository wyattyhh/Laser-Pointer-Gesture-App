import time
from collections import deque

import cv2
import imutils
import numpy as np
from PyQt5.QtCore import QThread, QObject, pyqtSignal, QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QMainWindow

from action_handler import handle_actions
from Classifier import Classifier
from init_ml import initML_pw


class RecordLaser(QThread):
    frameCaptured = pyqtSignal(QPixmap)
    gesSignal = pyqtSignal(object)

    # https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
    def __init__(self):
        super().__init__()
        # initial parameters
        self.que_buffer = 64
        self.low_red = np.array([160, 100, 100])
        self.high_red = np.array([179, 255, 255])
        self.pts = deque(maxlen=self.que_buffer)
        self.pts1 = []
        self.last_pt = None
        self.points = None
        self._stopped = True
        self.show_frame = False
        self.i = 0
        self.vc = cv2.VideoCapture(0)
        self.frame_rate = self.vc.get(cv2.CAP_PROP_FPS)
        self.set_mirror = False
        self.all_models = initML_pw()
        self.timer = None

    def initTimer(self):
        self.timer = QTimer(self)
        self.timer.setTimerType(Qt.VeryCoarseTimer)
        self.timer.timeout.connect(self.running)

    def running(self):
        # grab the current frame
        ret, frame = self.vc.read()
        # resize the frame, blur it , and convert it to rhe HSV color space
        frame = imutils.resize(frame, width=600)
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        heigt, width = frame.shape[:2]

        mask = cv2.inRange(hsv, self.low_red, self.high_red)
        mask = cv2.erode(mask, None, iterations=1)
        mask = cv2.dilate(mask, None, iterations=1)

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        center = None

        # only proceed if at least one contour was found
        if len(cnts) > 0:
            # find the largest contour in the mask, then use it to compute the minimum enclosing circle and centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            # only proceed if the radius meets a minimum size
            if radius > 10:
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                cv2.circle(frame, (int(x), int(y)), int(radius),
                           (0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)

        # update the points queue
        self.pts.appendleft(center)

        # loop over the set of tracked points
        for i in range(1, len(self.pts)):
            # if either of the tracked points are None, ignore
            # them
            if self.pts[i - 1] is None or self.pts[i] is None:
                continue
            # otherwise, compute the thickness of the line and
            # draw the connecting lines
            thickness = int(np.sqrt(self.que_buffer / float(i + 1)) * 2.5)
            cv2.line(frame, self.pts[i - 1], self.pts[i], (0, 0, 255), thickness)
            self.pts1.append(self.pts[i])
        if center:
            enable_points = True
            self.pts1.append(self.last_pt)
            self.last_pt = center
        else:
            if len(self.pts1) == 30:
                points = []
                if not self.set_mirror:
                    for pt in reversed(self.pts1):
                        points.append(list(pt))
                else:
                    for pt in self.pts1:
                        points.append(list(pt))
                # grab points it into classifier
                if self.points is not points:
                    self.points = points

                    self.classify(self.all_models, self.points)
                    print(self.final_ges)  # print gesture
                    current_action = handle_actions(self.ges_dict, self.final_ges)
                    self.gesSignal.emit(current_action)

                    self.points = []
                    self.pts1 = []
                    time.sleep(1)  # this step avoiding system from frozen

                self.pts1 = []
            self.pts1 = []
        pixmap = QImage(frame, width, heigt, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(pixmap)

        self.frameCaptured.emit(pixmap)

    def pass_data(self, ges_dict, all_models):
        self.ges_dict = ges_dict
        self.all_models = all_models

    def classify(self, all_models, points):
        classifier = Classifier(all_models, points)
        self.final_ges = classifier.ges

    def stop(self):
        # stopping timer
        self.timer.stop()

    def mirror(self):
        self.set_mirror = True

    def start(self, **kwargs):
        self.initTimer()
        self.timer.start()


class RealTimeWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.move(300, 300)
        self.setWindowTitle('OPENCV')
        self.setGeometry(300, 300, 500, 250)
        self.resize(500, 355)

        self.myLabel = QLabel(self)
        self.myLabel.setText("Please draw")
        self.myLabel.resize(500, 350)

