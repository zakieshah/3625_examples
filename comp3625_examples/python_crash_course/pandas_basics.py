import pandas as pd

df = pd.read_csv('data.csv')

print(df)
df['Duration'] /= 60
print(df)

# access by index
print(df.loc[1, 'Duration'])

# keep all but the calories column
df_new = df.drop('Calories', axis=1)
print(df_new)
df_new2 = df[['Duration', 'Pulse']]
df_new3 = df['Maxpulse']

# create a new column that shows where duration is > 50
df['duration>50'] = df['Duration'] > 50
# or, using a lambda:
df['duration>50'] = df['Duration'].apply(lambda x: x>50)
print(df)