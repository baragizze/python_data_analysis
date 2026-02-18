import pandas as pd

# Объединение данных транзакций и клиентских данных
def merge_data(transactions_df, clients_df):
    print("Объединение данных...")

    # Объединение таблиц по client_id (transactions) и id (clients)
    merged_df = pd.merge(transactions_df, clients_df, left_on='client_id', right_on='id', how='inner')

    print(f"Объединено {len(merged_df)} записей")
    
    return merged_df

# Анализ по уровням активов
def analyze_by_capital_levels(merged_df):
    print("\nАнализ по уровням активов...")

    # Создание новой колонки с уровнями активов
    def categorize_net_worth(net_worth):
        if net_worth < 100000:
            return 'Низкий капитал'
        elif net_worth <= 1000000:
            return 'Средний капитал'
        else:
            return 'Высокий капитал'
    
    merged_df['capital_category'] = merged_df['net_worth'].apply(categorize_net_worth)

    # Определение клиентов с наибольшей выручкой
    revenue_by_category = merged_df.groupby('capital_category')['amount'].agg(['sum', 'count', 'mean']).sort_values('sum', ascending=False)

    print("\nКатегории клиентов по уровню активов:")
    for category, row in revenue_by_category.iterrows():
        print(f"  {category}:")
        print(f"    Выручка: {row['sum']:.2f}")
        print(f"    Количество транзакций: {int(row['count'])}")
        print(f"    Средний чек: {row['mean']:.2f}")

    # Определение категории с наибольшей выручкой
    top_category = revenue_by_category.index[0]
    top_revenue = revenue_by_category.iloc[0]['sum']
    total_revenue = merged_df['amount'].sum()
    revenue_share = (top_revenue / total_revenue) * 100

    print(f"\nНаибольшую выручку приносит категория '{top_category}':")
    print(f"  Сумма: {top_revenue:.2f}")
    print(f"  Доля от общей выручки: {revenue_share:.1f}%")

    return revenue_by_category