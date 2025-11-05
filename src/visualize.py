import matplotlib.pyplot as plt

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
