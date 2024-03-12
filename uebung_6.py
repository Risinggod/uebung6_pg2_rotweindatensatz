import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Aufgabe 1
path = "winequality-red.csv"
df = pd.read_csv(path, delimiter=";")

print(df.head())
#print(df.tail())
#print(df.info())

print(df.isnull().any())

df = df.drop_duplicates()

descriptiv_statistic = df.describe()
print(descriptiv_statistic)

correlation = df.corr()
print(correlation["quality"].sort_values())

histogramm_varibal= df["alcohol"]
plt.hist(histogramm_varibal)
plt.title("verteilung des Alhoholgehalts")
plt.show()

plt.scatter(df['alcohol'], df['quality'])
plt.title('Alkoholgehalt vs. Qualität des Weins')
plt.show()

df.boxplot(column='alcohol', by='quality')
plt.title('Alkoholgehalt nach Weinqualität')
plt.show()










