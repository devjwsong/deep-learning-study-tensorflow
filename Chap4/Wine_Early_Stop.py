from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import  EarlyStopping

import pandas as pd
import numpy as np
import tensorflow as tf

seed = 0
np.random.seed(seed)
tf.set_random_seed(seed)

df_pre = pd.read_csv('../Dataset/wine.csv', header=None)
df = df_pre.sample(frac=0.15)
dataset = df.values
X = dataset[:, 0:12]
y = dataset[:, 12]

model = Sequential()
model.add(Dense(30, input_dim=12, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

early_stopping_callback = EarlyStopping(monitor='val_loss', patience=100)

model.fit(X, y, validation_split=0.2, epochs=2000, batch_size=500, callbacks=[early_stopping_callback])

print("\n Accuracy: %.4f" % (model.evaluate(X, y)[1]))
