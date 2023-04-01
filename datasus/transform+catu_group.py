import pandas as pd
import pickle

df = pd.read_pickle('save.pandas')


#print(df.columns)

df_pivot = df.pivot_table(index = ['PA_PROC_ID'], aggfunc ='size')

print()

df_pivot.to_excel("PA_PROC_ID.xlsx")

