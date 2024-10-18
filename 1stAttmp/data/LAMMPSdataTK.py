import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import os

"""
RECEIVE WRITE DATA FROM LAMMPS TO BE PROCESSED FOR WHATEVER USE
"""

def get_file(filename_):
    with open(filename_, "r") as file:
        file_content = file.readlines()
    df = pd.DataFrame(file_content, columns=['data'])
    return df


def get_structure(filename_,slices):
    data = get_file(filename_)[slices[0]:slices[1]].copy().reset_index(drop=True)
    data["data"] = data["data"].str.split('\s').apply(lambda x: list(filter(None, x)))
    data["atom id"] = data["data"].apply(lambda x: x[0]).astype(int)
    data["molecule id"] = data["data"].apply(lambda x: x[1]).astype(int)
    data["atom type"] = data["data"].apply(lambda x: x[2]).astype(int)
    data["charge"] = data["data"].apply(lambda x: x[3]).astype(float)
    data["x"] = data["data"].apply(lambda x: x[4]).astype(float)
    data["y"] = data["data"].apply(lambda x: x[5]).astype(float)
    data["z"] = data["data"].apply(lambda x: x[6]).astype(float)
    return data

def get_bonds(filename_,slices):
    data = get_file(filename_)[slices[0]:slices[1]].copy().reset_index(drop=True)
    data["data"] = data["data"].str.split('\s').apply(lambda x: list(filter(None, x)))
    data["bond id"] = data["data"].apply(lambda x: x[0]).astype(int)
    data["bond type"] = data["data"].apply(lambda x: x[1]).astype(int)
    data["atom1"] = data["data"].apply(lambda x: x[2]).astype(int)
    data["atom2"] = data["data"].apply(lambda x: x[3]).astype(int)
    return data


def get_angles(filename_, slices):
    angles = get_file(filename_)[slices[0]:slices[1]].copy().reset_index(drop=True)
    angles["data"] = angles["data"].str.split('\s').apply(lambda x: list(filter(None, x)))
    angles["angle id"] = angles["data"].apply(lambda x: x[0]).astype(int)
    angles["angle type"] = angles["data"].apply(lambda x: x[1]).astype(int)
    angles["atom1"] = angles["data"].apply(lambda x: x[2]).astype(int)
    angles["atom2"] = angles["data"].apply(lambda x: x[3]).astype(int)
    angles["atom3"] = angles["data"].apply(lambda x: x[4]).astype(int)
    return angles


def get_dihedrals(filename_,slices):
    dihedrals = get_file(filename_)[slices[0]:slices[1]].copy().reset_index(drop=True)
    dihedrals["data"] = dihedrals["data"].str.split('\s').apply(lambda x: list(filter(None, x)))
    dihedrals["dihedral id"] = dihedrals["data"].apply(lambda x: x[0]).astype(int)
    dihedrals["dihedral type"] = dihedrals["data"].apply(lambda x: x[1]).astype(int)
    dihedrals["atom1"] = dihedrals["data"].apply(lambda x: x[2]).astype(int)
    dihedrals["atom2"] = dihedrals["data"].apply(lambda x: x[3]).astype(int)
    dihedrals["atom3"] = dihedrals["data"].apply(lambda x: x[4]).astype(int)
    dihedrals["atom4"] = dihedrals["data"].apply(lambda x: x[5]).astype(int)
    return dihedrals


def get_impropers(filename_,slices):
    impropers = get_file(filename_)[slices[0]:slices[1]].copy().reset_index(drop=True)
    impropers["data"] = impropers["data"].str.split('\s').apply(lambda x: list(filter(None, x)))
    impropers["improper id"] = impropers["data"].apply(lambda x: x[0]).astype(int)
    impropers["improper type"] = impropers["data"].apply(lambda x: x[1]).astype(int)
    impropers["atom1"] = impropers["data"].apply(lambda x: x[2]).astype(int)
    impropers["atom2"] = impropers["data"].apply(lambda x: x[3]).astype(int)
    impropers["atom3"] = impropers["data"].apply(lambda x: x[4]).astype(int)
    impropers["atom4"] = impropers["data"].apply(lambda x: x[5]).astype(int)
    return impropers