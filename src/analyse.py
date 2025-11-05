def survival_rate(df):
    """
    Returns overall survival rate.
    """
    return df['Survived'].value_counts(normalize=True).round(2)

def survival_by_sex(df):
    """
    Returns survival rate grouped by Sex.
    """
    return df.groupby('Sex')['Survived'].mean().round(2)

def survival_by_class(df):
    """
    Returns survival rate grouped by Pclass.
    """
    return df.groupby('Pclass')['Survived'].mean().round(2)

def survival_by_sex_class(df):
    """
    Returns survival rate grouped by Sex and Pclass.
    """
    return df.groupby(['Sex', 'Pclass'])['Survived'].mean().round(2)
