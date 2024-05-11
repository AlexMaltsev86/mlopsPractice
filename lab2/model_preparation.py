import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Получение данных обучения
df_train = pd.read_csv('./train/result_train.csv')

# Выделение признаков
X_train = df_train.drop('target', axis=1)
y_train = df_train['target']

# Создание модели
model = LinearRegression()
print("--- Model created")

# Обучение модели
model.fit(X_train, y_train)
print("--- Model trained")

# Сохранение модели
pickle.dump(model, open('model.pkl', 'wb'))