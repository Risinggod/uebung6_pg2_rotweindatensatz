import pandas as pd
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

path = "winequality-red.csv"

data = pd.read_csv(path, delimiter=";")

print(data)

model = KMeans()

#visualizer = KElbowVisualizer(model, K=(2, 9), timings=False)
#visualizer.fit(data)
#visualizer.show()

KMeans = KMeans(n_clusters=4)

pred = KMeans.fit_predict(data)

data_new = pd.concat([data, pd.DataFrame(pred, columns=["label"])], axis=1)

print(data_new)

plt.scatter(data_new["quality"], data_new['label'])
plt.xlabel('quality')
plt.ylabel('label')
plt.show()

#data_new.to_csv("./data_new_winequality.csv")