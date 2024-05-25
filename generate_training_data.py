import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib

# Générer des données d'exemple pour entraîner le modèle
data = pd.DataFrame({
    'authorization_number': [i for i in range(1, 101)],
    'amount': [i * 10 for i in range(1, 101)],
    'merchant_number': [f'M{i}' for i in range(1, 101)],
    'merchant_email': [f'merchant{i}@example.com' for i in range(1, 101)],
    'merchant_name': [f'Merchant{i}' for i in range(1, 101)],
    'status': ['created', 'sent_to_merchant', 'processing_by_paymee', 'processing_by_bank', 'won', 'lost', 'desactivated', 'reactivate'] * 12 + ['created', 'sent_to_merchant', 'processing_by_paymee', 'processing_by_bank'],
    'reason': ['Customer dispute', 'Fraud', 'Technical issue'] * 33 + ['Customer dispute'],
    'resolution_time': [i % 30 + 1 for i in range(1, 101)]  # Temps de résolution en jours
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

# Sauvegarder les ensembles d'entraînement pour la visualisation
X_train.to_csv('X_train.csv', index=False)
y_train.to_csv('y_train.csv', index=False)

print("Model and training data saved successfully.")
