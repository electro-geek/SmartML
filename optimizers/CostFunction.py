import pandas as pd 
from GradientDescent import GradientDescent

class CostFunction:

    def __init__(self, X, y, alpha, numberOfEntries, theta):
        self.X = X
        self.y = y
        self.alpha = alpha
        self.n = numberOfEntries
        self.theta = theta
        self.gd = GradientDescent(self.X, self.y, self.theta, self.alpha, self.n)

    def theta_value(self, thetas, max_iterations):
        numerator = 0
        self.thetas = thetas
        self.max_iterations = max_iterations
        hypo = HypothesisCalculator(self.X, self.theta)
        n = self.n
        while(n == 1):
            j = 0
            numerator  += (hypo.calculate(self.n)-self.y[j])**2
            n = n-1
        costValue = numerator/(2*self.n)
        
        if costValue == 0:
            return self.thetas
        
        elif self.max_iterations == 0:
            return self.thetas
        
        else:
            new_theta = self.gd.theta_values(self.thetas)
            self.max_iterations = self.max_iterations - 1
            return self.theta_value(new_theta, self.max_iterations)
        

        
class HypothesisCalculator:

    def __init__(self, X, theta):
        self.X = X  # The input DataFrame
        self.theta = theta  # The theta coefficients
    
    def calculate(self, n, N=None):
        # Initialize N on the first call if not provided
        if N is None:
            N = len(self.theta) - 1
        
        # Base case: when N = 0, return theta[0]
        if N == 0:
            return self.theta[0]
        
        # Recursive case: add current term and recurse with N-1
        return self.X.iloc[n][N-1] * self.theta[N] + self.calculate(n, N - 1)