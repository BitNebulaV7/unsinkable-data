

def clean_missing_values(df, strategy = 'median'):
    """
    Cleans missing values in the Titanic dataset.
    - Drops 'Cabin' column
    - Imputes 'Age' using median or mode
    - Drops rows with missing 'Embarked'
    """

    df = df.drop(columns=['Cabin'])
    if strategy == 'median':
        df['Age'] = df['Age'].fillna(df['Age'].median())
    elif strategy == 'mode':
        df['Age'] = df['Age'].fillna(df['Age'].mode()[0])
    else:
        raise ValueError("Strategy must be 'median' or 'mode'")
    
    df = df.dropna(subset=['Embarked'])

    return df


def remove_outkliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    filltered_df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

    return filltered_df
    