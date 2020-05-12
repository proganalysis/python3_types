"""
vix-term-structure.utils

Some helper functions for evaluating the data.

:copyright: (c) 2017 Thomas Leyh
"""

import datetime
import os
from collections import namedtuple

import pandas as pd
import numpy as np


ModelParameters = namedtuple("ModelParameters", ("datetime", "hostname", "depth", "width", "days",
                                                 "dropout", "optimizer", "lr", "normalized"))
ModelParametersOld = namedtuple("ModelParameters", ("datetime", "hostname", "depth", "width",
                                                    "dropout", "optimizer", "lr", "normalized"))
ModelParametersMonthwise = namedtuple("ModelParameters", ("datetime", "hostname", "depth", "width", "month",
                                                          "dropout", "optimizer", "lr"))


################################################################
# This is for parsing old models without variable days.
################################################################


def parse_model_repr_old(repr_str: str):
    """
    Parse the basename of a model file to get its parameters
    returned as tuple.
    """
    repr_list = repr_str.split("_")
    assert len(repr_list) >= 7, "String does not match representation format."
    repr_dict = dict()
    repr_dict["datetime"] = datetime.datetime.strptime(repr_list[0], "%Y%m%d%H%M%S")
    repr_dict["hostname"] = repr_list[1]
    repr_dict["depth"] = int(repr_list[2].lstrip("depth"))
    repr_dict["width"] = int(repr_list[3].lstrip("width"))
    repr_dict["dropout"] = float(repr_list[4].lstrip("dropout"))
    repr_dict["optimizer"] = repr_list[5].lstrip("optim")
    repr_dict["lr"] = float(repr_list[6].lstrip("lr"))
    repr_dict["normalized"] = True if len(repr_list) >= 8 and repr_list[7] == "normalized" else False
    return ModelParametersOld(**repr_dict)


def parse_whole_directory_old(path: str):
    directory, _, files = next(os.walk(path))
    csv_files = tuple(file for file in files if os.path.splitext(file)[1] == ".csv")
    stats = [(parse_model_repr_old(os.path.splitext(file)[0]),
              pd.read_csv(os.path.join(directory, file), header=0, index_col=0,
                          dtype={"epoch": int, "loss": np.float32, "val_loss": np.float32,
                                 "denorm_mse": np.float32, "val_denorm_mse": np.float32}))
             for file in csv_files]
    parameters, stats_data = zip(*stats)
    for d in stats_data:
        if len(d.columns) == 2:
            use_this_as_columns = d.columns
            break
    for d in stats_data:
        if len(d.columns) == 4:
            d.drop(["loss", "val_loss"], axis=1, inplace=True)
            d.columns = use_this_as_columns
    dataframe = pd.concat(stats_data, keys=[(p.depth, p.width, p.normalized, p.datetime) for p in parameters],
                          names=["depth", "width", "normalized", "datetime"])
    dataframe.sort_index(inplace=True)
    return dataframe


################################################################
# This is for newer models where one can choose future days.
################################################################


def parse_model_repr(repr_str: str):
    """
    Parse the basename of a model file to get its parameters
    returned as tuple.
    """
    repr_list = repr_str.split("_")
    assert len(repr_list) >= 8, "String does not match representation format."
    repr_dict = dict()
    repr_dict["datetime"] = datetime.datetime.strptime(repr_list[0], "%Y%m%d%H%M%S")
    repr_dict["hostname"] = repr_list[1]
    repr_dict["depth"] = int(repr_list[2].lstrip("depth"))
    repr_dict["width"] = int(repr_list[3].lstrip("width"))
    repr_dict["days"] = int(repr_list[4].lstrip("days"))
    repr_dict["dropout"] = float(repr_list[5].lstrip("dropout"))
    repr_dict["optimizer"] = repr_list[6].lstrip("optim")
    repr_dict["lr"] = float(repr_list[7].lstrip("lr"))
    repr_dict["normalized"] = True if len(repr_list) >= 9 and repr_list[8] == "normalized" else False
    return ModelParameters(**repr_dict)


def parse_whole_directory(path: str):
    directory, _, files = next(os.walk(path))
    csv_files = tuple(file for file in files if os.path.splitext(file)[1] == ".csv")
    stats = [(parse_model_repr(os.path.splitext(file)[0]),
              pd.read_csv(os.path.join(directory, file), header=0, index_col=0,
                          dtype={"epoch": int, "loss": np.float32, "val_loss": np.float32,
                                 "denorm_mse": np.float32, "val_denorm_mse": np.float32}))
             for file in csv_files]
    parameters, stats_data = zip(*stats)
    for d in stats_data:
        if len(d.columns) == 2:
            use_this_as_columns = d.columns
            break
    for d in stats_data:
        if len(d.columns) == 4:
            d.drop(["loss", "val_loss"], axis=1, inplace=True)
            d.columns = use_this_as_columns
    dataframe = pd.concat(stats_data, keys=[(p.depth, p.width, p.normalized, p.datetime) for p in parameters],
                          names=["depth", "width", "normalized", "datetime"])
    dataframe.sort_index(inplace=True)
    return dataframe


################################################################
# And this is for the new monthwise data representation.
################################################################


def parse_model_repr_monthwise(repr_str: str):
    """
    Parse the basename of a model file to get its parameters
    returned as tuple.
    """
    repr_list = repr_str.split("_")
    assert len(repr_list) == 8, "String does not match representation format."
    repr_dict = dict()
    repr_dict["datetime"] = datetime.datetime.strptime(repr_list[0], "%Y%m%d%H%M%S")
    repr_dict["hostname"] = repr_list[1]
    repr_dict["depth"] = int(repr_list[2].lstrip("depth"))
    repr_dict["width"] = int(repr_list[3].lstrip("width"))
    repr_dict["month"] = int(repr_list[4].lstrip("month"))
    repr_dict["dropout"] = float(repr_list[5].lstrip("dropout"))
    repr_dict["optimizer"] = repr_list[6].lstrip("optim")
    repr_dict["lr"] = float(repr_list[7].lstrip("lr"))
    return ModelParametersMonthwise(**repr_dict)


def parse_whole_directory_monthwise(path: str):
    directory, _, files = next(os.walk(path))
    csv_files = tuple(file for file in files if os.path.splitext(file)[1] == ".csv")
    stats = [(parse_model_repr_monthwise(os.path.splitext(file)[0]),
              pd.read_csv(os.path.join(directory, file), header=0, index_col=0))
             for file in csv_files]
    parameters, stats_data = zip(*stats)
    dataframe = pd.concat(stats_data, keys=[(p.depth, p.width, p.month, p.datetime) for p in parameters],
                          names=["depth", "width", "month", "datetime"])
    dataframe.sort_index(inplace=True)
    return dataframe
