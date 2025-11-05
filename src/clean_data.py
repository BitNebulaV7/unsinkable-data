

def clean_missing_values(df, strategy = 'median'):
    """
    Cleans missing values in the Titanic dataset.
    - Drops 'Cabin' column
    - Imputes 'Age' using median or mode
    - Drops rows with missing 'Embarked'
    """

    df = df.drop(columns=['Cabin'])
    if strategy == 'median':
        df['Age'] = df['Age'].fillna(df['Age']).median()
    elif strategy == 'mode':
        df['Age'] = df['Age'].fillna(df['Age']).mode()[0]
    else:
        raise ValueError("Strategy must be 'median' or 'mode'")
    
    df = df.dropna(subset=['Embarked'])

    return df

    