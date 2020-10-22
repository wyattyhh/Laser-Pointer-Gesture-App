import matplotlib.pyplot as plt
import math
from scipy.stats import multivariate_normal
import numpy as np


class State:

    def __init__(self, mean, covariance, weight):
        self.mean = mean
        self.covariance = covariance
        self.weight = weight


class HiddenMarkovModel:
    # Here we use Expectation–maximization algorithm to learn data.

    def __init__(self, states_num, ges_name, ges_data):
        self.all_states = []
        # self.transMat = []
        self.initializeData1 = self.initializeData(ges_data['X'])
        self.ges_name = ges_name
        self.states_num = states_num
        self.states_list = []
        self.train_data = self.initializeData1[0:70]
        self.test_data = self.initializeData1[70:100]
        self.gaussian(self.train_data)
        self.init_trans()

    def initializeData(self, ges_data):
        # get mean
        mean_x = []
        mean_y = []
        for i in range(len(ges_data)):
            sum_x = 0.0
            sum_y = 0.0
            for j in range(len(ges_data[i])):
                sum_x += ges_data[i][j][0]
                sum_y += ges_data[i][j][1]
            mean_x.append(sum_x / len(ges_data[i]))
            mean_y.append(sum_y / len(ges_data[i]))

        # get deviation
        dev_x = []
        dev_y = []
        for i in range(len(ges_data)):
            diff_x = 0
            diff_y = 0
            for j in range(len(ges_data[i])):
                # get diff
                diff_x += (ges_data[i][j][0] - mean_x[i]) ** 2
                diff_y += (ges_data[i][j][1] - mean_y[i]) ** 2
            # get variance
            var_x = diff_x / len(ges_data[i])
            var_y = diff_y / len(ges_data[i])
            # append standard deviation
            dev_x.append(math.sqrt(var_x))
            dev_y.append(math.sqrt(var_y))
        # get z-score/standard score
        for i in range(len(ges_data)):
            for j in range(len(ges_data[i])):
                ges_data[i][j][0] = (ges_data[i][j][0] - mean_x[i]) / dev_x[i]
                ges_data[i][j][1] = (ges_data[i][j][1] - mean_y[i]) / dev_y[i]
        return ges_data

    def init_trans(self):
        self.transMat = np.zeros((self.states_num, self.states_num))
        self.transMat = self.transMat.astype(dtype=np.float64)
        for i in range(self.states_num - 1):
            self.transMat[i][i] = 0.75
            self.transMat[i][i + 1] = 0.25
        self.transMat[self.states_num - 1][self.states_num - 1] = 1

        for i in range(len(self.train_data)):
            plt.plot(*zip(*self.train_data[i]), marker='.', color='r', ls='')
        for s in self.all_states:
            x1, y1 = np.random.multivariate_normal(s.mean, s.covariance, 5000).T
            plt.plot(x1, y1, 'x')

    def evaluate(self, obs):
        # print(obs)

        # forward-backward algorithm
        obs = self.initializeData([obs])
        # obs = self.initializeData(obs)
        # plt.show()
        T = len(obs[0])
        self.alpha = np.dtype(np.float64)
        self.alpha = np.arange(T * self.states_num, dtype=np.float64).reshape(self.states_num, T)
        self.alpha[0][0] = 1.0
        for s in range(1, self.states_num):
            self.alpha[s][0] = 0.0
        self.beta = np.dtype(np.float64)
        self.beta = np.arange(T * self.states_num, dtype=np.float64).reshape(self.states_num, T)
        for s in range(0, self.states_num):
            self.beta[s][T - 1] = 1.0
        for t in range(0, T - 1):
            for i in range(self.states_num):
                sumAlpha = 0.0
                for j in range(self.states_num):
                    sumAlpha = sumAlpha + self.alpha[j][t] * (self.transMat[j][i])

                self.alpha[i][t + 1] = float(sumAlpha * ((multivariate_normal.pdf(obs[0][t + 1],
                                                                                  self.all_states[i].mean,
                                                                                  self.all_states[i].covariance))))

        for t in range(0, T - 1):
            for i in range(self.states_num):
                sumBeta = 0
                for j in range(self.states_num):
                    sumBeta = sumBeta + (self.transMat[i][j]) * (multivariate_normal.pdf(obs[0][T - t - 1],
                                                                                         self.all_states[j].mean,
                                                                                         self.all_states[
                                                                                             j].covariance)) * \
                              self.beta[j][T - t - 1]
                self.beta[i][T - t - 2] = sumBeta

        prob = 0
        for t in range(T):
            for i in range(self.states_num):
                prob = prob + self.alpha[i][t] * self.beta[i][t]
                # print (prob)
        return prob

    def logLikelihood(self, data):

        llh = list()
        for obs in data:
            sumLog = 0
            for point in obs:
                sumC = 0
                for s in self.all_states:
                    sumC = sumC + s.weight * multivariate_normal.pdf(point, s.mean, s.covariance)
                if sumC == 0.0:
                    sumC = 0.0000001
                sumLog = sumLog + math.log(sumC)
            llh.append(sumLog)
        prob = sum(llh) / len(llh)
        return prob

    def gaussian(self, data):
        pnts = 0
        for obs in data:
            pnts = pnts + len(obs)
        pnts = int(pnts / self.states_num)
        part = int(pnts / len(data))
        for s in range(self.states_num):
            xp = list()
            yp = list()
            for obs in data:
                for i in range(s * part, part + s * part):
                    if (i >= len(obs)):
                        break
                    xp.append(obs[i][0])
                    yp.append(obs[i][1])
            self.all_states.append(State([np.mean(xp), np.mean(yp)], np.cov(xp, yp), 1 / self.states_num))
            xp.clear()
            yp.clear()
