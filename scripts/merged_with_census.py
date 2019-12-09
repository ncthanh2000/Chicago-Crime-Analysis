import pandas as pd
df_crime = pd.read_csv('data/Chicago_Merged.csv')
df_census = pd.read_csv('data/Census.csv')

df = pd.merge(df_crime, df_census, on ='Community Area', how = 'outer')

df = df.drop("Unnamed: 0", axis = 1)

df.columns.values
df.to_csv('data/Census_merged.csv')