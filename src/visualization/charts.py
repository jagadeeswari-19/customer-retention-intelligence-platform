import matplotlib.pyplot as plt

def plot_churn_distribution(df):

    df["Churn"].value_counts().plot(kind="bar")

    plt.title("Churn Distribution")

    plt.xlabel("Churn")

    plt.ylabel("Count")

    plt.show()