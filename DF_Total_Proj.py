import pandas as pd

df = pd.read_csv('DF_projections.csv')
df = df[['Player', 'TOI_GP_Proj', 'Goal_Proj', 'Assist_Proj', 'Shots_Proj', 'Hits_Proj', 'Shots_Blocked_Proj']]

df['Total_Goals'] = (df.Goal_Proj/60) * df.TOI_GP_Proj * 80
df['Total_Assists'] = (df.Assist_Proj/60) * df.TOI_GP_Proj * 80
df['Total_Shots'] = (df.Shots_Proj/60) * df.TOI_GP_Proj * 80
df['Total_Hits'] = (df.Hits_Proj/60) * df.TOI_GP_Proj * 80
df['Total_Shots_Blocked'] = (df.Shots_Blocked_Proj/60) * df.TOI_GP_Proj * 80

df['Projected Fantasy Points'] = (df.Total_Goals*3) + (df.Total_Assists*1.5) + (df.Total_Shots*.25) + (df.Total_Hits*.25) + (df.Total_Shots_Blocked*.25)


df.to_csv('DF_Total_Proj.csv')