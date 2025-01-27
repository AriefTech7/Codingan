import matplotlib.pyplot as mp
import pandas as pd
uci_datasets = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(uci_datasets)
iris.columns = ['SepalLengthCm', 'SepalWidthCm', 'PetaLengthCm', 'PetalwidthCm', 'Species']

iris.plot(kind="scatter",
          x="SepalLengthCm", y="SepalWidthCm")
mp.show()
mp.boxplot(iris.drop ('Species', axis=1).transpose())
mp.violinplot(iris.drop('Species', axis=1).transpose())
mp.plotting.scatter_matrix(iris.drop('Species', axis=1), alpha=0.2)