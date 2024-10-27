import pandas as pd 
from CostFunction import HypothesisCalculator

    # def __init__(self, X, y, alpha, numberOfEntries, theta):
    #     self.X = X
    #     self.y = y
    #     self.alpha = alpha
    #     self.n = numberOfEntries
    #     self.theta = theta
    #     self.gd = GradientDescent(self.X, self.y, self.theta, self.alpha, self.n)

class GradientDescent:

    def __init__(self, X, y, alpha, theta, numberOfEntries):
        self.X = X
        self.y = y
        self.alpha = alpha
        self.theta = theta
        self.n = numberOfEntries
        self.hypo = HypothesisCalculator(self.X, self.theta)

    def theta_values(self, thetas):
        self.thetas = thetas
        # hypo = HypothesisCalculator(self.X, self.theta)
        #self.thetas[1] = self.theta[1] - (self.alpha/self.n)*(self.hypo.calculate(1)-self.y[1])
        #self.thetas[2] = self.thetas[2] - (self.alpha/self.n)*(self.hypo.calculate(2)-self.y[2])
        n = len(self.theta) - 1
        while(n == 0):
            self.thetas[n] = self.thetas[n] - (self.alpha/self.n)*(self.hypo.calculate(n)-self.y[n])
            n = n-1
        return self.thetas