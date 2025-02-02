from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F

# Load Sentence-BERT model
model_name = "sentence-transformers/all-MiniLM-L6-v2"  # Fast and optimized model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def get_embedding(text):
    """Generates embedding for a given text"""
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        output = model(**inputs)
    return output.last_hidden_state.mean(dim=1)  # Mean pooling

def zero_shot_classification(text, labels):
    """Finds the most relevant label using cosine similarity"""
    text_emb = get_embedding(text)
    label_embs = torch.stack([get_embedding(label) for label in labels])

    # Compute cosine similarity
    similarities = F.cosine_similarity(text_emb, label_embs)
    
    # Sort labels by similarity
    sorted_labels = sorted(zip(labels, similarities.tolist()), key=lambda x: x[1], reverse=True)

    return sorted_labels


sentence = "in-person"
labels = ["avaialble online", "available onsite", "both-in person"]

results = zero_shot_classification(sentence, labels)

# Print the ranked labels

# Corrected Code
list_ = []
for label, score in results:
    list_.append(label)
    print(f"Label: {label} \t Similarity Score: {score[0]:.4f}")  # Access the first element
    break
print(list_)