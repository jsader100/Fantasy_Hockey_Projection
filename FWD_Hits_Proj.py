import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


year_end = 18
dfs = []


while year_end < 24:
    dfs.append(pd.read_csv(f'forwards20{year_end}.csv'))
    year_end += 1

merged_dfs = []

for i in range(len(dfs)-2):
    df = pd.merge(dfs[i], dfs[i+1], on='Player', how='outer')
    df = pd.merge(df, dfs[i+2], on='Player', how='outer')
    merged_dfs.append(df)

df = merged_dfs[0]
for i in range(1, len(merged_dfs)):
    df = pd.concat([df, merged_dfs[i]])

df.dropna(inplace=True)

#print correlation rates
print(df.corr()['Hits/60'])

X = df[['Hits/60_x', 'Hits/60_y']]

y = df['Hits/60']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234567)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
print(f"R-squared: {r2}")

df = pd.read_csv('FWD_projections.csv')

X = df[['Hits/60_x', 'Hits/60_y']]

df['Hits_Proj'] = model.predict(X)

df.to_csv('FWD_projections.csv')
