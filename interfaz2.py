import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
#importacion de librerias. 
df = pd.read_csv('product_demand.csv')
##cargar el conjunto de datos desde un csv

# Split the data into training and test sets
#preprocesado de datos, division de informacion en pronostico y prueba
X_train, X_test, y_train, y_test = train_test_split(df[['feature_1', 'feature_2', ...]], df['demand'], test_size=0.25, random_state=42)

# Normalize the data
#Normalizacion de datos. 
X_train_scaled = X_train.apply(StandardScaler().fit_transform)
X_test_scaled = X_test.apply(StandardScaler().fit_transform)

##Creacion del modelo perceptron.
mlp = MLPRegressor(hidden_layer_sizes=(128, 64), activation='relu', solver='adam', max_iter=1000)

# Train the model
#entrenar modelo.
mlp.fit(X_train_scaled, y_train)

# Evaluate the model on the test set
y_pred = mlp.predict(X_test_scaled)
print('Test R-squared:', mlp.score(X_test_scaled, y_test))

##evaluacion del modelo con un conjunto de datos de prueba. 
# Create a list of future dates
future_dates = pd.date_range('2023-11-08', periods=30, freq='D')

# Create a DataFrame with the future dates
future_df = pd.DataFrame({'date': future_dates})

# Forecast product demand for the future dates
future_demand = mlp.predict(future_df)

# Add the forecast demand to the DataFrame
future_df['demand'] = future_demand

# Print the forecast product demand
print(future_df)

##pronosticar la demanda.

##El codigo es de diseño sencillo.

