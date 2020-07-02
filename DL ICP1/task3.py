
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers.core import Dense

# load dataset
import pandas as pd
dataset = pd.read_csv("breastcancer.csv")


X = dataset.iloc[:, 2:32].values
y = dataset.iloc[:, 1].values

print(dataset.iloc[:, 1].value_counts())

# Encoding categorical data
labelencoder_X_1 = LabelEncoder()
# Fit label encoder and return encoded labels M=1, B=0
y = labelencoder_X_1.fit_transform(y)

sc = StandardScaler()
X_scaled = sc.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.25, random_state=0)


my_first_nn = Sequential()  # create model
my_first_nn.add(Dense(20, input_dim=30, activation='relu'))  # hidden layer
my_first_nn.add(Dense(1, activation='sigmoid'))  # output layer
my_first_nn.compile(loss='binary_crossentropy',
                    optimizer='adam', metrics=['accuracy'])
my_first_nn_fitted = my_first_nn.fit(X_train, y_train, epochs=100, verbose=0,
                                     initial_epoch=0)

print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, y_test))
