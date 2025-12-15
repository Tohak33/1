import csv
import json

animals_data = [
    {'Животное': 'Медведь', 'Среда обитания': 'Лес'},
    {'Животное': 'Дельфин', 'Среда обитания': 'Океан'},
    {'Животное': 'Верблюд', 'Среда обитания': 'Пустыня'}
]

csv_filename = 'animals.csv'
fieldnames = ['Животное', 'Среда обитания']
json_filename = 'zoo.json'
data_json = []

with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(animals_data)

print(f"Файл '{csv_filename}' создан.")

with open(csv_filename, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data_json.append(row)

with open(json_filename, 'w', encoding='utf-8') as jsonfile:
    json.dump(data_json, jsonfile, ensure_ascii=False, indent=4)

print(f"Данные преобразованы и сохранены в '{json_filename}'.")







people_data = [
    {'Имя': 'Анна', 'Возраст': 28, 'Город': 'Москва', 'Должность': 'Разработчик'},
    {'Имя': 'Иван', 'Возраст': 34, 'Город': 'Санкт-Петербург', 'Должность': 'Менеджер'},
    {'Имя': 'Мария', 'Возраст': 25, 'Город': 'Казань', 'Должность': 'Дизайнер'},
    {'Имя': 'Петр', 'Возраст': 41, 'Город': 'Екатеринбург', 'Должность': 'Аналитик'},
    {'Имя': 'Елена', 'Возраст': 'Ошибка', 'Город': 'Сочи', 'Должность': 'Бухгалтер'},
    {'Имя': 'Олег', 'Возраст': 31, 'Город': 'Новосибирск', 'Должность': 'Инженер'}
]
csv_file = 'employees_data.csv'
json_file = 'employees_data.json'
fieldnames = ['Имя', 'Возраст', 'Город', 'Должность']

with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(people_data)

print(f"Сотрудники старше 30 из файла '{csv_file}':")

try:
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            try:
                age = int(row['Возраст'])
                
                if age > 30:
                    print(row['Имя'])
                    
            except ValueError:
                continue
                
except FileNotFoundError:
    print("Файл не найден.")

def convert_csv_to_json(csv_path: str, json_path: str) -> None:
    data = []
    
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    with open(json_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)
    
    print(f"Конвертация CSV в JSON завершена. Файл: '{json_path}'")


def convert_json_to_csv(json_path: str, csv_path: str) -> None:
    with open(json_path, 'r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)

    if not data:
        return
        
    fieldnames = list(data[0].keys())

    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
        
    print(f"Конвертация JSON в CSV завершена. Файл: '{csv_path}'")

convert_csv_to_json(csv_file, json_file)

new_csv_file = 'employees_data_final.csv'
convert_json_to_csv(json_file, new_csv_file)