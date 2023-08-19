# Clasificación no supervisada
from kmodes.kmodes import KModes

# Métricas para evaluar modelos
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from sklearn.metrics.cluster import adjusted_rand_score

# Funciones propias
import src.data_common_functions as dcf

def _generate_df_kmodes(df):
    
    df_to_transform = df.loc[:, ['age_range', 
                            'obesity_bmi',
                            'obesity_cc',
                            'obesity_rcc',
                            'obesity_ict',
                            'risk_factors'
                                ] ]
    
    columns_to_encode = ['age_range']
    columns_to_scale = []
    # Passthrough columns
    columns_to_pass = [ 'obesity_bmi',
                        'obesity_cc',
                        'obesity_rcc',
                        'obesity_ict',
                        'risk_factors'
                      ]
    
    df_kmodes = dcf.transform_df(df_to_transform, columns_to_encode, columns_to_scale, columns_to_pass)
    
    return df_kmodes

def generate_kmodes_clusters(df, n_clusters, n_init, random_state, eda_report=True):    
    
    df_kmodes = _generate_df_kmodes(df)
    
    k_modes = KModes(n_clusters=n_clusters, init='Huang', n_init=n_init, random_state=random_state)
    cluster_labels = k_modes.fit_predict(df_kmodes)

    # Agrega los resultados de la agrupación al dataframe original
    df['cluster'] = cluster_labels

    # Métricas del modelo
    metrics = {
        'model': 'KModes',
        'n_clusters': n_clusters,
        'cost': k_modes.cost_,
        'silhouette_score': silhouette_score(df_kmodes, k_modes.labels_),
        'calinski_harabasz_score': calinski_harabasz_score(df_kmodes, k_modes.labels_),
        'davies_bouldin_score': davies_bouldin_score(df_kmodes, k_modes.labels_)
    }

    return (df, metrics)
