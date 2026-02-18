from data_cleaning import prepare_data
from data_analysis import get_analysis_results
from data_merge import merge_data, analyze_by_capital_levels

def main():
    print("Запуск тестового задания...")

    # 1. Очистка и подготовка данных
    print("\n1. Очистка и подготовка данных...")
    transactions_df, clients_df = prepare_data()

    # 2. Анализ данных
    print("\n2. Анализ данных транзакций...")
    get_analysis_results(transactions_df)

    # 3. Объединение данных и анализ по уровням активов
    print("\n3. Объединение данных и анализ по уровням активов...")
    merged_df = merge_data(transactions_df, clients_df)
    analyze_by_capital_levels(merged_df)


if __name__ == "__main__":
    main()