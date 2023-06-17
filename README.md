# pima-analysis

# Answer of a: [768 rows x 9 columns], <class 'pandas.core.frame.DataFrame'>
# Answer of b: Number of instances: and  Number of features: 9
# Answer of c: The dataset has no missing entries.

# Answer of d
# Outcome
# 0    500
# 1    268
# Name: count, dtype: int64

# Answer of e:
# First 5 instances:
    Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  DiabetesPedigreeFunction  Age  Outcome
0            6      148             72             35        0  33.6                     0.627   50        1
1            1       85             66             29        0  26.6                     0.351   31        0
2            8      183             64              0        0  23.3                     0.672   32        1
3            1       89             66             23       94  28.1                     0.167   21        0
4            0      137             40             35      168  43.1                     2.288   33        1

Last 5 instances:
      Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  DiabetesPedigreeFunction  Age  Outcome
763           10      101             76             48      180  32.9                     0.171   63        0
764            2      122             70             27        0  36.8                     0.340   27        0
765            5      121             72             23      112  26.2                     0.245   30        0
766            1      126             60              0        0  30.1                     0.349   47        1
767            1       93             70             31        0  30.4                     0.315   23        0


# Answer of f: The dataset contains 1263 zero entries.

# answer of g
![DEMO](https://github.com/cseshahriar/pima-analysic/blob/main/histogram.png)

# answer of j Plot train and test accuracy
![DEMO](https://github.com/cseshahriar/pima-analysic/blob/main/test_accuracy_result.png)


# Download & Setup Instructions
## `Clone project: git clone https://github.com/cseshahriar/pima-analysic.git`
## `cd pima-analysis`
## `Create virtual environment: python3.8 im venv venv`
## `for linux venv activate: source venv/bin/activate`
## `for linux venv activate: venv\Scripts\activate`
## `pip3 install -r requirements.txt`
## `python3 pima.py # run python script`