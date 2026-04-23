import 'package:practos4/practos4.dart' as practos4;
import 'dart:io';

class Cup{
  String color;

  Cup(this.color);
  }

class Human{
  String name;
  int age;

  Human(this.name, this.age);

  void Drink(Cup){
  print("${name} пьет из ${Cup.color} кружки");
}
}

class Wardrobe{
  List<String> topShelf=[];
  List<String> middleShelf=[];
  List<String> bottomShelf=[];
  
  void addItemTop(String item,){
    topShelf.add(item);
    print("Вы положили ${item} на верхнюю полку");
  }

  void addItemMiddle(String item,){
    middleShelf.add(item);
    print("Вы положили ${item} на среднюю полку");
  }

  void addItemBottom(String item,){
    bottomShelf.add(item);
    print("Вы положили ${item} на нижнюю полку");
  }

  void takeItemTop(String item){
    if(topShelf.contains(item)){
      topShelf.remove(item);
      print("Вы взяли ${item} с верхней полки");
    } else {
      print("${item} нет на верхней полке");
    }
  }

  void takeItemMiddle(String item){
    if(middleShelf.contains(item)){
      middleShelf.remove(item);
      print("Вы взяли ${item} с средней полки");
    } else {
      print("${item} нет на средней полке");
    }
  }

  void takeItemBottom(String item){
    if(bottomShelf.contains(item)){
      bottomShelf.remove(item);
      print("Вы взяли ${item} с нижней полки");
    } else {
      print("${item} нет на нижней полке");
    }
  }
}

class Grif{
  int maxWeight;
  List<Blin> leftSide=[];
  List<Blin> rightSide=[];
  Grif(this.maxWeight, this.leftSide, this.rightSide);

  void knowWeight(){
    print("Сейчас на штанге ${getTotalWeight()} кг");
  }
  int getTotalWeight(){
    int total = 0;
    for(var blin in leftSide){
      total += blin.weight;
    }
    for(var blin in rightSide){
      total += blin.weight;
    }
    return total;

  }
  void AddLeft(Blin blin){
    if(getTotalWeight() + blin.weight <= maxWeight){
      leftSide.add(blin);
      print("Вы положили блин весом ${blin.weight} на левую сторону грифа");
    } else {
      print("Невозможно положить блин, превышен максимальный вес грифа");
    }
  }

  void AddRight(Blin blin){
    if(getTotalWeight() + blin.weight <= maxWeight){
      rightSide.add(blin);
      print("Вы положили блин весом ${blin.weight} на правую сторону грифа");
    } else {
      print("Невозможно положить блин, превышен максимальный вес грифа");
    }
  }
}

class Blin{
  int weight;
  Blin(this.weight);
}

class MoneyConverter{
  double rubToUsd;
  double usdToRub;
  MoneyConverter(this.rubToUsd, this.usdToRub);

  void rubToDollar(int rub){
    print("${rub} рублей это ${rub * rubToUsd} долларов");
  }

  void dollarToRub(int usd){
    print("${usd} долларов это ${usd * usdToRub} рублей");
  }
}

class Garage<T>{
  List<T> items = [];
  void addItem(T item){
    items.add(item);
    print("Вы добавили ${item} в гараж");
  }
  void removeItem(T item){
    if(items.contains(item)){
      items.remove(item);
      print("Вы удалили ${item} из гаража");
    } else {
      print("${item} нет в гараже");
    }
  }
}

class Number{
  int value;
  Number(this.value);
  int operator +(Number other){
    return (value + other.value);
  }
  int operator -(Number other){
    return (value - other.value);
  }
  int operator *(Number other){
    return (value * other.value);
  }
  int operator /(Number other){
    if(other.value != 0){
      return (value ~/ other.value);
    } else {
      print("Ошибка: деление на ноль");
      return 0;
    }
}
}

enum Condition{
  drive,
  stop,
  turn;
}
class Car{
  String model;
  Condition condition;

  Car(this.model, this.condition);

  void drive(){
    condition = Condition.drive;
    print("${model} едет");
  }

  void stop(){
    condition = Condition.stop;
    print("${model} остановилась");
  }

  void turn(){
    condition = Condition.turn;
    print("${model} повернула");
  }
}

class Figure{
  void area(){
    print("Площадь фигуры");
  }
}
class Square extends Figure{
  double side;
  Square(this.side);
  @override
  void area(){
    print("Площадь квадрата: ${side * side}");
  }
}
class Circle extends Figure{
  double radius;
  Circle(this.radius);
  @override
  void area(){
    print("Площадь круга: ${3.14 * radius * radius}");
  }
}

class Number2{
  int value;
  Number2(this.value);
  void toTen(){
    print("Число в десятичной системе: ${value}");
  }
  void toTwo(){
    print("Число в двоичной системе: ${value.toRadixString(2)}");
  }
  void toSixteen(){
    print("Число в шестнадцатеричной системе: ${value.toRadixString(16)}");
  }
  void toEight(){
    print("Число в восьмеричной системе: ${value.toRadixString(8)}");
  }

}

abstract class Figure2{
  String name;
  Figure2(this.name);
  double getArea();
}

class Square1 extends Figure2{
  double side;
  Square1(String name, this.side) : super(name);
  @override
  double getArea(){
    return side * side;
  }
}

class Circle1 extends Figure2{
  double radius;
  Circle1(String name, this.radius) : super(name);
  @override
  double getArea(){
    return 3.14 * radius * radius;
  }
}

class GeometryFigures{
  List<Figure2> figures =[];
  void addFigure(Figure2 figure){
    figures.add(figure);
    print("Вы добавили фигуру ${figure.name} в коллекцию");
  }
  Figure2 calculateAreas(){
    Figure2 maxShape=figures[0];
    for(var figure in figures){
      print("Площадь фигуры ${figure.name}: ${figure.getArea()}");
      if(maxShape == null || figure.getArea() > maxShape.getArea()){
        maxShape = figure;
      }
    }
    return maxShape;
  }
  void printMaxAreaFigure(){
    Figure2 maxShape = calculateAreas();
    print("Фигура с максимальной площадью: ${maxShape.name} с площадью ${maxShape.getArea()}");
  }
}

abstract class Items{
  String name;
  Items(this.name);
}
class Fork extends Items{
  Fork(String name) : super(name);
}
class Lozhka extends Items{
  Lozhka(String name) : super(name);
}
class Knife extends Items{
  Knife(String name) : super(name);
}

class Table{
  List<Items> items = [];
  void addItem(Items item){
    items.add(item);
    print("Вы положили ${item.name} на стол");
  }
  void removeItem(Items item){
    if(items.contains(item)){
      items.remove(item);
      print("Вы убрали ${item.name} со стола");
    } else {
      print("${item.name} нет на столе");
  }
  }
}

void main(List<String> arguments) {
  var cup1 = Cup("красная");
  var human1 = Human("Алексей", 30);
  human1.Drink(cup1);

  var wardrobe = Wardrobe();
  wardrobe.addItemTop("рубашка");
  wardrobe.addItemMiddle("брюки");
  wardrobe.addItemBottom("носки");
  wardrobe.takeItemTop("рубашка");
  wardrobe.takeItemMiddle("брюки");
  wardrobe.takeItemBottom("носки");

  var blin1 = Blin(10);
  var blin2 = Blin(25);
  var blin3 = Blin(50);
  var grif = Grif(400, [], []);
  grif.AddLeft(blin1);
  grif.AddRight(blin1);
  grif.AddLeft(blin3);
  grif.AddLeft(blin3);
  grif.knowWeight();

  var converter = MoneyConverter(0.07, 70.0);
  converter.rubToDollar(1000);
  converter.dollarToRub(1000);

  var garage = Garage();
  garage.addItem("машина");
  garage.addItem("велосипед");
  garage.removeItem("машина");

  var a = Number(5);
  var b = Number(10);
  print("Сумма: ${a + b}");
  print("Разность: ${a - b}");
  print("Произведение: ${a * b}");
  print("Частное: ${a / b}");

  var car = Car("BMW", Condition.stop);
  car.drive();
  car.turn();
  car.stop();

  var square = Square(4);
  var circle = Circle(3);
  square.area();
  circle.area();

  var number2 = Number2(255);
  number2.toTen();
  number2.toTwo();
  number2.toSixteen();
  number2.toEight();

  var geometryFigures = GeometryFigures();
  geometryFigures.addFigure(Square1("Квадрат", 4));
  geometryFigures.addFigure(Circle1("Круг", 3));
  geometryFigures.printMaxAreaFigure();

  var table = Table();
  var fork = Fork("вилка");
  var lozhka = Lozhka("ложка");
  var knife = Knife("нож");
  table.addItem(fork);
  table.addItem(lozhka);
  table.addItem(knife);
  table.removeItem(lozhka);

}

