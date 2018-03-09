import pandas
data = pandas.read_csv('datasets/titanic-machine-learning-from-disaster/train.csv',index_col = 'PassengerId')
print(data.head())