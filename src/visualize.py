import matplotlib.pyplot as plt
import seaborn as sns

def plot_overall_survival(survival_series):
    survival_series.plot(kind='bar', color=['salmon', 'skyblue'])
    plt.title("Overall Survival Rate")
    plt.xlabel("Survived")
    plt.ylabel("Proportion")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

def plot_survival_by_sex(survival_series):
    survival_series.plot(kind='bar', color='mediumseagreen')
    plt.title("Survival Rate by Sex")
    plt.xlabel("Sex")
    plt.ylabel("Survival Rate")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
    
def plot_survival_by_class(survival_series):
    survival_series.plot(kind='bar', color='steelblue')
    plt.title("Survival Rate by Class")
    plt.xlabel("Pclass")
    plt.ylabel("Survival Rate")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

def plot_survival_by_sex_class(survival_series):
    survival_series.unstack().plot(kind='bar', stacked=False, colormap='coolwarm')
    plt.title("Survival Rate by Sex and Class")
    plt.xlabel("Sex")
    plt.ylabel("Survival Rate")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
    

def plot_distribution(df, column):
    plt.figure(figsize=(15, 4))

    # Histogram
    plt.subplot(1, 3, 1)
    sns.histplot(df[column], kde=False, bins=30)
    plt.title(f'Histogram of {column}')

    # KDE Plot
    plt.subplot(1, 3, 2)
    sns.kdeplot(df[column], fill=True)
    plt.title(f'KDE Plot of {column}')

    # Boxplot
    plt.subplot(1, 3, 3)
    sns.boxplot(x=df[column])
    plt.title(f'Boxplot of {column}')

    plt.tight_layout()
    plt.show()
