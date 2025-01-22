import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def TransformDataset(Dataset : pd.DataFrame, Threshold: int = 0.95) -> pd.DataFrame:
        if bool(Dataset.isna().sum().any()):
                Dataset.dropna(inplace=True)
        # Change the class to Integer values manually to math action space in the ENV
        Dataset.iloc[:, -1] = Dataset.iloc[:,-1].map(lambda x: 0 if x == 'normal' else 1)
        Dataset.iloc[:, -1].astype(dtype=np.int64)
        # Change categorical data to integer data of the remaining columns
        categorical_columns = Dataset.select_dtypes(include=['object']).columns
        for col in categorical_columns:
                le = LabelEncoder()
                Dataset[col] = le.fit_transform(Dataset[col])
        scaler = MinMaxScaler()
        scaled_df = pd.DataFrame(scaler.fit_transform(Dataset), columns=Dataset.columns)
        # Drop high correlated columns
        correlation = scaled_df.corr()
        upper_tri = correlation.where(np.triu(np.ones(correlation.shape, dtype=bool), k=1))
        to_drop = [column for column in upper_tri.columns if any(upper_tri[column] >= Threshold)]
        scaled_df.drop(to_drop, inplace=True)
        print(len(scaled_df.columns))
        return scaled_df
        
