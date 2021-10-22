from sklearn.datasets import make_blobs
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import time

from DBSCAN import DBSCAN

color_dict = dict({'NOISE':'gray',
              'cluster0':'blue',
              'cluster1':'green',
              'cluster2':'orange'})

# データセット生成
centers = [[-1.5, 0.5], [0.5, 2], [1, -1.5]] # 答えは3つのクラスターに分かれる
stds = [0.3, 0.5, 0.1] # それぞれのクラスターの標準偏差 (ばらつき具合)
X, labels_true = make_blobs(n_samples=1000, centers=centers, cluster_std=stds, random_state=0)
labels_true = ['cluster{}'.format(x) for x in labels_true]
fig = plt.figure(figsize=(10, 10))
scatter_plot = sns.scatterplot(x=X[:,0], y=X[:,1], palette=color_dict, hue=labels_true)
figure = scatter_plot.get_figure()
figure.savefig("true_fig.png")

eps = 0.2
min_samples = 10

# DBSCANのテスト
st = time.time()
db = DBSCAN(eps=eps, min_samples=min_samples)
db.fit(X)
print("DBSCAN time: {}".format(time.time() - st))
labels = ['NOISE' if x==-1 else 'cluster{}'.format(x) for x in db.get_labels()]
fig = plt.figure(figsize=(10, 10))
scatter_plot = sns.scatterplot(x=X[:,0], y=X[:,1], palette=color_dict, hue=labels)
figure = scatter_plot.get_figure()
figure.savefig("DBSCAN_fig.png")