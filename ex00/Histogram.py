import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_histogram(file_path):
    df = pd.read_csv(file_path)

    plt.figure(figsize=(15, 10))

    for column in df.columns:
        if column != 'knight':
            sns.histplot(data=df, x=column, hue='knight', kde=True, multiple="stack")
            plt.title(f'Distribution of {column} by Knight Type')
            plt.xlabel(column)
            plt.ylabel('Count')
            plt.legend(title='Knight Type')
            plt.savefig(f'histogram_{column}.png')
            plt.clf()  # Clear the current figure

    print("Histograms have been saved as separate PNG files.")

if __name__ == "__main__":
    create_histogram("Test_knight.csv")
