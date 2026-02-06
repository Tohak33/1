import 'dart:io';
import 'dart:math';

void main() {
  print('a: ');
  double a = double.parse(stdin.readLineSync()!);

  print('b: ');
  double b = double.parse(stdin.readLineSync()!);

  print('op: ');
  String op = stdin.readLineSync()!;




  switch (op) {
    case '+': 
    print(a + b); 
    break;
    
    case '-': 
    print(a - b); 
    break;

    case '*': 
    print(a * b); 
    break;

    case '/': 
    if(b==0){
      print("нельзя делить на 0");
    }
    else{
      print(a / b);
    }
    break;
    
    case '~/': 
    if(b==0){
      print("нельзя делить на 0");
    }
    else{
      print(a / b);
    }
    break;

    case '%': 
    if(b==0){
      print("нельзя делить на 0");
    }
    else{
      print(a / b);
    } 
    break;

    case 'pow': 
    print(pow(a, b)); 
    break;

    case '==': 
    print(a == b); 
    break;

    case '!=': 
    print(a != b); 
    break;

    case '>':  
    print(a > b); 
    break;

    case '<':  
    print(a < b); 
    break;

    case '>=': 
    print(a >= b); 
    break;

    case '<=': 
    print(a <= b); 
    break;

    case '&&': 
    print((a > 0) && (b > 0)); break;
    case '||': 
    print((a > 0) || (b > 0)); break;
    case '!':  
    print(!(a == b)); break;
    default: print('error');
  }
}
