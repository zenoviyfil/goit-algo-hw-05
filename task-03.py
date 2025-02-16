import sys
from typing import List, Dict

# Функція для парсингу рядка логу
def parse_log_line(line: str) -> dict:
    parts = line.split(" ", 3)
    if len(parts) < 4:
        return {}
    
    date, time, level, message = parts
    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message.strip()
    }

# Функція для завантаження логів з файлу
def load_logs(file_path: str) -> List[dict]:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
    return logs

# Функція для фільтрації логів за рівнем
def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return [log for log in logs if log["level"].upper() == level.upper()]

# Функція для підрахунку записів за рівнем логування
def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts

# Функція для виведення результатів у вигляді таблиці
def display_log_counts(counts: Dict[str, int]):
    print(" Рівень логування   | Кількість  ")
    print("--------------------|------------")
    for level, count in counts.items():
        print(f" {level:<9}          | {count:<10} ")

# Основна функція
def main():
    # Перевіряємо наявність аргументів командного рядка
    if len(sys.argv) < 2:
        print("Використання: python script.py <шлях_до_файлу_логів> [<рівень_логування>]")
        return
    
    file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None
    
    logs = load_logs(file_path)
    
    # Якщо вказано рівень логування, фільтруємо записи
    if log_level:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
        
        filtered_logs = filter_logs_by_level(logs, log_level)
        print(f"\nДеталі логів для рівня {log_level.upper()}:")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} {log['level']} {log['message']}")
    else:
        # Підраховуємо кількість записів для кожного рівня
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

if __name__ == "__main__":
    main()
