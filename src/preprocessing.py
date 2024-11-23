import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('../energy_usage.csv')

print(data.shape)

print(data.info())

print(data.describe())

print(data.isnull().sum())