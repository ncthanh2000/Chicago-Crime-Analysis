import pandas as pd
df_crime = pd.read_csv('data/Chicago_Crimes_Processed.csv')
df_econ = pd.read_csv('data/Chicago_Socioeconomic_Indicators.csv')
df_census = pd.read_csv('data/Census.csv')
df_econ.rename(columns = {'Community Area Number': 'Community Area'}, inplace = True)
df = pd.merge(df_crime, df_econ, on ='Community Area', how = 'outer')
df = df.drop("Unnamed: 0", axis = 1)
df.to_csv('data/Chicago_Merged.csv')

