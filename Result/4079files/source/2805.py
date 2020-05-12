"""
CLI for training feedforward neural networks with prepared data.
Trying classification approach.

Unfortunately, this is quickly hacked together.
"""

import argparse
import sys
import os
import datetime
import socket
from math import sqrt

import tensorflow.contrib.keras as keras
import numpy as np


parser = argparse.ArgumentParser(description="Train a fully-connected neural network.")
parser.add_argument("network_depth", type=int)
parser.add_argument("network_width", type=int)
parser.add_argument("leg", type=int)
parser.add_argument("-op", "--optimizer", choices=["Adam", "SGD"], default="Adam")
parser.add_argument("-bs", "--batch_size", type=int, default=32)
parser.add_argument("-e", "--epochs", type=int, default=100)
parser.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("-s", "--save", type=str, help="Specify save path for trained model.")
parser.add_argument("-a", "--activation", default="relu")
parser.add_argument("--reduce_lr", action="store_true", help="If validation loss stagnates, reduce lr by sqrt(0.1).")
parser.add_argument("--early_stopping", action="store_true")
parser.add_argument("--shuffle_off", action="store_false", help="Don't shuffle training data.")
parser.add_argument("--reduce_width", action="store_true", help="Linearly reduce hidden layers' width.")
#parser.add_argument("--days", type=int, default=1, help="How many days to predict into the future.")


def classification_model(depth, width, input_length=7, categories=3,
                         activation="relu", reduce_width=False):
    inputs = keras.layers.Input(shape=(input_length,), name="input")
    layer = input
    if reduce_width:
        widths = np.linspace(width, categories, depth + 1).round().astype(int)[:-1]
        assert len(widths) == depth
    else:
        widths = [width] * depth
    for w in widths:
        layer = keras.layers.Dense(w, activation=activation)(layer)
    outputs = keras.layers.Dense(categories, activation="softmax", name="output")(layer)
    model = keras.models.Model(inputs=inputs, outputs=outputs)
    return model


def train(args):
    # Check if month number is valid.
    if args.leg not in range(1, 7):
        print("leg argument has to be an integer between 1 and 6", file=sys.stderr)
        sys.exit(1)
    input_length = 7
    model = classification_model(args.depth, args.width, input_length=input_length,
                                 activation=args.activation, reduce_width=args.reduce_width)
    model.compile(args.optimizer, "categorical_crossentropy", metrics=["accuracy"])
    callbacks = []
    if args.save:
        now = datetime.datetime.now()
        name = "{}_{}_depth{}_width{}_leg{}".format(
            now.strftime("%Y%m%d%H%M%S"),
            socket.gethostname(),
            args.network_depth,
            args.network_width,
            args.leg)
        callbacks.append(keras.callbacks.CSVLogger(os.path.join(args.save, name + ".csv")))
    if args.reduce_lr:
        callbacks.append(keras.callbacks.ReduceLROnPlateau(factor=sqrt(0.1), patience=20, min_lr=0.0001, verbose=1))
    if args.early_stopping:
        callbacks.append(keras.callbacks.EarlyStopping(patience=22, verbose=1))
    #model.fit(x_train, y_train, args.batch_size, args.epochs, verbose=0 if args.quiet else 2,
    #          validation_data=(x_val, y_val), callbacks=callbacks, shuffle=args.shuffle_off)
    if args.save:
        try:
            model.save_weights(os.path.join(args.save, name + ".h5"))
        except FileNotFoundError as e:
            print("Could not save the model.", str(e), file=sys.stderr)


if __name__ == "__main__":
    args = parser.parse_args()
    train(args)
