from src.make_index.create_index import vector_db 
import pandas as pd
path = r"C:\Users\Umer\Desktop\Recomendation-Therapist-End-to-End-Project\data\preprocessed_with_combine_text.csv"
df = pd.read_csv(path)

obj = vector_db(dataframe=df)
# obj.make_chromadb()
print(obj.search(" Available both in-person and online"))






