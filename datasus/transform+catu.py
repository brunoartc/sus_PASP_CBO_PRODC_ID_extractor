import pandas as pd
import pickle

df = pd.read_pickle('dbf.df')


print(df.columns)

df_no = df.drop(columns = ['PA_CODUNI', 'PA_GESTAO', 'PA_CONDIC', 'PA_REGCT',
       'PA_INCOUT', 'PA_INCURG', 'PA_TIPPRE', 'PA_MN_IND',
       'PA_CNPJCPF', 'PA_CNPJMNT', 'PA_CNPJ_CC', #'PA_MVMR',
        'PA_TPFIN', 'PA_SUBFIN', 'PA_NIVCPL', 'PA_DOCORIG',
       'PA_AUTORIZ', 'PA_CNSMED', 'PA_MOTSAI', 'PA_OBITO',
       'PA_ENCERR', 'PA_PERMAN', 'PA_ALTA', 'PA_TRANSF', 'PA_CIDPRI',
       'PA_CIDSEC', 'PA_CIDCAS', 'PA_CATEND', 'PA_IDADE', 'IDADEMIN',
       'IDADEMAX', 'PA_FLIDADE', 'PA_SEXO', 'PA_RACACOR', 'PA_MUNPCN',
       'PA_QTDPRO', 'PA_QTDAPR', 'PA_VALPRO', 'PA_VALAPR', 'PA_UFDIF',
       'PA_MNDIF', 'PA_DIF_VAL', 'NU_VPA_TOT', 'NU_PA_TOT', 'PA_INDICA',
       'PA_CODOCO', 'PA_FLQT', 'PA_FLER', 'PA_ETNIA', 'PA_VL_CF', 'PA_VL_CL',
       'PA_VL_INC', 'PA_SRV_C'])[df['PA_CBOCOD'] == "225155"]

print(df_no.head())

fileObj = open('dbf_small.df', 'wb')
pickle.dump(df_no,fileObj)
fileObj.close()

dataframe_cllean_e = df_no.applymap(lambda x: x.encode('unicode_escape').
                 decode('utf-8') if isinstance(x, str) else x)


dataframe_cllean_e.to_excel("output.xlsx", engine='xlsxwriter') 