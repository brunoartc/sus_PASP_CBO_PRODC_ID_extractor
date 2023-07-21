import subprocess
import sys

from simpledbf import Dbf5
import pickle
import pandas as pd

procedimentos = [
"0101040024",
"0202010473",
"0214010015",
"0301100039",
"0202010074",
"0202010759",
"0214010031",
"0202010040",
"0202010317",
"0211060100",
"0208040080",
"0202010279",
"0202010287",
"0202010473",
"0214010015",
"0301100039",
"0202010074",
"0202010759",
"0214010031",
"0202010040",
"0202010317",
"0211060100",
"0208040080",
"0202010279",
"0202010287",
"0202010295",
"0101010036",
"0101010010",
"0309050111",
"0309050120",
"0101050062",
"0309050227",
"0101010060",
"0101050038",
"0101050100",
"0101050119",
"0101050127",
"0309050138",
"0101050135",
"0309050146",
"0309050154",
"0309050197",
"0309050162",
"0101050097",
"0309050219",
"0309050014",
"0309050022",
"0101050070",
"0101050089",
"0309050073",
"0309050081",
"0309050200",
"0309050090",
"0309050103",
"0101010052",
"0101050020",
"0309050189",
"0101050143",
"0309050065",
"0101010079",
"0101050046",
"0301010064",
"0301010072",
"0301010030",
"0301010048"
]



def db5_to_dataframe(filename_dbf = "current.dbf", save_name="output.xlsx"):


    pandas_df = None


    dbf = Dbf5(filename_dbf, codec='iso8859_15')

    print(dbf.mem())

    for df in dbf.to_dataframe(chunksize=1000000):
        if pandas_df is None:
            pandas_df = df.drop(columns = ['PA_CODUNI', 'PA_GESTAO', 'PA_CONDIC', 'PA_REGCT',
        'PA_INCOUT', 'PA_TIPPRE', 'PA_MN_IND',# 'PA_INCURG'
        'PA_CNPJCPF', 'PA_CNPJMNT', 'PA_CNPJ_CC', #'PA_MVMR',
            'PA_TPFIN', 'PA_SUBFIN', 'PA_NIVCPL', 'PA_DOCORIG',
        'PA_AUTORIZ', 'PA_CNSMED', 'PA_MOTSAI', 'PA_OBITO',
        'PA_ENCERR', 'PA_PERMAN', 'PA_ALTA', 'PA_TRANSF', 'PA_CIDPRI',
        'PA_CIDSEC', 'PA_CIDCAS', 'PA_CATEND', 'PA_IDADE', 'IDADEMIN',
        'IDADEMAX', 'PA_FLIDADE', 'PA_SEXO', 'PA_RACACOR', 'PA_MUNPCN',
        'PA_QTDPRO', 'PA_QTDAPR', 'PA_VALPRO', 'PA_VALAPR', 'PA_UFDIF',
        'PA_MNDIF', 'PA_DIF_VAL', 'NU_VPA_TOT', 'NU_PA_TOT', 'PA_INDICA',
        'PA_CODOCO', 'PA_FLQT', 'PA_FLER', 'PA_ETNIA', 'PA_VL_CF', 'PA_VL_CL',
        'PA_VL_INC', 'PA_SRV_C'], errors='ignore')
        else:
            pandas_df = pd.concat([pandas_df, df.drop(columns = ['PA_CODUNI', 'PA_GESTAO', 'PA_CONDIC', 'PA_REGCT',
            'PA_INCOUT', 'PA_TIPPRE', 'PA_MN_IND',#, 'PA_INCURG'
            'PA_CNPJCPF', 'PA_CNPJMNT', 'PA_CNPJ_CC', #'PA_MVMR',
                'PA_TPFIN', 'PA_SUBFIN', 'PA_NIVCPL', 'PA_DOCORIG',
            'PA_AUTORIZ', 'PA_CNSMED', 'PA_MOTSAI', 'PA_OBITO',
            'PA_ENCERR', 'PA_PERMAN', 'PA_ALTA', 'PA_TRANSF', 'PA_CIDPRI',
            'PA_CIDSEC', 'PA_CIDCAS', 'PA_CATEND', 'PA_IDADE', 'IDADEMIN',
            'IDADEMAX', 'PA_FLIDADE', 'PA_SEXO', 'PA_RACACOR', 'PA_MUNPCN',
            'PA_QTDPRO', 'PA_QTDAPR', 'PA_VALPRO', 'PA_VALAPR', 'PA_UFDIF',
            'PA_MNDIF', 'PA_DIF_VAL', 'NU_VPA_TOT', 'NU_PA_TOT', 'PA_INDICA',
            'PA_CODOCO', 'PA_FLQT', 'PA_FLER', 'PA_ETNIA', 'PA_VL_CF', 'PA_VL_CL',
            'PA_VL_INC', 'PA_SRV_C'], errors='ignore')])
            print(";", end="")

    del dbf

    pickle.dump( pandas_df, open( "save.pandas", "wb" ) )


    df_no = pandas_df[pandas_df['PA_CBOCOD'] == "225155"]

    #df_pivot = pandas_df[(pandas_df['PA_PROC_ID'] == "0101040024") | (pandas_df['PA_PROC_ID'] == "0101040024") | (pandas_df['PA_PROC_ID'] == "0202010074") | (pandas_df['PA_PROC_ID'] == "0202010473") | (pandas_df['PA_PROC_ID'] == "0202010759") | (pandas_df['PA_PROC_ID'] == "0214010015") | (pandas_df['PA_PROC_ID'] == "0214010031") | (pandas_df['PA_PROC_ID'] == "0202010040") | (pandas_df['PA_PROC_ID'] == "0202010317") | (pandas_df['PA_PROC_ID'] == "0211060100") | (pandas_df['PA_PROC_ID'] == "0208040080") | (pandas_df['PA_PROC_ID'] == "0202010279") | (pandas_df['PA_PROC_ID'] == "0202010287") | (pandas_df['PA_PROC_ID'] == "0202010295") | (pandas_df['PA_PROC_ID'] == "0101010036") | (pandas_df['PA_PROC_ID'] == "0101010010")]

    df_pivot = pandas_df[(pandas_df['PA_PROC_ID'].isin(procedimentos))].drop(columns=['PA_CBOCOD', 'PA_NAT_JUR', 'PA_INENE'], errors='ignore')

    #df_pivot["PA_PROC_ID-PA_UFMUN"] = df_pivot["PA_PROC_ID"] + df_pivot["PA_UFMUN"]

    #df_pivot.head()

    df_pivot_sum = pandas_df.pivot_table(index = ['PA_PROC_ID', 'PA_UFMUN', 'PA_INCURG', 'PA_TPUPS'], aggfunc ='size')

    df_pivot_sum.to_excel(f"output/PA_PROC_ID_{save_name}", engine='xlsxwriter') 

    #no need to work on this again
    df_no.to_excel(f"output/PA_CBOCOD_{save_name}", engine='xlsxwriter') 


def main():


    filename = sys.argv[1]

    save_name = filename.split("/")[2] + ".xlsx"

    subprocess.Popen(["./blast-dbf", filename, "current.dbf"]).wait()
    db5_to_dataframe(save_name=save_name)


if __name__ == "__main__":
   main()