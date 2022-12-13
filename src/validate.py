import os
import numpy as np

# Laden der Prädiktionsdaten
path_test_prediction = os.path.join("data", "model", "testdata_prediction.npy")
data_test_prediction = np.load(path_test_prediction)

# Laden der Zieldaten
path_test_target = os.path.join("data", "model", "testdata_target.npy")
data_test_target = np.load(path_test_target)

# Validierung
data_diff = np.subtract(data_test_target, data_test_prediction)

print(data_diff)
print("Maximale Abweichung der Werte von Ziel und Prädiktion: ",
      np.amax(a=data_diff))
