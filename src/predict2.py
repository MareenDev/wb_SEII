import os
import pickle
import numpy as np

# Lesen der serialisierten Model-Daten

path = os.path.join("data", "model", "model.sav")
file_model = open(path, 'rb')
loaded_model = pickle.load(file_model)
file_model.close()

# Lesen der Test-Feature-Daten
path_test_features = os.path.join("data", "model", "testdata_features.npy")
data_test_features = np.load(path_test_features)

# Prediktion auf Basis der Testdaten
prediction = loaded_model.predict(data_test_features)
print(prediction)

path_test_prediction = os.path.join("data", "model", "testdata_prediction.npy")
np.save(path_test_prediction, prediction)
