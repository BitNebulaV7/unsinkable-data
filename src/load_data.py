import pandas as pd



def load_data(path):
    df = pd.read_csv(path)
    return df

def summarise_df(df):
    """
    Summarizes the DataFrame:
    - Data types
    - Null counts
    - Null percentages
    """

    summary = pd.DataFrame({
        'dtypes' : df.dtypes,
        'nulls' : df.isnull().sum(),
        'nulls_%' : df.isnull().mean().round(2)

    })

    return summary