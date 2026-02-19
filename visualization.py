import matplotlib.pyplot as plt
import os

# Папка для сохранения визуализаций
OUTPUT_DIR = 'visualizations'

def ensure_output_dir():
    """Создать папку для визуализаций, если она не существует"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

# Распределение сумм транзакций
def plot_transaction_distribution(transactions_df):
    ensure_output_dir()
    plt.figure(figsize=(10, 6))
    plt.hist(transactions_df['amount'], bins=50, alpha=0.7)
    plt.title('Распределение сумм транзакций')
    plt.xlabel('Сумма транзакции')
    plt.ylabel('Количество')
    plt.grid(True)
    plt.savefig(os.path.join(OUTPUT_DIR, 'transaction_distribution.png'))
    print(f"График распределения сумм транзакций сохранен в {OUTPUT_DIR}/transaction_distribution.png")

# Диаграмма выручки по услугам
def plot_revenue_by_service(transactions_df):
    ensure_output_dir()
    revenue_by_service = transactions_df.groupby('service')['amount'].sum()

    plt.figure(figsize=(10, 6))
    bars = plt.bar(revenue_by_service.index, revenue_by_service.values)
    plt.title('Выручка по услугам')
    plt.xlabel('Услуга')
    plt.ylabel('Выручка')
    plt.xticks(rotation=45)

    # Добавление значений на столбцы
    for bar, value in zip(bars, revenue_by_service.values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{value:.2f}', ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'revenue_by_service.png'))
    print(f"График выручки по услугам сохранен в {OUTPUT_DIR}/revenue_by_service.png")

# График зависимости средней суммы транзакции от возраста
def plot_age_vs_transaction_amount(transactions_df):
    ensure_output_dir()
    # Сгруппируем данные по возрасту и рассчитаем среднюю сумму
    age_stats = transactions_df.groupby('age')['amount'].mean().reset_index()

    plt.figure(figsize=(12, 6))
    plt.plot(age_stats['age'], age_stats['amount'], marker='o', linewidth=2, markersize=6, color='#2196F3')
    plt.title('Средняя сумма транзакции по возрасту', fontsize=14, fontweight='bold')
    plt.xlabel('Возраст (лет)', fontsize=12)
    plt.ylabel('Средняя сумма транзакции (₽)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xticks(range(int(age_stats['age'].min()), int(age_stats['age'].max()) + 1, 5))

    # Добавим значения на точки
    for x, y in zip(age_stats['age'], age_stats['amount']):
        plt.text(x, y + 50, f'{y:.0f}', ha='center', va='bottom', fontsize=8, alpha=0.7)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'age_vs_transaction_amount.png'), dpi=150)
    print(f"График зависимости средней суммы транзакции от возраста сохранен в {OUTPUT_DIR}/age_vs_transaction_amount.png")

# Создание всех визуализаций
def create_visualizations(transactions_df):
    print("Создание визуализаций...")
    
    plot_transaction_distribution(transactions_df)
    plot_revenue_by_service(transactions_df)
    plot_age_vs_transaction_amount(transactions_df)
    
    print("Все визуализации созданы")
