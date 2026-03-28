import sys
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer


def preprocess_for_clustering(df, numeric_columns=None):
    """
    Prepare data for clustering by handling non-numeric columns and missing values
    """
    if numeric_columns is None:
        numeric_df = df.select_dtypes(include=[np.number])
    else:
        numeric_df = df[numeric_columns].select_dtypes(include=[np.number])
    
    imputer = SimpleImputer(strategy='mean')
    numeric_df_imputed = pd.DataFrame(
        imputer.fit_transform(numeric_df),
        columns=numeric_df.columns
    )
    
    scaler = StandardScaler()
    numeric_df_scaled = pd.DataFrame(
        scaler.fit_transform(numeric_df_imputed),
        columns=numeric_df.columns
    )
    
    return numeric_df_scaled, numeric_df_imputed.columns.tolist()

df = pd.read_csv(sys.argv[1])

print(f"Dataset shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Data types:\n{df.dtypes}")

numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

if len(numeric_cols) < 2:
    print("Error: Need at least 2 numeric columns for clustering")
    print(f"Found numeric columns: {numeric_cols}")
    sys.exit(1)

print(f"\nUsing numeric columns for clustering: {numeric_cols}")

try:
    X, used_columns = preprocess_for_clustering(df, numeric_cols)
    print(f"\nData prepared for clustering with shape: {X.shape}")
    
    n_samples = X.shape[0]
    n_features = X.shape[1]
    
    if n_samples < 30:
        n_clusters = 2
    elif n_samples < 100:
        n_clusters = 3
    else:
        n_clusters = 4
    
    print(f"\nApplying K-Means clustering with {n_clusters} clusters...")
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(X)
    
    df['cluster'] = cluster_labels
    
    counts = df['cluster'].value_counts().sort_index()
    
    with open("results/clusters.txt", "w") as f:
        f.write("K-Means Clustering Results\n")
        f.write("=" * 40 + "\n")
        f.write(f"Total samples: {len(df)}\n")
        f.write(f"Number of clusters: {n_clusters}\n")
        f.write(f"Features used: {', '.join(used_columns)}\n")
        f.write("=" * 40 + "\n\n")
        f.write("Samples per cluster:\n")
        f.write("-" * 20 + "\n")
        for cluster_id, count in counts.items():
            f.write(f"Cluster {cluster_id}: {count} samples ({count/len(df)*100:.1f}%)\n")
        
        f.write("\n\nClustering Statistics:\n")
        f.write("-" * 20 + "\n")
        f.write(f"Inertia (within-cluster sum of squares): {kmeans.inertia_:.2f}\n")
    
    print("\nClustering done!")
    print("Results saved to clusters.txt")
    print("\nCluster distribution:")
    for cluster_id, count in counts.items():
        print(f"  Cluster {cluster_id}: {count} samples ({count/len(df)*100:.1f}%)")
    
except Exception as e:
    print(f"Error during clustering: {e}")
    sys.exit(1)