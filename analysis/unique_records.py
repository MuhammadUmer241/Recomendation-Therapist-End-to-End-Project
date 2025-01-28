import pandas as pd
import os 



class analyzer:
    def __init__(self, path_dir=os.path.join("data", "therapist data.csv") ):
        self.df = pd.read_csv(path_dir)
        
    def analyze_objective(self):
        print("name" ,len(self.df))


