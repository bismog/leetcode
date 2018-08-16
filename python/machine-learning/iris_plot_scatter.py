from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()
x = pd.DataFrame(iris['data'], columns=iris['feature_names'])
y = pd.DataFrame(iris['target'], columns=['target_names'])
o = pd.concat([x,y], axis=1)
# print iris['target']
# print iris['target_names']
# print o
o.plot.scatter(x="sepal length (cm)", y="sepal width (cm)", c="target")
