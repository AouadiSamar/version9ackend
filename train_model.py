import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib

# Exemple de données pour générer le modèle
data = pd.DataFrame({
    'authorization_number': [123456, 654321, 789012],
    'amount': [100.00, 200.00, 150.00],
    'merchant_number': ['M12345', 'M54321', 'M67890'],
    'merchant_email': ['merchant1@example.com', 'merchant2@example.com', 'merchant3@example.com'],
    'merchant_name': ['Merchant1', 'Merchant2', 'Merchant3'],
    'status': ['created', 'sent_to_merchant', 'processing_by_paymee'],
    'reason': ['Customer dispute', 'Fraud', 'Technical issue'],
    'resolution_time': [15, 20, 18]  # Exemple de temps de résolution en jours
})

# Encodage des catégories
label_encoder_status = LabelEncoder()
label_encoder_reason = LabelEncoder()
data['status_encoded'] = label_encoder_status.fit_transform(data['status'])
data['reason_encoded'] = label_encoder_reason.fit_transform(data['reason'])

# Préparation des données pour l'entraînement
X = data[['authorization_number', 'amount', 'status_encoded', 'reason_encoded']]
y = data['resolution_time']

# Séparation des ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement du modèle
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Sauvegarde du modèle
model_path = 'C:/Users/samar/Version5/Baackend/models/chargeback_resolution_model.pkl'
joblib.dump(model, model_path)
print("Model saved successfully.")
