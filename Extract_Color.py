import PIL
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter
import numpy as np
class Extract:
    def __init__(self):
        self.clt=KMeans(n_clusters=4)
        self.k_cluster=[]
    def Clt(self,n):
        self.clt=KMeans(n_clusters=n)
    def fit(self,masked):
        self.k_cluster=self.clt.fit(masked.reshape(-1,3))
        
    def palette_perc(self):
        width = 300
        palette = np.zeros((50, width, 3), np.uint8)
        
        n_pixels = len(self.k_cluster.labels_)
        counter = Counter(self.k_cluster.labels_) # count how many pixels per cluster
        perc = {}
        for i in counter:
            perc[i] = np.round(counter[i]/n_pixels, 2)
        perc = dict(sorted(perc.items()))
        
        step = 0
        
        for idx, centers in enumerate(self.k_cluster.cluster_centers_): 
            palette[:, step:int(step + perc[idx]*width+1), :] = centers
            step += int(perc[idx]*width+1)
            
        return palette, perc, self.k_cluster
    
    def Centers(self):
        return self.k_cluster.cluster_centers_
