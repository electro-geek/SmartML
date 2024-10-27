from CheckingpandasDF import DataFrameloader
from CostFunction import hypothesis
import pandas as pd


# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [24, 27, 22, 32],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
# }
# df = pd.DataFrame(data)

# # Initialize the DataFrameHandler with the DataFrame
# df_handler = DataFrameloader(df)
# print(df_handler.get_rowElement(0,0))

theta = [1,2,3,4]
data = {
    'x1' :[1, 2, 3],
    'x2' : [4,5,6],
    'x3': [7, 8, 9]
}

X = pd.DataFrame(data)
print(len(theta))
print(hypothesis(X, theta, 0))