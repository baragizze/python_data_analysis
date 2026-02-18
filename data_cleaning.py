import pandas as pd

# Загрузка данных
def load_data():
    try:
        transactions_df = pd.read_excel('transactions_data.xlsx')
        clients_df = pd.read_json('clients_data.json')
        return transactions_df, clients_df
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        return None, None

# Очистка данных транзакций
def clean_transactions_data(df):
    print("Очистка данных транзакций...")

    # Удаление строк с пропущенными значениями
    df_cleaned = df.dropna(subset=['transaction_id', 'client_id', 'transaction_date'])
    
    # Очистка дат
    df_cleaned['transaction_date'] = pd.to_datetime(df_cleaned['transaction_date'], errors='coerce')
    
    # Удаление некорректных дат
    df_cleaned = df_cleaned[df_cleaned['transaction_date'].notna()]
    
    # Удаление отрицательных сумм
    df_cleaned = df_cleaned[df_cleaned['amount'] >= 0]

    # Удаление строк с некорректными значениями в service
    valid_services = [
        'Инвестиционное консультирование',
        'Налоговое планирование',
        'Структурирование капитала',
        'Управление активами',
        'Финансовое планирование'
    ]
    df_cleaned = df_cleaned[df_cleaned['service'].isin(valid_services) |
                           df_cleaned['service'].isna()]
    
    print(f"Очищено {len(df) - len(df_cleaned)} строк транзакций")
    return df_cleaned

# Очистка клиентских данных
def clean_clients_data(df):
    print("Очистка клиентских данных...")

    # Удаление строк с пропущенными client_id
    df_cleaned = df.dropna(subset=['id'])

    # Ограничение возраста
    df_cleaned = df_cleaned[(df_cleaned['age'] > 0)]

    # Удаление отрицательных значений капитала
    df_cleaned = df_cleaned[df_cleaned['net_worth'] >= 0]

    print(f"Очищено {len(df) - len(df_cleaned)} строк клиентов")
    return df_cleaned

# Функция подготовки данных
def prepare_data():
    # Загрузка данных
    transactions_df, clients_df = load_data()
    
    if transactions_df is None or clients_df is None:
        print("Не удалось загрузить данные")
        return None, None
    
    # Очистка данных
    transactions_cleaned = clean_transactions_data(transactions_df)
    clients_cleaned = clean_clients_data(clients_df)
    
    # Проверка уникальности client_id
    unique_clients = set(transactions_cleaned['client_id'].unique()) & set(clients_cleaned['id'].unique())
    print(f"Уникальных клиентов в обеих таблицах: {len(unique_clients)}")
    
    return transactions_cleaned, clients_cleaned

# Запуск подготовки данных
if __name__ == "__main__":
    transactions_df, clients_df = prepare_data()
    print("Подготовка данных завершена")