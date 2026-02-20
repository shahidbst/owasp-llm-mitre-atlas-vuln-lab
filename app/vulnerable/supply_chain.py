import pickle
import requests

def load_remote_model():
    # Vulnerable: downloading model without integrity check
    data = requests.get("http://example.com/model.pkl").content
    return pickle.loads(data)
