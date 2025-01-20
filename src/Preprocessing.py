import numpy as np
from datasets import load_dataset
import pandas as pd
import pickle as pkl
from pprint import pprint as print

def TransformDataset(Dataset : pd.DataFrame) -> pd.DataFrame:
        if bool(Dataset.isna().sum().any()):
                Dataset.dropna(inplace=True)
        categorical_columns = Dataset.select_dtypes(include=['object']).columns
        with open('/home/slypex/studies/3CS/Ingeniorat/AdvanDL/Mini-Project/project/src/Encoders/labelencoder.pkl', 'rb') as label_encoder:
                le = pkl.load(label_encoder)
                for col in categorical_columns:
                        Dataset[col] = le[col].transform(Dataset[col])
        with open('/home/slypex/studies/3CS/Ingeniorat/AdvanDL/Mini-Project/project/src/Encoders/scaler.pkl', 'rb') as scaler_fd:
                scaler = pkl.load(scaler_fd)
                scaled_data = scaler.transform(Dataset)
        
        return pd.DataFrame(scaled_data, columns=Dataset.columns)
        
