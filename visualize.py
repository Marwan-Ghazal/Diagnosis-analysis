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

fig = plt.figure(figsize=(18, 14))

ax1 = plt.subplot(2, 2, 1)  
ax2 = plt.subplot(2, 2, 2)  
ax3 = plt.subplot(2, 2, 3)  

if not numeric_df.empty:
    numeric_df.hist(ax=ax1, bins=20, alpha=0.7, edgecolor='black', linewidth=1.5)
    ax1.set_title('1. DISTRIBUTION OF NUMERIC FEATURES', fontsize=14, fontweight='bold', pad=20)
    ax1.tick_params(axis='x', rotation=45, labelsize=10)
    ax1.tick_params(axis='y', labelsize=10)
    ax1.set_xlabel('Values', fontsize=12, labelpad=10)
    ax1.set_ylabel('Frequency', fontsize=12, labelpad=10)
    ax1.grid(True, alpha=0.3)
else:
    ax1.text(0.5, 0.5, 'No numeric columns', ha='center', va='center', fontsize=12)

if not numeric_df.empty and len(numeric_df.columns) >= 2:
    corr_matrix = numeric_df.corr()
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
                square=True, ax=ax2, cbar_kws={'shrink': 0.8, 'label': 'Correlation'},
                annot_kws={'size': 10}, linewidths=0.5, linecolor='white')
    ax2.set_title('2. CORRELATION HEATMAP', fontsize=14, fontweight='bold', pad=20)
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right', fontsize=10)
    ax2.set_yticklabels(ax2.get_yticklabels(), rotation=0, fontsize=10)
else:
    ax2.text(0.5, 0.5, f'Need 2+ numeric columns\nFound: {len(numeric_df.columns)}', 
             ha='center', va='center', fontsize=12)

if not numeric_df.empty and len(numeric_df.columns) >= 2:
    col1 = numeric_df.columns[0]
    col2 = numeric_df.columns[1]
    if len(numeric_df.columns) >= 3:
        col3 = numeric_df.columns[2]
        scatter = ax3.scatter(numeric_df[col1], numeric_df[col2], 
                             c=numeric_df[col3], cmap='viridis', 
                             alpha=0.6, s=50, edgecolors='black', linewidth=0.5)
        cbar = plt.colorbar(scatter, ax=ax3)
        cbar.set_label(col3, fontsize=10)
    else:
        ax3.scatter(numeric_df[col1], numeric_df[col2], alpha=0.6, s=50, 
                   edgecolors='black', linewidth=0.5)
    
    ax3.set_xlabel(col1, fontsize=12, labelpad=10)
    ax3.set_ylabel(col2, fontsize=12, labelpad=10)
    ax3.set_title(f'3. SCATTER PLOT: {col1} vs {col2}', fontsize=14, fontweight='bold', pad=20)
    ax3.grid(True, alpha=0.3)
else:
    ax3.text(0.5, 0.5, f'Need 2+ numeric columns\nFound: {len(numeric_df.columns)}', 
             ha='center', va='center', fontsize=12)

plt.tight_layout(pad=5.0)  
plt.subplots_adjust(top=0.93, bottom=0.08, left=0.08, right=0.92, 
                    hspace=0.45, wspace=0.4)  

fig.suptitle('DATASET VISUALIZATION SUMMARY', fontsize=18, fontweight='bold', y=0.98)

output_file = "summary_plot.png"
plt.savefig(output_file, dpi=200, bbox_inches='tight', format='png', facecolor='white', edgecolor='none')
plt.close()

if os.path.exists(output_file):
    file_size = os.path.getsize(output_file)
    print(f"\n{'='*50}")
    print(f"✓ summary_plot.png created successfully!")
    print(f"  File size: {file_size:,} bytes")
    print(f"  Expected size: > 50,000 bytes for a valid image")
    
    if file_size < 10000:
        print(f"  ⚠ WARNING: File is too small ({file_size} bytes). Plot may be empty!")
    else:
        print(f"  ✓ File size is good. Open with image viewer to see the graphs!")
    print(f"{'='*50}")
else:
    print(f"ERROR: Failed to create {output_file}")

print("\nTHREE PLOTS INCLUDED:")
print("  1. HISTOGRAMS - Distribution of all numeric features")
print("  2. CORRELATION HEATMAP - Feature relationships using seaborn")
print("  3. SCATTER PLOT - Relationship between first two numeric features")

print("\n IMPROVEMENTS MADE:")
print("  ✓ Increased figure size (18x14) for more space")
print("  ✓ Added more spacing between subplots (hspace=0.45, wspace=0.4)")
print("  ✓ Increased tight_layout padding (pad=5.0)")
print("  ✓ Used seaborn heatmap with annotations and colorbar")
print("  ✓ Added grid lines and improved styling")
print("  ✓ Increased DPI to 200 for better quality")

if os.path.exists("cluster.py"):
    print("\n Proceeding to clustering...")
    os.system("python cluster.py data_preprocessed.csv")