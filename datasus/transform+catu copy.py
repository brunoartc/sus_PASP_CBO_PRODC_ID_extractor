import pandas as pd
import pickle

df = pd.read_pickle('dbf.df')


print(df.columns)

df_no = df[df['PA_CBOCOD'] == "225155"]

print(df_no.head())

fileObj = open('dbf_small.df', 'wb')
pickle.dump(df_no,fileObj)
fileObj.close()

dataframe_cllean_e = df_no.applymap(lambda x: x.encode('unicode_escape').
                 decode('utf-8') if isinstance(x, str) else x)


dataframe_cllean_e.to_excel("output.xlsx", engine='xlsxwriter') 