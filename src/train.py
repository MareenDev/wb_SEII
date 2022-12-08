import pandas as pd
import os
import pickle
from sklearn import model_selection
from sklearn.linear_model import LinearRegression

# Daten aus Datei auslesen
path = os.path.join("data", "auto_mpg.csv")
df = pd.read_csv(path, sep=';')
array = df.values

features = array[:, 1:]
target = array[:, 0:1]

# Splitting der Daten in Test- und Trainingsdaten
X_train, X_test, y_train, y_test = model_selection.train_test_split(
    features, target, test_size=0.8)

# Modell trainieren
model = LinearRegression()
model.fit(X_train, y_train)

# Modell speichern
path_new = os.path.join("data", "model", "model.sav")
pickle.dump(model, open(path_new, 'wb'))
