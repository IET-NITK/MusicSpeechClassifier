''' Support Vector Machine (SVM) '''

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing dataset
X = np.load("X_values.npy")
y = np.load("y_values.npy")

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)


# calculating accuracy
accuracy = (cm[0,0] + cm[1,1]) * 100 / len(y_pred)
print("Accuracy of Linear SVM:",accuracy,"%")