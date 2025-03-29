import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_metric(results: pd.DataFrame, metric: str, title: str, legend_title: str = ""):
    plt.figure(figsize=(10, 6))

    sns.set(style="whitegrid")
    # Plot each retrieval model as a separate line
    sns.lineplot(
        data=results,
        x="noise_level",
        y=metric,
        hue="name",
        marker="o",
    )

    plt.title(title, fontsize=14)
    plt.xlabel("Noise Level", fontsize=12)
    plt.ylabel(metric, fontsize=12)
    plt.legend(title=legend_title)  # Add a legend for models
    plt.show()

def add_query_noise(queries: pd.DataFrame, noise_metric) -> pd.DataFrame:
    noisy_queries_list = []
    for _, row in queries.iterrows():
        noisy_query = noise_metric.augment(row['query'])

        if isinstance(noisy_query, list):
            noisy_query = " ".join(noisy_query)

        noisy_queries_list.append({'qid': row['qid'], 'query': noisy_query})

    noisy_queries_df = pd.DataFrame(noisy_queries_list)
    noisy_queries_df["qid"] = noisy_queries_df["qid"].astype(str)
    return noisy_queries_df