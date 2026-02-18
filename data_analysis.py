# Анализ данных транзакций
def analyze_transactions(transactions_df):
    print("Анализ транзакций...")
    
    # Топ-5 наиболее популярных услуг по количеству заказов
    popular_services = transactions_df['service'].value_counts().head(5)
    print("Топ-5 популярных услуг:")
    for service, count in popular_services.items():
        print(f"  {service}: {count} транзакций")
    
    # Средняя сумма транзакций по городам
    avg_amount_by_city = transactions_df.groupby('city')['amount'].mean()
    print("\nСредняя сумма транзакций по городам:")
    for city, avg_amount in avg_amount_by_city.items():
        print(f"  {city}: {avg_amount:.2f}")
    
    # Услуга с наибольшей выручкой
    revenue_by_service = transactions_df.groupby('service')['amount'].sum()
    max_revenue_service = revenue_by_service.idxmax()
    max_revenue = revenue_by_service.max()
    print(f"\nУслуга с наибольшей выручкой: {max_revenue_service} ({max_revenue:.2f})")
    
    # Процент транзакций по способам оплаты
    payment_distribution = transactions_df['payment_method'].value_counts(normalize=True) * 100
    print("\nПроцент транзакций по способам оплаты:")
    for method, percentage in payment_distribution.items():
        print(f"  {method}: {percentage:.2f}%")
    
    # Выручка за последний месяц
    last_month = transactions_df['transaction_date'].max().to_period('M')
    revenue_last_month = transactions_df[transactions_df['transaction_date'].dt.to_period('M') == last_month]['amount'].sum()
    print(f"\nВыручка за последний месяц: {revenue_last_month:.2f}")
    
    return {
        'popular_services': popular_services,
        'avg_amount_by_city': avg_amount_by_city,
        'max_revenue_service': max_revenue_service,
        'revenue_by_service': revenue_by_service,
        'payment_distribution': payment_distribution,
        'revenue_last_month': revenue_last_month
    }

# Получение результатов анализа
def get_analysis_results(transactions_df):
    return analyze_transactions(transactions_df)