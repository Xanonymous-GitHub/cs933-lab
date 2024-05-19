import os

os.environ["KERAS_BACKEND"] = "jax"

from keras.api.layers import Conv2D, MaxPooling2D, Input, Flatten, Dense
from keras.api.models import Sequential


def run():
    model = Sequential([
        Input(shape=(4, 4, 1)),
        Conv2D(1, kernel_size=(3, 3), padding='same', activation='relu'),
        # MaxPooling2D((2, 2)),
        # Conv2D(2, (3, 3), padding='same', activation='relu'),
        MaxPooling2D((2, 2), strides=2),
        Flatten(),
        Dense(3, activation='relu'),
    ])
    model.summary()


if __name__ == '__main__':
    run()
