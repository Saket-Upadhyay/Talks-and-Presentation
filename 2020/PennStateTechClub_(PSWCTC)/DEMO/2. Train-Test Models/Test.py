
import time
from os import system as sys
import csv
import os
import numpy as np
import pickle
import pandas as pd
import subprocess

dlls=[]

def ExtractPerms(ExeName=None,ExePath=None):

    print("GOT PATH = "+ExePath)
    with open('dataret.csv') as csv_file:
        CSVREADER = csv.DictReader(csv_file)
        fieldnames = CSVREADER.fieldnames
        csv_master_dict = dict.fromkeys(fieldnames, 0)

        dlls = []
        path = str(ExePath)+str(ExeName)
        out = subprocess.Popen(['rabin2', '-i', path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        stdout = stdout.split()
        listr = stdout

        for i in range(0, len(listr)):
            listr[i] = str(listr[i])

        for i in range(0, len(listr)):
            listr[i] = listr[i][2:-1]

        for i in range(0, len(listr)):
            temp = listr[i]
            temp = temp.lower()
            listr[i] = temp

        for element in listr:
            if '.dll' in element or '.DLL' in element:
                if element not in dlls:
                    dlls.append(element)

        try:
            csv_master_dict = dict.fromkeys(fieldnames, 0)
            csv_master_dict['NAME'] = ExeName
            csv_master_dict['CLASS'] = 2
            for dll in dlls:
                if dll in fieldnames:
                    csv_master_dict[dll] = 1
            with open('dataret.csv', 'a') as csv_dump:
                CSVwriter = csv.DictWriter(csv_dump, fieldnames=fieldnames)
                CSVwriter.writerow(csv_master_dict)
            print('\n')
        except Exception:
            print("Error\n")
        
    return 1



if __name__=='__main__':
    os.system("cat data.bak > dataret.csv")
    DIR2 = "./test/"
    ExtractPerms(ExePath=DIR2,ExeName="m.ex_")

    file = pd.read_csv("dataret.csv")
    coulmnNames = file.iloc[1:1, 1:].columns
    FeatureNames = list(coulmnNames[1:-1])
    X = file[FeatureNames]
    X = np.asarray(X)
    print(X)
    # pickle.dump(X,open("malwareX",'wb'))
    clf = pickle.load(open("LReg/LOGREGRESSION.model", 'rb'))
    predictr,proba= clf.predict(X), clf.predict_proba(X)
    probam=np.round(proba[0][1], 3) * 100
    probas=np.round(proba[0][0], 3) * 100
    flag=""
    if int(predictr[0]) == int(0):
        flag="Safe"
    elif int(predictr[0]) == int(1):
        flag="Malware"
    print("The classification is = "+str(flag)+" \nWith accuracy of (Malware | Safe) = "+str(probam)+" | "+str(probas))
