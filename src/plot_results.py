import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_all(results_dir="results"):
    # Load final results
    results_path = os.path.join(results_dir, "final_results.csv")
    if not os.path.exists(results_path):
        print("Results file not found.")
        return
    
    df = pd.read_csv(results_path)
    
    # Example plot: Accuracy vs Method
    plt.figure(figsize=(10, 6))
    for alpha in df['alpha'].unique():
        alpha_df = df[df['alpha'] == alpha]
        plt.bar(alpha_df['method'], alpha_df['final_acc'], label=f'Alpha={alpha}')
    
    plt.title('Final Accuracy by Method and Alpha')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.savefig(os.path.join(results_dir, 'accuracy_comparison.png'))
    plt.close()
    
    # Communication vs Accuracy
    plt.figure(figsize=(10, 6))
    for method in df['method'].unique():
        method_df = df[df['method'] == method]
        plt.scatter(method_df['total_comm_mb'], method_df['final_acc'], label=method)
    
    plt.title('Communication Cost vs Accuracy')
    plt.xlabel('Total Communication (MB)')
    plt.ylabel('Final Accuracy')
    plt.legend()
    plt.savefig(os.path.join(results_dir, 'comm_vs_acc.png'))
    plt.close()

if __name__ == "__main__":
    plot_all()
