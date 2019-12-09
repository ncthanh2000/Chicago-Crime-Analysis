import pandas as pd

df = pd.read_csv('data/Chicago_Crimes_Raw.csv')

# Convert the string dates to Pandas timestamps
df['Date'] = pd.to_datetime(df['Date'])

# Select only data from the last 5 years
pf = df[df.Date > pd.Timestamp('2015-01-01')]

# Take a sample of about 25,000 crimes
final = pf.sample(frac=0.02)

final.to_csv('data/Chicago_Crimes_Processed.csv')

# Select only data from the last 10 years
pf = df[df.Date > pd.Timestamp('2010-01-01')]

# Take a sample of about 25,000 crimes
final = pf.sample(frac=0.02)

final.to_csv('data/Chicago_Crimes_Processed_2011.csv')