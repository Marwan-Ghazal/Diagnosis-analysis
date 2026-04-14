import sys
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from matplotlib.gridspec import GridSpec

print("Loading data...")
df = pd.read_csv(sys.argv[1])
print(f"Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")

numeric_df = df.select_dtypes(include=[np.number])
print(f"Numeric columns: {len(numeric_df.columns)} columns")

binary_cols = [col for col in numeric_df.columns if numeric_df[col].nunique() <= 2]
continuous_cols = [col for col in numeric_df.columns if numeric_df[col].nunique() > 2]

print(f"Excluded binary columns: {binary_cols}")
print(f"Using continuous columns: {continuous_cols}")

os.makedirs("results", exist_ok=True)

fig, axes = plt.subplots(4, 3, figsize=(20, 22))
fig.patch.set_facecolor('white')
plt.subplots_adjust(hspace=0.45, wspace=0.25, left=0.08, right=0.95, top=0.93, bottom=0.04)

hist_axes = axes[0, :].tolist() + axes[1, :].tolist()

if continuous_cols:
    n_features = len(continuous_cols)
    hist_per_row = 3
    n_hist_rows = 2
    
    for idx, col in enumerate(continuous_cols):
        if idx < len(hist_axes):
            ax = hist_axes[idx]
            numeric_df[col].hist(ax=ax, bins=20, alpha=0.7, edgecolor='black', linewidth=1.2, color='steelblue')
            ax.set_title(f'{col}', fontsize=11, fontweight='bold')
            ax.tick_params(labelsize=9)
            ax.grid(True, alpha=0.3)
            ax.set_xlabel('')
            ax.set_ylabel('Frequency', fontsize=9)
    
    for ax in hist_axes[n_features:]:
        ax.set_visible(False)
    
    for i in range(n_features, len(hist_axes)):
        axes.flat[i].set_visible(False)

n_corr = len(numeric_df.columns)
if n_corr >= 2:
    corr_matrix = numeric_df.corr()
    annot_size = 10 if n_corr <= 6 else 7
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm',
                square=True, ax=axes[2, 1], cbar_kws={'shrink': 0.7},
                annot_kws={'size': annot_size}, linewidths=0.5, linecolor='white')
    axes[2, 1].set_title('CORRELATION HEATMAP', fontsize=12, fontweight='bold', pad=12)
    axes[2, 1].set_xticklabels(axes[2, 1].get_xticklabels(), rotation=45, ha='right', fontsize=8)
    axes[2, 1].set_yticklabels(axes[2, 1].get_yticklabels(), rotation=0, fontsize=8)
axes[2, 0].set_visible(False)
axes[2, 2].set_visible(False)

if not numeric_df.empty:
    bp = numeric_df.boxplot(ax=axes[3, 1], rot=45, fontsize=10, patch_artist=True)
    axes[3, 1].set_title('BOX PLOTS', fontsize=12, fontweight='bold', pad=12)
    axes[3, 1].set_ylabel('Values', fontsize=10)
    axes[3, 1].grid(True, alpha=0.3)
    if numeric_df.max().max() > 1000:
        axes[3, 1].ticklabel_format(style='scientific', axis='y', scilimits=(0, 0))
    for patch in bp.artists:
        patch.set_width(0.6)
axes[3, 0].set_visible(False)
axes[3, 2].set_visible(False)

fig.suptitle('COMPREHENSIVE DATASET VISUALIZATION', fontsize=16, fontweight='bold', y=0.98)

output_file = "results/summary_plot.png"
plt.savefig(output_file, dpi=150, bbox_inches='tight', format='png', facecolor='white')
plt.close()

if os.path.exists(output_file):
    file_size = os.path.getsize(output_file)
    print(f"\n{'='*50}")
    print(f"summary_plot.png created successfully!")
    print(f"  File size: {file_size:,} bytes")
    print(f"{'='*50}")

print("\nLAYOUT (4 ROWS x 3 COLS):")
print("  ROW 1-2: Histograms (6 total)")
print("  ROW 3: Correlation Heatmap (center)")
print("  ROW 4: Box Plots (center)")