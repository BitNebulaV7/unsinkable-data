
def convert_types(df, schema):
    """
    Converts column types based on a schema dictionary.
    """
    for col, dtype in schema.items():
        if col in df.columns:
            df[col] = df[col].astype(dtype)
    return df