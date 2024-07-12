from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Standardize the features
scaler = StandardScaler()
data_poly_scaled = scaler.fit_transform(data_poly.drop(columns='target'))

# Apply PCA
pca = PCA(n_components=0.95)  # Preserve 95% of the variance
data_poly_pca = pca.fit_transform(data_poly_scaled)

# Get the number of components selected
n_components = pca.n_components_
print(f'Number of components selected: {n_components}')
