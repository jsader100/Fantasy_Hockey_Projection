import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def add_goal_proj(df):
    print(df.corr()['Goals/60'])

    X = df[
        ['Goals/60_x', 'Goals/60_y', 'Total Assists/60_x', 'Total Assists/60_y', 'IPP_x', 'IPP_y', 'SH%_x', 'ixG/60_x',
         'ixG/60_y', 'iSCF/60_x', 'iSCF/60_y', 'iHDCF/60_x', ]]
    y = df['Goals/60']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234567)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    print(f"R-squared: {r2}")

    goal_predict_df = pd.merge(pd.read_csv(f'defenseman2022.csv'), pd.read_csv(f'defenseman2023.csv'), on='Player', how='outer')
    goal_predict_df.dropna(inplace=True)
    X = goal_predict_df[['Goals/60_x', 'Goals/60_y', 'Total Assists/60_x', 'Total Assists/60_y', 'IPP_x', 'IPP_y', 'SH%_x', 'ixG/60_x',
         'ixG/60_y', 'iSCF/60_x', 'iSCF/60_y', 'iHDCF/60_x']]

    goal_predict_df['Goal_Proj'] = model.predict(X)

    goal_predict_df.to_csv('DF_projections.csv')



def add_assist_proj(df):
    print(df.corr()['Total Assists/60'])

    X = df[['Goals/60_x', 'Goals/60_y', 'Total Assists/60_x', 'Total Assists/60_y', 'IPP_x', 'IPP_y', 'SH%_x', 'ixG/60_x',
         'ixG/60_y', 'iSCF/60_x', 'iSCF/60_y', 'iHDCF/60_x']]

    y = df['Total Assists/60']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234567)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    print(f"R-squared: {r2}")

    df = pd.read_csv('DF_projections.csv')

    X = df[
        ['Goals/60_x', 'Goals/60_y', 'Total Assists/60_x', 'Total Assists/60_y', 'IPP_x', 'IPP_y', 'SH%_x', 'ixG/60_x',
         'ixG/60_y', 'iSCF/60_x', 'iSCF/60_y', 'iHDCF/60_x', ]]

    df['Assist_Proj'] = model.predict(X)

    df.to_csv('DF_projections.csv')

def add_shots_proj(df):
    print(df.corr()['Shots/60'])

    X = df[['Goals/60_x', 'Goals/60_y', 'Total Assists/60_x', 'Total Assists/60_y', 'IPP_x', 'IPP_y', 'SH%_x', 'ixG/60_x',
         'ixG/60_y', 'iSCF/60_x', 'iSCF/60_y', 'iHDCF/60_x']]

    y = df['Shots/60']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234567)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    print(f"R-squared: {r2}")

    df = pd.read_csv('DF_projections.csv')

    X = df[['Goals/60_x', 'Goals/60_y', 'Total Assists/60_x', 'Total Assists/60_y', 'IPP_x', 'IPP_y', 'SH%_x', 'ixG/60_x',
         'ixG/60_y', 'iSCF/60_x', 'iSCF/60_y', 'iHDCF/60_x', ]]

    df['Shots_Proj'] = model.predict(X)

    df.to_csv('DF_projections.csv')



def add_hits_proj(df):
    print(df.corr()['Hits/60'])

    X = df[['Hits/60_x', 'Hits/60_y']]

    y = df['Hits/60']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234567)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    print(f"R-squared: {r2}")

    df = pd.read_csv('DF_projections.csv')

    X = df[['Hits/60_x', 'Hits/60_y']]

    df['Hits_Proj'] = model.predict(X)

    df.to_csv('DF_projections.csv')


def add_blockedshots_proj(df):
    print(df.corr()['Shots Blocked/60'])

    X = df[['Shots Blocked/60_x', 'Shots Blocked/60_y']]

    y = df['Shots Blocked/60']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234567)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    print(f"R-squared: {r2}")

    df = pd.read_csv('DF_projections.csv')

    X = df[['Shots Blocked/60_x', 'Shots Blocked/60_y']]

    df['Shots_Blocked_Proj'] = model.predict(X)

    df.to_csv('DF_projections.csv')


year_end = 18
dfs = []


while year_end < 24:
    dfs.append(pd.read_csv(f'defenseman20{year_end}.csv'))
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

add_goal_proj(df)
add_assist_proj(df)
add_shots_proj(df)
add_hits_proj(df)
add_blockedshots_proj(df)