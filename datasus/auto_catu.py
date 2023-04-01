from full_catu import db5_to_dataframe
from os import listdir
import subprocess
import sys

for file_name in listdir("./PASP/"):
    filename = f"./PASP/{file_name}"
    print(filename)
    #subprocess.Popen(["./blast-dbf", filename, "current.dbf"]).wait()
    subprocess.Popen(["/usr/bin/python3", "full_catu.py", filename]).wait()
    '''try:
        db5_to_dataframe(save_name=file_name)
    except Exception as e:
        print(e)'''