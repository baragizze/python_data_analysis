import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from datetime import timedelta

# Подготовка данных для прогнозирования
def prepare_forecast_data(transactions_df):
    # Преобразование даты в числовой формат (дни с начала)
    transactions_df['date_numeric'] = (transactions_df['transaction_date'] - transactions_df['transaction_date'].min()).dt.days

    # Группировка по дате
    transactions_df['date_only'] = transactions_df['transaction_date'].dt.date
    daily_data = transactions_df.groupby('date_only')['amount'].sum().reset_index()
    daily_data['transaction_date'] = pd.to_datetime(daily_data['date_only'])

    # Создание временного ряда с ежедневными значениями
    date_range = pd.date_range(start=daily_data['transaction_date'].min(), end=daily_data['transaction_date'].max(), freq='D')

    complete_df = pd.DataFrame({'transaction_date': date_range})
    complete_df = complete_df.merge(daily_data, on='transaction_date', how='left')
    complete_df['amount'] = complete_df['amount'].fillna(0)

    # Добавление признаков
    complete_df['day_of_year'] = complete_df['transaction_date'].dt.dayofyear
    complete_df['month'] = complete_df['transaction_date'].dt.month

    return complete_df

# Предсказание следующего месяца
def predict_next_month(transactions_df):
    print("Прогнозирование спроса...")
    
    df = prepare_forecast_data(transactions_df)

    # Создание признаков для модели
    x = df[['day_of_year', 'month']].values
    y = df['amount'].values

    # Разделение на обучающую и тестовую выборки
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Создание модели
    model = LinearRegression()
    model.fit(x_train, y_train)

    print("Прогноз спроса выполнен")

    # Генерация дат для прогнозирования на следующий месяц (30 дней)
    last_date = df['transaction_date'].max()
    forecast_dates = pd.date_range(start=last_date + timedelta(days=1), periods=30, freq='D')
    
    # Создание признаков для прогнозирования
    forecast_features = np.column_stack([
        forecast_dates.dayofyear,
        forecast_dates.month
    ])
    
    # Предсказание значений
    forecast_values = model.predict(forecast_features)
    
    # Вывод результатов в строку
    print(f"\nПрогноз на следующий месяц ({forecast_dates.min().strftime('%d-%m-%Y')} по {forecast_dates.max().strftime('%d-%m-%Y')}):")
    print(f"Общая выручка: {forecast_values.sum():.2f} | Средняя в день: {forecast_values.mean():.2f} | Мин: {forecast_values.min():.2f} | Макс: {forecast_values.max():.2f}")

    return model, forecast_dates, forecast_values