import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt



data = pd.read_csv("cars.csv")
print(data.info())
print(f"Total Rows (Before NaN Removal): {len(data)}")
print(data.isna().sum())

