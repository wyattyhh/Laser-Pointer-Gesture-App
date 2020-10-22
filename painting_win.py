from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPen, QImage
from PyQt5.QtWidgets import QMainWindow, QLabel

from Classifier import Classifier
from init_ml import initML_pw


def downsizing(list):
    while len(list) > 100:
        list = [list[i] for i in range(len(list)) if i % 2 == 0]
    return list


class paintingWindow(QMainWindow):

    def __init__(self,parent = None):
        super().__init__(parent)

        self.setWindowTitle("PaintBrush")
        self.resize(500, 350)

        self.myLabel = QLabel(self)
        self.myLabel.setText("Please draw")
        self.myLabel.adjustSize()

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black

        self.lastPoint = QPoint()

        self.all_models = initML_pw()

        self.final_ges = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
            self.points = []

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint,event.pos())
            self.lastPoint = event.pos()
            x = self.lastPoint.x()
            y = self.lastPoint.y()
            point = [x,y]
            self.points.append(point)
            self.update()

    def mouseReleaseEvent(self, event) :
        if event.button() == Qt.LeftButton:
            self.drawing = False
        self.clear()

        # classify points
        if len(self.points) > 0:
            # downsizing list of points to less than 100 items
            self.points = downsizing(self.points)
            self.classify(self.all_models, self.points)
            self.print_ges()

        # reset list of points
        self.points = []

    def paintEvent(self, event) :
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def classify(self,all_models, points):
        classifier = Classifier(all_models, points)
        self.final_ges = classifier.ges

    def print_ges(self):
        if self.final_ges:
            temp_str = "what you draw is " + str(self.final_ges)
            self.myLabel.setText(temp_str)
            self.myLabel.adjustSize()
            print(1)
        else:
            self.myLabel.setText('sorry no gesture for you')
            self.myLabel.adjustSize()

