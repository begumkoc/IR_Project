import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def plot_metric(results: pd.DataFrame, metric: str, hue: str,
                title: str, legend_title: str = ""):
    plt.figure(figsize=(10, 6))

    sns.set(style="whitegrid")
    # Plot each retrieval model as a separate line
    sns.lineplot(
        data=results,
        x="noise_level",
        y=metric,
        hue=hue,
        marker="o",
    )

    plt.title(title, fontsize=14)
    plt.xlabel("Noise Level", fontsize=12)
    plt.ylabel(metric, fontsize=12)
    plt.legend(title=legend_title)  # Add a legend for models
    plt.show()