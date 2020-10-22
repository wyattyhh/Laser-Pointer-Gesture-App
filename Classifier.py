import math


class Classifier:

    def __init__(self, allModels, points):
        self.allModels = allModels
        self.points = points
        self.ges = None
        for model in self.allModels:
            cName = self.classify(self.points)
            if cName == model.ges_name:
                self.ges = model.ges_name

    def classify(self, points):
        classRes = None
        maxRes = None
        for model in self.allModels:
            ev = model.evaluate(points)
            if classRes is None or ev > maxRes:
                classRes = model
                maxRes = ev
        maxRes.item()
        if maxRes > math.exp(-150):
            return classRes.ges_name
        else:
            self.ges = None
