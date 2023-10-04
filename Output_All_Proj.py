import pandas as pd

fwd_df = pd.read_csv('FWD_Total_Proj.csv')
df_df = pd.read_csv('DF_Total_Proj.csv')

df = pd.concat([fwd_df, df_df])

df.to_csv('Final_Total_Projections.csv')