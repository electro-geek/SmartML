import pandas as pd
from ..optimizers.CostFunction import CostFunction

class LinearRegression:

    def __init__(self, alpha, max_iterations, df, theta):
        self.alpha = alpha
        self.max_iterations = max_iterations
        self.df = df
        self.theta = theta
    

    def fit(self, X , y):
        self.X = X
        self.y = y
        #load the values of X and y in cost function and get the values of new thetas
        #In other words get the weight of the model 
        cf = CostFunction(self.X, self.y, self.alpha, numberOfEntries, self.theta)

    def predict(self, x):


































