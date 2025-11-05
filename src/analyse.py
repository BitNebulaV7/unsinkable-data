def survival_rate(df):
    """
    Returns overall survival rate.
    """
    return df['Survived'].value_counts(normalize=True).round(2)

def survival_by_sex(df):
    """
    Returns survival rate grouped by Sex.
    """
    return df.groupby('Sex', observed=True)['Survived'].mean().round(2)

def survival_by_class(df):
    """
    Returns survival rate grouped by Pclass.
    """
    return df.groupby('Pclass', observed=True)['Survived'].mean().round(2)

def survival_by_sex_class(df):
    """
    Returns survival rate grouped by Sex and Pclass.
    """
    return df.groupby(['Sex', 'Pclass'], observed=True)['Survived'].mean().round(2)
