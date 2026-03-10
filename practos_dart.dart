void main() {
  var journal = {
    'Иванов': {'Математика': 5, 'Физика': 4, 'Программирование': 5},
    'Петров': {'Математика': 3, 'Физика': 2, 'Программирование': 4},
    'Сидоров': {'Математика': 5, 'Физика': 5, 'Программирование': 5},
    'Смирнов': {'Математика': 4, 'Физика': 4, 'Программирование': 3},
    'Кузнецов': {'Математика': 3, 'Физика': 3, 'Программирование': 2},
  };

 
  var subjects = ['Математика', 'Физика', 'Программирование']; 

  var excellent = [];
  var good = [];
  var others = [];
  
  journal.forEach((studentName, grades) {
    int sum = grades.values.reduce((a, b) => a + b);
    double avg = sum / grades.length;
    
    if (avg >= 4.5) {
      excellent.add(studentName);
    } 
    else if (avg >= 3.5) {
      good.add(studentName);
    } 
    else {
      others.add(studentName);
    }
  });
  print('1. Отличники: $excellent\nХорошисты: $good\nОстальные: $others');

  var counts = {2: 0, 3: 0, 4: 0, 5: 0};
  for (var grades in journal.values) {
    for (var grade in grades.values) {
      counts[grade] = counts[grade]! + 1;
    }
  }
  print('\n2. Оценки: $counts');

  print('\n3. Пятерки по предметам:');
  for (var subject in subjects) {
    var studentsWithFives = [];
    for (var studentName in journal.keys) {
      if (journal[studentName]![subject] == 5) {
        studentsWithFives.add(studentName);
      }
    }

    print('$subject: $studentsWithFives');
  }

  var subjectsWithoutTwos = [];
  for (var subject in subjects) {
    bool hasTwo = journal.values.any((grades) => grades[subject] == 2);
    if (hasTwo == false) {
      subjectsWithoutTwos.add(subject);
    }
  }
  print('\n4. Без двоек: $subjectsWithoutTwos');

  int maxTwosCount = 0;
  String worstSubject = '';
  for (var subject in subjects) {
    int currentTwosCount = journal.values.where((grades) => grades[subject] == 2).length;
    
    if (currentTwosCount > maxTwosCount) {
      maxTwosCount = currentTwosCount;
      worstSubject = subject;
    }
  }
  print('\n5. Худший предмет: $worstSubject ($maxTwosCount двоек)');

  int maxFivesCount = 0;
  var topStudents = [];
  journal.forEach((studentName, grades) {
    int currentFivesCount = grades.values.where((grade) => grade == 5).length;
    
    if (currentFivesCount > maxFivesCount) {
      maxFivesCount = currentFivesCount;
      topStudents = [studentName];
    } else if (currentFivesCount == maxFivesCount && maxFivesCount > 0) {
      topStudents.add(studentName);
    }
  });
  print('\n6. Больше всего пятерок: $topStudents (кол-во: $maxFivesCount)');

  print('\n7. Оценки ниже 4:');
  journal.forEach((studentName, grades) {
    var badSubjects = grades.keys.where((subject) => grades[subject]! < 4).toList();
    if (badSubjects.isNotEmpty) {
      print('$studentName: ${badSubjects.length} шт. (${badSubjects.join(', ')})');
    }
  });

  print('\n8. Пары Студент-Предмет (5):');
  journal.forEach((studentName, grades) {
    grades.forEach((subject, grade) {
      if (grade == 5) {
        print('$studentName - $subject');
      }
    });
  });
}