import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

def plot_final_report_charts(results_dir="results"):
    # Load the main balanced results
    balanced_path = os.path.join(results_dir, "final_results.csv")
    if not os.path.exists(balanced_path):
        print("Final results for balanced mode not found.")
        return
    
    df = pd.read_csv(balanced_path)
    
    # Set professional style
    plt.rcParams.update({'font.size': 12, 'figure.titlesize': 14})
    
    # 1. Bar Chart: Accuracy across Methods and Alphas
    plt.figure(figsize=(12, 7))
    methods = ["standard_lora", "ffa_lora", "rolora"]
    alphas = sorted(df['alpha'].unique(), reverse=True)
    
    n_groups = len(alphas)
    index = np.arange(n_groups)
    bar_width = 0.25
    opacity = 0.8
    
    for i, method in enumerate(methods):
        method_data = df[df['method'] == method].sort_values('alpha', ascending=False)
        plt.bar(index + i*bar_width, method_data['final_acc'], bar_width,
                alpha=opacity, label=method.replace('_', ' ').upper())
    
    plt.xlabel('Dirichlet Alpha (Heterogeneity level)')
    plt.ylabel('Test Accuracy')
    plt.title('Performance comparison under varying Data Heterogeneity')
    plt.xticks(index + bar_width, [f'Alpha={a}' for a in alphas])
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, 'accuracy_matrix.png'), dpi=300)
    plt.close()
    
    # 2. Scatter Plot: Communication Efficiency vs Accuracy (Alpha=10.0)
    plt.figure(figsize=(10, 6))
    alpha_10 = df[df['alpha'] == 10.0]
    for _, row in alpha_10.iterrows():
        plt.scatter(row['total_comm_mb'], row['final_acc'], s=200, label=row['method'])
        plt.annotate(row['method'].upper(), (row['total_comm_mb'], row['final_acc']), 
                     textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.xlabel('Total Communication Volume (MB)')
    plt.ylabel('Final Accuracy')
    plt.title('Efficiency Pareto Front (IID Case)')
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(results_dir, 'efficiency_frontier.png'), dpi=300)
    plt.close()

    print("Regenerated report-ready charts: accuracy_matrix.png and efficiency_frontier.png")

if __name__ == "__main__":
    plot_final_report_charts()
