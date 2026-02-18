import pandas as pd
from datetime import datetime
from data_cleaning import prepare_data

def main():
    print("Запуск тестового задания...")

    # 1. Очистка и подготовка данных
    print("\n1. Очистка и подготовка данных...")
    transactions_df, clients_df = prepare_data()

if __name__ == "__main__":
    main()