import sys
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

print("Loading data...")
df = pd.read_csv(sys.argv[1])
print(f"Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")

numeric_df = df.select_dtypes(include=[np.number])
print(f"Numeric columns: {len(numeric_df.columns)} columns")


print("\n Creating Plot 1: Histograms...")
plt.figure(figsize=(12, 8))

if not numeric_df.empty:
    numeric_df.hist(bins=20, alpha=0.7, edgecolor='black', linewidth=1.5)
    plt.suptitle('Distribution of Numeric Features', fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig("histogram.png", dpi=150, bbox_inches='tight', facecolor='white')
    print("✓ Saved: histogram.png")
else:
    plt.text(0.5, 0.5, 'No numeric columns available', ha='center', va='center', fontsize=14)
    plt.savefig("histogram.png", dpi=150, bbox_inches='tight')
    print("✓ Saved: histogram.png (empty - no numeric data)")
plt.close()

print("\nCreating Plot 2: Correlation Heatmap...")
plt.figure(figsize=(12, 10))

if not numeric_df.empty and len(numeric_df.columns) >= 2:
    corr_matrix = numeric_df.corr()
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
                square=True, cbar_kws={'shrink': 0.8, 'label': 'Correlation'},
                annot_kws={'size': 10}, linewidths=0.5, linecolor='white')
    plt.title('Correlation Heatmap of Numeric Features', fontsize=16, fontweight='bold', pad=20)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig("heatmap.png", dpi=150, bbox_inches='tight', facecolor='white')
    print("✓ Saved: heatmap.png")
else:
    plt.text(0.5, 0.5, f'Need at least 2 numeric columns\nFound: {len(numeric_df.columns)}', 
             ha='center', va='center', fontsize=14)
    plt.title('Correlation Heatmap', fontsize=16, fontweight='bold')
    plt.savefig("heatmap.png", dpi=150, bbox_inches='tight')
    print("✓ Saved: heatmap.png (insufficient numeric columns)")
plt.close()

print("\n Creating Plot 3: Pairplot...")

if not numeric_df.empty and len(numeric_df.columns) >= 2:
    n_cols = min(5, len(numeric_df.columns))
    cols_to_plot = numeric_df.columns[:n_cols].tolist()
    
    pairplot_fig = sns.pairplot(numeric_df[cols_to_plot], 
                                diag_kind='hist',
                                plot_kws={'alpha': 0.6, 's': 30, 'edgecolor': 'black'},
                                diag_kws={'bins': 20, 'edgecolor': 'black'})
    
    pairplot_fig.fig.suptitle('Pairplot of Numeric Features', 
                              fontsize=16, fontweight='bold', y=1.02)
    
    pairplot_fig.fig.tight_layout()
    
    pairplot_fig.savefig("pairplot.png", dpi=150, bbox_inches='tight', facecolor='white')
    plt.close(pairplot_fig.fig)
    print(f"✓ Saved: pairplot.png (using {n_cols} features: {', '.join(cols_to_plot)})")
else:
    plt.figure(figsize=(10, 8))
    plt.text(0.5, 0.5, f'Need at least 2 numeric columns\nFound: {len(numeric_df.columns)}', 
             ha='center', va='center', fontsize=14)
    plt.title('Pairplot', fontsize=16, fontweight='bold')
    plt.savefig("pairplot.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Saved: pairplot.png (insufficient numeric columns)")


print("\n" + "="*50)
print(" ALL THREE PLOTS CREATED SUCCESSFULLY!")
print("="*50)
print("\n Generated Files:")
print("  1. histogram.png  - Distribution of numeric features")
print("  2. heatmap.png    - Correlation between features")
print("  3. pairplot.png   - Pairwise relationships between features")

print("\n File Sizes:")
for filename in ["histogram.png", "heatmap.png", "pairplot.png"]:
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        print(f"  {filename}: {size:,} bytes")
    else:
        print(f"  {filename}: NOT FOUND")

print("\n TIP: Open each file with an image viewer (Photos/Paint/Preview) to see the graphs!")

if os.path.exists("cluster.py"):
    print("\n Proceeding to clustering...")
    os.system("python cluster.py data_preprocessed.csv")