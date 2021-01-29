import pandas as pd
import csv
import matplotlib.pyplot as plt

df = pd.read_csv('Bigramsdf.csv')
df2 = pd.read_csv('wordFreq.csv')

data_set = df.groupby('Appearance')['count'].sum()
data_set2 = df2.groupby('Word1')['Frequency1'].sum()

df = pd.DataFrame(data_set)
df2 = pd.DataFrame(data_set2)

print(df.sort_values(by=['count'], ascending=False)[:10])
print(df2.sort_values(by=['Frequency1'], ascending=False)[:10])



df2.sort_values(by=['Frequency1'], ascending=False)[:10].plot(kind='bar')
plt.ylabel('Frequency')
plt.xlabel('word Frequency')
plt.xticks(rotation=45)
plt.title('Overall Frequency when Top word')

#
plt.show()
