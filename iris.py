import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as plt
iris = pd.read_csv("iris.csv")
iris_setosa = iris.iloc[0:50,[2]]
iris_versicolor = iris.iloc[50:100,[2]]
iris_virginica= iris.iloc[100:150,[2]]
print(iris.head(4))
print(iris.tail(4))
print(iris.shape)
print("The size of the iris dataset is:- " , iris.size)
print(f"The size is :-  (fstring used) {iris.size}")
print(f"The size is {iris.size}")
print(f"The columns are {iris.columns}")
print(iris["species"].value_counts())
iris.plot(kind = 'scatter',x='sepal_length',y='sepal_width')
plt.show()
sbn.set_style("whitegrid") ; 
sbn.FacetGrid(iris,hue = "species", size = 5) \
    .map(plt.scatter,"sepal_length","sepal_width") \
    .add_legend()
plt.show()
plt.close();
sbn.set_style("whitegrid")
sbn.pairplot(iris,hue = "species", size = 3)
plt.show()

print("Means")
print("Mean of Setosa - Petal Length" , np.mean(iris_setosa["petal_length"]))
print("Mean of Versicolor - Petal Length", np.mean(iris_versicolor["petal_length"]))
print("Mean of Virginica - Petal Length", np.mean(iris_virginica["petal_length"]))
print("standard deviation")
print("std of Setosa - Petal Length" , np.std(iris_setosa["petal_length"]))
print("std of Versicolor - Petal Length", np.std(iris_versicolor["petal_length"]))
print("std of Virginica - Petal Length", np.std(iris_virginica["petal_length"]))
print(iris_setosa.tail(4))
print(iris.iloc[1:3])
print(iris_virginica.head())