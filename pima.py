import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# The python3 is available in your machine
# Make sure the 'pima_diabetes.csv' file is in the same directory as your Python script or notebook.


# a) Read the dataset using pandas' DataFrame:
data = pd.read_csv('diabetes.csv')
print(f"The dataset \n {data}, {type(data)} \n\n")
# ans: [768 rows x 9 columns], <class 'pandas.core.frame.DataFrame'>


# b) Find the number of instances and features:
num_instances = data.shape[0]
num_features = data.shape[1]
print("Number of instances:", num_instances)  # ans: Number of instances: 768
print("Number of features:", num_features, end='\n\n')  # ans: Number of features: 9


# c) Check for missing entries:
missing_entries = data.isnull().sum().sum()
if missing_entries == 0:
    print("The dataset has no missing entries.")
else:
    print("The dataset has", missing_entries, "missing entries.")

# ans: The dataset has no missing entries.


# d) Count the number of instances for each outcome value:
outcome_counts = data['Outcome'].value_counts()
print(f"\nOutcome_counts {outcome_counts}")
"""
Outcome
0    500
1    268
Name: count, dtype: int64
"""

# e) Show the first 5 and last 5 instances:
first_instances = data.head(5)
last_instances = data.tail(5)
print("\nFirst 5 instances:\n", first_instances, end='\n\n')
"""
First 5 instances:
    Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  DiabetesPedigreeFunction  Age  Outcome
0            6      148             72             35        0  33.6                     0.627   50        1
1            1       85             66             29        0  26.6                     0.351   31        0
2            8      183             64              0        0  23.3                     0.672   32        1
3            1       89             66             23       94  28.1                     0.167   21        0
4            0      137             40             35      168  43.1                     2.288   33        1
"""

print("Last 5 instances:\n", last_instances, end='\n\n')
"""
Last 5 instances:
      Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  DiabetesPedigreeFunction  Age  Outcome
763           10      101             76             48      180  32.9                     0.171   63        0
764            2      122             70             27        0  36.8                     0.340   27        0
765            5      121             72             23      112  26.2                     0.245   30        0
766            1      126             60              0        0  30.1                     0.349   47        1
767            1       93             70             31        0  30.4                     0.315   23        0
"""


# f) Check if missing entries are replaced by zeros:
zero_entries = (data == 0).sum().sum()
if zero_entries > 0:
    print("\nThe dataset contains", zero_entries, "zero entries.")
else:
    print("\nThe dataset does not have missing entries replaced by zeros.")
# ans: The dataset contains 1263 zero entries.


# g) Draw a histogram for each numerical feature:

data.hist(figsize=(10, 10))


# h) Split the dataset into X and y:
x = data.drop('Outcome', axis=1)
y = data['Outcome']
print(f"X {x}")
print(f"y {y}")
# Here, X contains all the predictors/features, and y contains the target class entries.

# i) Split the dataset into train and test sets:
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

"""
This code splits the dataset into an 80% train set and a 20% test set. 
Adjust the test_size parameter if you want a different split ratio.
"""




"""
j) Apply the KNN classifier with the Euclidean distance metric and 
determine the suitable value of the hyperparameter k:
"""

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Determine suitable k value
train_accuracy = []
test_accuracy = []
k_values = range(1, 31)

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
    knn.fit(X_train_scaled, y_train)
    train_accuracy.append(knn.score(X_train_scaled, y_train))
    test_accuracy.append(knn.score(X_test_scaled, y_test))

# Plot train and test accuracy with respect to k
plt.plot(k_values, train_accuracy, label='Train Accuracy')
print("j ", plt)
plt.show()  # result file test_accuracy_result.png

