import pandas as pd 
from pathlib import Path 
import os 

def path(root=True):
    path = os.path.join(Path(__file__).resolve().parents[2], "data","unique_records")
    if root==True:
        return path
    return os.path.join(path, root)


def data_processing(path):
    df = pd.read_csv(path)
    cols = df.columns
    return list(df[cols[0]])


def load_list(name="age"):

    for dirs in os.listdir(path()):
        try:
            if name in dirs.lower():
                return data_processing(path= path(root=dirs))            
        except:
            raise "file not found"

