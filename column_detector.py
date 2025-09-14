import pandas as pd

def detect_column_types(df: pd.DataFrame, threshold: int = 20):
    column_types = {}
    
    for col in df.columns:
        dtype = df[col].dtype
        
        if dtype == "object" or pd.api.types.is_string_dtype(df[col]):
            avg_len = df[col].dropna().astype(str).apply(len).mean()
            column_types[col] = "text" if avg_len > 20 else "categorical"
        
        elif pd.api.types.is_numeric_dtype(df[col]):
            unique_vals = df[col].nunique()
            column_types[col] = "categorical" if unique_vals < threshold else "numerical"
        
        else:
            column_types[col] = "categorical"
    
    return column_types


if __name__ == "__main__":
    sample_df = pd.DataFrame({
        "Age": [23, 25, 31, 40],
        "ZIP": [560001, 560002, 560001, 560003],
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "Review": ["Good product", "Bad", "Very long descriptive text...", "Average"]
    })
    
    result = detect_column_types(sample_df)
    print(result)
