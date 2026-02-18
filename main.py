import pandas as pd
from datetime import datetime
from data_cleaning import prepare_data
from data_analysis import get_analysis_results

def main():
    print("Запуск тестового задания...")

    # 1. Очистка и подготовка данных
    print("\n1. Очистка и подготовка данных...")
    transactions_df, clients_df = prepare_data()

    # 2. Анализ данных
    print("\n2. Анализ данных транзакций...")
    analysis_results = get_analysis_results(transactions_df)

if __name__ == "__main__":
    main()