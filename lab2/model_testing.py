from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd
import pickle

# Загрузка модели
model = pickle.load(open('model.pkl', 'rb'))

# Загрузка тестовых данных
df_test = pd.read_csv('./test/result_test.csv')
X_test = df_test.drop("target", axis=1)
y_test = df_test["target"]

# Предсказание
predict = pd.DataFrame(model.predict(X_test))

# Результаты
print("--- Metrics:")
print(f"--- MAE - {mean_absolute_error(y_test, predict)}")
print(f"--- MSE - {mean_squared_error(y_test, predict)}")
print(f"--- RMSE - {mean_squared_error(y_test, predict)**0.5}")
print(f"--- r2 - {r2_score(y_test, predict, multioutput='variance_weighted')}")