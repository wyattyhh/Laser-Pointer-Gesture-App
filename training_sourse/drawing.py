import cv2
import numpy as np
import pickle

# First, change the gesture type as the one you want to store
# as well as number of the gesture
# GESTURE TYPE :
# LEFT; RIGHT; UP; DOWN; UPDOWN; DOWNUP; DOWNRIGHT; DOWNLEFT; UPRIGHT; UPLEFT; CIRCLE
ges_type = 'CROSS'
ges_num = 100

# Prepare basic valuable
img = np.zeros((512, 512, 3), np.uint8)
file_name = ges_type + '.pickle'
ges_data = []


# a class to store mouse move coordinates.
class CoordinateStore:
    def __init__(self):
        self.points = []
        self.drawing = False
        self.init = 0

    def draw_circle(self, event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True

        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing:
                cv2.circle(img, (x, y), 1, (0, 0, 225), -1)
                self.points.append([x, y])

        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            cv2.circle(img, (x, y), 1, (0, 0, 255), -1)
            self.init += 1


# instantiate class
coordinateStore = []


def store(data, type):
    temp = {'X': list(), 'Y': list()}
    for i in range(0, ges_num):
        temp['X'].append(data[i])
        temp['Y'].append(type)
    with open(file_name, "wb") as scores:
        pickle.dump(temp, scores)


def main():
    for i in range(ges_num):
        coordinateStore.append(CoordinateStore())
        windowName = 'Draw ' + ges_type + ' gesture NO.' + str(i + 1)
        cv2.namedWindow(windowName)
        cv2.setMouseCallback(windowName, coordinateStore[i].draw_circle)

        while True:
            cv2.imshow(windowName, img)
            k = cv2.waitKey(1)
            if k == 27:
                break
            elif coordinateStore[i].init == ges_num:
                break

        cv2.destroyAllWindows()
        ges_data.append(coordinateStore[i].points)
    a = ''
    while a != 'yes': # in case running this program by accident and erasing data
        a = input('Do you wanna store data?')
    store(ges_data, ges_type)
    with open(file_name, 'rb') as f:
        obs = pickle.load(f)
    print(obs)


if __name__ == "__main__":
    main()
