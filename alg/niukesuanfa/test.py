from sklearn.preprocessing import OneHotEncoder
import numpy as np
enc = OneHotEncoder()
f = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[9]])
print(f.shape)
s = enc.fit_transform(f).toarray()
print(s)
