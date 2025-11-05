
from src.load_data import load_data, summarise_df
from src.clean_data import clean_missing_values


df = load_data("data/raw/Titanic_dataset.csv")
summary = summarise_df(df)
print(summary)


df_clean = clean_missing_values(df, strategy = 'median')
print(df_clean.isnull().sum())