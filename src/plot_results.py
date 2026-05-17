import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_all(results_dir="results", filename="final_results.csv", suffix=""):
    # Load final results
    results_path = os.path.join(results_dir, filename)
    if not os.path.exists(results_path):
        print(f"Results file {results_path} not found.")
        return
    
    df = pd.read_csv(results_path)
    
    # 1. Accuracy Comparison by Method and Alpha
    plt.figure(figsize=(10, 6))
    methods = df['method'].unique()
    alphas = df['alpha'].unique()
    
    x = range(len(methods))
    width = 0.2
    
    for i, alpha in enumerate(alphas):
        alpha_df = df[df['alpha'] == alpha]
        # Ensure methods are in same order
        accs = [alpha_df[alpha_df['method'] == m]['final_acc'].values[0] for m in methods]
        plt.bar([p + i*width for p in x], accs, width, label=f'Alpha={alpha}')
    
    plt.title(f'Final Accuracy Comparison {suffix}')
    plt.xticks([p + width for p in x], methods)
    plt.ylabel('Accuracy')
    plt.ylim(0, 1.0)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig(os.path.join(results_dir, f'accuracy_comparison{suffix}.png'))
    plt.close()
    
    # 2. Communication Cost vs Accuracy
    plt.figure(figsize=(10, 6))
    for method in methods:
        method_df = df[df['method'] == method]
        plt.scatter(method_df['total_comm_mb'], method_df['final_acc'], s=100, label=method)
        # Add alpha labels to dots
        for _, row in method_df.iterrows():
            plt.annotate(f"a={row['alpha']}", (row['total_comm_mb'], row['final_acc']))
    
    plt.title(f'Communication Cost vs Accuracy {suffix}')
    plt.xlabel('Total Communication (MB)')
    plt.ylabel('Final Accuracy')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig(os.path.join(results_dir, f'comm_vs_acc{suffix}.png'))
    plt.close()

if __name__ == "__main__":
    # Plot the balanced results
    if os.path.exists("results/balanced_results.csv"):
        plot_all(filename="balanced_results.csv", suffix="_balanced")
    # Also plot the final_results.csv if it exists (for the quick run later)
    if os.path.exists("results/final_results.csv"):
        plot_all(filename="final_results.csv", suffix="_quick")
