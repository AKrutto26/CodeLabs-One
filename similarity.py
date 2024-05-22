from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np

class LABSE:
    def __init__(self):
        # Load the tokenizer and model for LABSE
        self.tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/LaBSE")
        self.model = AutoModel.from_pretrained("sentence-transformers/LaBSE")
    
    def get_embeddings(self, texts):
        """
        Get embeddings for a list of texts using the LABSE model.
        
        Parameters:
        texts (list of str): List of names to encode.
        
        Returns:
        np.ndarray: Embeddings for the provided names.
        """
        # Tokenize the input texts
        inputs = self.tokenizer(texts, return_tensors='pt', padding=True, truncation=True)
        
        # Pass the inputs through the model to get embeddings
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # Extract embeddings for the [CLS] token (first token)
        embeddings = outputs.last_hidden_state[:, 0, :].cpu().numpy()
        
        return embeddings
    
    def compute_similarity(self, name1, name2):
        """
        Compute cosine similarity between two names.
        
        Parameters:
        name1 (str): The first name.
        name2 (str): The second name.
        
        Returns:
        float: Cosine similarity between the embeddings of the two names.
        """
        # Get embeddings for the two names
        embeddings = self.get_embeddings([name1, name2])
        
        # Compute cosine similarity
        similarity = np.dot(embeddings[0], embeddings[1]) / (np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1]))
        
        return similarity
