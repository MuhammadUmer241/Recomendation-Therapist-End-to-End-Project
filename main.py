from src.make_index.create_index import vector_db 
import pandas as pd
from src.ner.unique_list import load_list
from src.ner.zero_short import zero_shot_classification


# path = r"C:\Users\Umer\Desktop\Recomendation-Therapist-End-to-End-Project\data\preprocessed_with_combine_text.csv"
# df = pd.read_csv(path)

# obj = vector_db(dataframe=df)
# # obj.make_chromadb()
# print(obj.search(" Available both in-person and online"))




sentence = "i need a direct therapist "
labels = load_list(name="therapy")

results = zero_shot_classification(sentence, labels)

# Print the ranked labels
list_ = []
for label, score in results:
    list_.append(label)
    print(f"Label: {label} \t Similarity Score: {score[0]:.4f}")  # Access the first element
    break
print(list_)
# print(labels)
# Corrected Code



