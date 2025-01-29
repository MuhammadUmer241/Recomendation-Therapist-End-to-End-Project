from sentence_transformers import SentenceTransformer
import os
import chromadb
class vector_db:
    def __init__(self, dataframe, model= SentenceTransformer("all-MiniLM-L6-v2") ):
        self.dataframe = dataframe
        self.model= model
        self.path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),"vectordb")
        os.makedirs(self.path, exist_ok=True)
        self.chroma_client = chromadb.PersistentClient(path= self.path)  # Saves the DB locally
        self.collection = self.chroma_client.get_or_create_collection(name="therapist_db")

    def __check_col(self):
        required_cols = ["combine_text", "age", "participants", "fee", "availablity"]
        if not all(col in self.dataframe.columns for col in required_cols):
           raise ValueError("Missing required columns in CSV.")
    
        return self.dataframe
    
    def make_chromadb(self):
        self.dataframe = self.__check_col()
        for i, row in self.dataframe.iterrows():
          text = row["combine_text"]
          metadata = {
              "age": row["age"],
              "participants": row["participants"],
              "fee": row["fee"],
              "availability": row["availablity"]
          }
          
          # Generate embedding for the text
          embedding = self.model.encode(text).tolist()
          
          # Insert into ChromaDB
          self.collection.add(
              ids=[str(i)],  # Unique ID for each entry
              embeddings=[embedding],
              metadatas=[metadata],
              documents=[text]  # Store original text for reference
          )
      
        print(f"✅ Successfully inserted {len(self.dataframe)} records into ChromaDB.")

import pandas as pd
path = r"C:\Users\Umer\Desktop\Recomendation-Therapist-End-to-End-Project\data\preprocessed_with_combine_text.csv"
df = pd.read_csv(path)

obj = vector_db(dataframe=df)
obj.make_chromadb()







