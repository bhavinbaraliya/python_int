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

from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Separate features and target variable
X = data_poly.drop(columns='target')
y = data['target']

# Train a Random Forest model
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X, y)

# Get feature importances
importances = rf.feature_importances_

# Create a DataFrame for feature importances
feature_importances = pd.DataFrame({
    'feature': X.columns,
    'importance': importances
}).sort_values(by='importance', ascending=False)

# Display the top 10 most important features
print(feature_importances.head(10))
