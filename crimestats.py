import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
from datetime import datetime 

pd.set_option('display.max_columns', None)
calldata = pd.read_csv("2022calls.csv")
column_names = list(calldata.columns)

print('Column Names Are: ', column_names)

print(calldata.info())

print('Number of calls per priority: \r')
print(calldata.groupby('Priority') ['Priority'].count())

print(calldata.groupby('Final Call Type') ['Final Call Type'].count())

print(calldata.groupby('Initial Call Type') ['Initial Call Type'].count())

print(calldata.groupby('Priority') ['Priority'].count())

plt.title('This Can Not Be Happening!:', fontsize = 15)
plt.xlabel('This one thing')
plt.ylabel('This other thing')

plt.plot(calldata['Initial Call Type'].count(), calldata['Precinct'])
plt.savefig("precinctcallcount.png")