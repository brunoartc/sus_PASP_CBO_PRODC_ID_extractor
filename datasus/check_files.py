from ftplib import FTP
from os import listdir

ftp = FTP('ftp.datasus.gov.br')
ftp.login()

ftp.cwd('/dissemin/publicos/SIASUS/200801_/Dados/')

filtered = [x.split(".")[0] for x in filter(lambda file_name: "PASP" in file_name, ftp.nlst())]

output = listdir("./output/")

for i in filtered:
    if i not in "".join(output):
        print(i)