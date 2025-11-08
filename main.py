
from src.load_data import load_data, summarise_df
from src.clean_data import clean_missing_values
from utils.schema import schema
from src.convert_types import convert_types
from src.analyse import survival_rate, survival_by_sex, survival_by_class, survival_by_sex_class
from src.visualize import (plot_overall_survival,
    plot_survival_by_sex,
    plot_survival_by_class,
    plot_survival_by_sex_class)

df = load_data("data/raw/Titanic_dataset.csv")
summary = summarise_df(df)
print(summary)


df_clean = clean_missing_values(df, strategy = 'median')
print(df_clean.isnull().sum())

df_convert = convert_types(df_clean, schema)
print(df_convert.dtypes)

print("Overall survival rate:")
print(survival_rate(df_convert))

print("\nSurvival by Sex:")
print(survival_by_sex(df_convert))

print("\nSurvival by Class:")
print(survival_by_class(df_convert))

print("\nSurvival by Sex and Class:")
print(survival_by_sex_class(df_convert))




plot_overall_survival(survival_rate(df_convert))
plot_survival_by_sex(survival_by_sex(df_convert))
plot_survival_by_class(survival_by_class(df_convert))
plot_survival_by_sex_class(survival_by_sex_class(df_convert))