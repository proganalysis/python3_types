"""
vix-term-structure.models

In this file I will define some models (starting with some very simple ones)
to see what captures the existing data the best.

:copyright: (c) 2017 Thomas Leyh
"""

from typing import Optional

import tensorflow.contrib.keras as keras
import numpy as np


def selu(x):
    """Scaled Exponential Linear Unit. (Klambauer et al., 2017)
    # Arguments
        x: A tensor or variable to compute the activation function for.
    # References
        - [Self-Normalizing Neural Networks](https://arxiv.org/abs/1706.02515)
        - Taken from keras.activations (selu got included on Jun 14 2017)
    """
    alpha = 1.6732632423543772848170429916717
    scale = 1.0507009873554804934193349852946
    return scale * keras.backend.elu(x, alpha)


def term_structure_to_spread_price(hidden_layers, hidden_layer_width, dropout=None,
                                   input_data_length=9, output_data_length=6,
                                   activation_function="relu"):
    """
    Simple feed-forward network for mapping some input data to some output data.
    :param hidden_layers: Defines depth of network.
    :param hidden_layer_width: Defines width of hidden layers.
    :param dropout: If you want to use dropout 0.5 is a nice value.
    :param input_data_length: How many values does one sample hold?
    :param output_data_length: How many values does one target sample hold?
    :param activation_function: Activation function for hidden layers; see keras.activations
    :return: A keras model defining the network.
    """
    if activation_function == "selu":
        activation = selu
    else:
        activation = getattr(keras.activations, activation_function)
    input = keras.layers.Input(shape=(input_data_length,), name="input")
    layer = input
    for _ in range(hidden_layers):
        layer = keras.layers.Dense(hidden_layer_width, activation=activation)(layer)
        if dropout:
            layer = keras.layers.Dropout(rate=dropout)(layer)
    output = keras.layers.Dense(output_data_length, name="output")(layer)
    model = keras.models.Model(inputs=input, outputs=output)
    return model


def mask_output(x):
    x = keras.backend.cast(keras.backend.greater(x[:, -1], 0.0), "int32")
    ones = keras.backend.ones_like(keras.backend.one_hot(x, 5), dtype="int32")
    x = keras.backend.concatenate([keras.backend.expand_dims(x, axis=1), ones])
    return keras.backend.cast(x, "float32")


def term_structure_to_spread_price_v2(hidden_layers, hidden_layer_width, dropout=None,
                                      input_data_length=9, output_data_length=6,
                                      activation_function="relu"):
    """
    The same as above but prediction is always zero for first spread price when
    time until expiration is 0. Time until expiration is always the last dimension
    of input vector.
    """
    if activation_function == "selu":
        activation = selu
    else:
        activation = getattr(keras.activations, activation_function)
    input = keras.layers.Input(shape=(input_data_length,), name="input")
    layer = input
    for _ in range(hidden_layers):
        layer = keras.layers.Dense(hidden_layer_width, activation=activation)(layer)
        if dropout:
            layer = keras.layers.Dropout(rate=dropout)(layer)
    output = keras.layers.Dense(output_data_length, name="output")(layer)
    mask = keras.layers.Lambda(mask_output)(input)
    output = keras.layers.Multiply()([mask, output])
    model = keras.models.Model(inputs=input, outputs=output)
    return model


def term_structure_to_single_spread_price(hidden_layers, hidden_layer_width, dropout=None,
                                          input_data_length=8, activation_function="relu",
                                          reduce_width=False):
    """
    Predict only a single spread price instead of the whole set like above.
    """
    if activation_function == "selu":
        activation = selu
    else:
        activation = getattr(keras.activations, activation_function)
    input = keras.layers.Input(shape=(input_data_length,), name="input")
    layer = input
    if reduce_width:
        widths = np.linspace(hidden_layer_width, 1, hidden_layers + 1).round().astype(int)[:-1]
        assert len(widths) == hidden_layers
    else:
        widths = [hidden_layer_width] * hidden_layers
    for idx, width in enumerate(widths):
        if activation_function == "selu":  # Use gaussian initialization in this case.
            if idx == 0:
                initializer = keras.initializers.RandomNormal(0.0, np.sqrt(1.0 / (input_data_length / 2)))
            else:
                initializer = keras.initializers.RandomNormal(0.0, np.sqrt(1.0 / widths[idx - 1]))
            layer = keras.layers.Dense(width, activation=activation,
                                       kernel_initializer=initializer)(layer)
        else:
            layer = keras.layers.Dense(width, activation=activation)(layer)
        if dropout:
            if activation_function == "selu":
                raise RuntimeError("Do not use dropout together with SELUs.")
            else:
                layer = keras.layers.Dropout(rate=dropout)(layer)
    if activation_function == "selu":
        initializer = keras.initializers.RandomNormal(0.0, np.sqrt(1.0 / widths[-1]))
        output = keras.layers.Dense(1, name="output", kernel_initializer=initializer)(layer)
    else:
        output = keras.layers.Dense(1, name="output")(layer)
    model = keras.models.Model(inputs=input, outputs=output)
    return model


################################################################
# This is some old stuff. Try the functions above.
################################################################

def naive_fully_connected(hidden_layers: int, past_days: int, days_to_future: int):
    """
    This is a simple network consisting of a variable number of fully connected layers.
    It doesn't produce the final output (investment recommendations) but just tries to
    generate a future term structure. 
    
    "Isn't this useless" you might ask?
    
    Well, at the moment I still lack some data and expertise but this naive approach seems
    to be a good idea to investigate the temporal dependencies of the data in general.
    The question I want to answer here is: How many days do I have to look into the past
    to get a glimpse of the future?
    
    Though the main problem here is will be certainly overfitting. There is not much data,
    its not augmented and the model itself if because of its verbosity prone to overfitting.
    I'll try to counter this with dropout regularization.
    
    :param hidden_layers: Number of hidden layers.
    :param past_days: How many days to look into the past.
    :param days_to_future: For which day in the future to make the prediction.
    :return: A Keras model with these inputs (one vector for each day):
                - The VIX indices of ``past_days``
                - The term structures of ``past_days``
             The output is a term structure in ``days_to_future``.
             The model is not yet compiled.
    """
    initializer = keras.initializers.glorot_normal()
    activation = keras.activations.tanh
    input = keras.layers.Input(shape=(past_days, 9), name="input")
    hidden = keras.layers.Flatten()(input)
    for _ in range(hidden_layers):
        hidden = keras.layers.Dense(9 * past_days, activation=activation, kernel_initializer=initializer)(hidden)
        hidden = keras.layers.Dropout(rate=0.5)(hidden)
    output = keras.layers.Dense(8, activation=activation, name="output", kernel_initializer=initializer)(hidden)
    model = keras.models.Model(inputs=input, outputs=output)
    return model


def spread_price_prediction(hidden_layers: int, data_length: int, dropout: Optional[float]):
    initializer = keras.initializers.glorot_uniform()
    activation = keras.activations.relu
    input = keras.layers.Input(shape=(data_length,), name="input")
    hidden = input
    for _ in range(hidden_layers):
        hidden = keras.layers.Dense(data_length, activation=activation, kernel_initializer=initializer)(hidden)
        if dropout:
            hidden = keras.layers.Dropout(rate=dropout)(hidden)
    output = keras.layers.Dense(data_length, activation=activation, name="output", kernel_initializer=initializer)(hidden)
    model = keras.models.Model(inputs=input, outputs=output)
    return model
