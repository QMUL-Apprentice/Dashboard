import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    '/Users/arnavram/IOT451U Assignment 3/Dashboard/data-set/air-quality-london.xlsx - Monthly averages.csv',
    na_values = ['NO DATA', 'N/A', 'MISSING', 'NaN', 'NA']
    )
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes = axes.flatten()

print(df)