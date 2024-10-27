import pandas as pd 

# def CostFunction(X, y, alpha, numberOfEntries, theta):


#     #now type the hypothesis
#     #h(0)
#     for i in theta:
#         hypothesis
#     if CostFunction == 0:
#         return theta
#     else:
#         cf = 


#hypothesis should be a function
#n brings the row number you 


# def hypothesis(X, theta, n):
#     #take the length of theta
#     #N brings out the number of column
#     N = len(theta)-1
#     h = theta[0]
#     while(N >= 1):
#         h += X.iloc[n][N-1]*theta[N]
#         N = N-1
    
#     return h

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