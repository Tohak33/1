import 'dart:io';

// --- ЗАДАЧА 1 ---
String formatName(String firstName, String lastName, [String? otchestvo]) {
  if (otchestvo != null && otchestvo.isNotEmpty) {
    return '$lastName $firstName $otchestvo';
  }
  return '$lastName $firstName';
}

// --- ЗАДАЧА 2 ---
num? calculate(num firstNumber, num secondNumber, String operation) {
  if (operation == '/' && secondNumber == 0) return null;
  switch (operation) {
    case '+': return firstNumber + secondNumber;
    case '-': return firstNumber - secondNumber;
    case '*': return firstNumber * secondNumber;
    case '/': return firstNumber / secondNumber;
    default: return null;
  }
}

// --- ЗАДАЧА 3 ---
void countSigns(List<int> numbers) {
  int positiveCount = 0, negativeCount = 0, zeroCount = 0;
  for (int number in numbers) {
    if (number > 0) positiveCount++;
    else if (number < 0) negativeCount++;
    else zeroCount++;
  }
  print('Положительных: $positiveCount, Отрицательных: $negativeCount, Нулевых: $zeroCount');
}

// --- ЗАДАЧА 4 ---
List<int> transformList(List<int> numbers, int Function(int) transform) {
  List<int> resultList = [];
  for (int number in numbers) {
    resultList.add(transform(number));
  }
  return resultList;
}


int multiplyByTwo(int number) {
  return number * 2;
}

// --- ЗАДАЧА 5 ---
int sumDigits(int number) {
  if (number == 0) return 0;
  return (number % 10) + sumDigits(number ~/ 10);
}


void main() {

  print('--- Задача 1: Форматирование ФИО ---');
  stdout.write('Введите имя: ');
  String firstName = stdin.readLineSync()!;
  
  stdout.write('Введите фамилию: ');
  String lastName = stdin.readLineSync()!;
  
  stdout.write('Введите отчество (или просто нажмите Enter, если его нет): ');
  String otchestvo = stdin.readLineSync()!;
  
  print('Результат: ${formatName(firstName, lastName, otchestvo.isEmpty ? null : otchestvo)}\n');

  print('--- Задача 2: Простейший калькулятор ---');
  stdout.write('Введите первое число: ');
  num firstNumber = num.parse(stdin.readLineSync()!);
  
  stdout.write('Введите второе число: ');
  num secondNumber = num.parse(stdin.readLineSync()!);
  
  stdout.write('Введите знак операции (+, -, *, /): ');
  String operation = stdin.readLineSync()!;
  
  print('Результат вычисления: ${calculate(firstNumber, secondNumber, operation)}\n');


  print('--- Задачи 3 и 4: Работа со списками ---');
  stdout.write('список: 1, 2, 3, -4, 5 ');
  List<int> numbersList =[1, 2, 3, -4, 5];  
  print('\nАнализ вашего списка (Задача 3):');
  countSigns(numbersList);
  
  print('\nсписок, умноженный на 2 (Задача 4):');
  List<int> transformedNumbers = transformList(numbersList, multiplyByTwo);
  print('Результат: $transformedNumbers\n');


  print('--- Задача 5: Сумма цифр числа ---');
  stdout.write('Введите целое число: ');
  int inputNumber = int.parse(stdin.readLineSync()!);
  
  print('Сумма цифр числа $inputNumber равна: ${sumDigits(inputNumber)}\n');
}