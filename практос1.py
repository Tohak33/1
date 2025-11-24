import random

def get_board_size():
    while True:
        try:
            size = int(input("Введите размер игрового поля (минимум 3): "))
            if size >= 3:
                return size
            else:
                print("Размер поля должен быть не менее 3.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

def display_board(board):
    size = len(board)
    headers = [str(i + 1) for i in range(size)] 
    
    print("\n--- Игровое поле ---")
    
    col_headers = "   " + " | ".join(f"{h:2}" for h in headers)
    print(col_headers)
    print("  " + "---" * size + "--")

    for r in range(size):
        row_content = f"{r + 1:2} | " + " | ".join(f"{board[r][c]:2}" for c in range(size))
        print(row_content)
        if r < size - 1:
            print("  " + "---" * size + "--")
    print("-------------------\n")

def check_win(board, player):
    size = len(board)
    WIN_COUNT = 3
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for r in range(size):
        for c in range(size):
            if board[r][c] != player:
                continue

            for dr, dc in directions:
                count = 1
                for i in range(1, WIN_COUNT):
                    nr, nc = r + dr * i, c + dc * i
                    
                    if (0 <= nr < size and 
                        0 <= nc < size and 
                        board[nr][nc] == player):
                        count += 1
                    else:
                        break
                
                if count == WIN_COUNT:
                    return True
                    
    return False

def get_move(board, player):
    size = len(board)
    while True:
        try:
            move_input = input(f"Игрок '{player}', введите координаты хода (строка,столбец, например 1,2): ")
            
            r_in, c_in = map(int, move_input.split(','))
            
            r = r_in - 1 
            c = c_in - 1

            if 1 <= r_in <= size and 1 <= c_in <= size:
                if board[r][c] == ' ':
                    return r, c
                else:
                    print("Эта ячейка уже занята. Выберите другую.")
            else:
                print(f"Координаты должны быть от 1 до {size}.")
        except ValueError:
            print("Некорректный формат. Пожалуйста, введите два числа через запятую (например, 1,2).")
        except:
            print("Произошла ошибка ввода. Попробуйте снова.")

def start_game(size):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    
    players = ['X', 'O']
    current_player = random.choice(players)
    print(f"Первым ходит игрок: '{current_player}'")

    moves_made = 0 
    
    while True:
        display_board(board)
        
        row, col = get_move(board, current_player)
        
        board[row][col] = current_player
        moves_made += 1
        
        if check_win(board, current_player):
            display_board(board)
            print(f"Поздравляем! Игрок '{current_player}' победил, собрав 3 в ряд!")
            break
        
        elif moves_made == size * size:
            display_board(board)
            print("Ничья! Игровое поле заполнено.")
            break
            
        current_player = 'O' if current_player == 'X' else 'X'

def main():
    print("--- Добро пожаловать в игру Крестики-нолики! ---")
    
    while True:
        board_size = get_board_size()
        start_game(board_size)
        
        while True:
            play_again = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
            if play_again =='да':
                print("\n--- Запуск новой игры ---\n")
                break
            elif play_again in ['нет', 'no', 'н']:
                print("Спасибо за игру! До свидания.")
                return
            else:
                print("Некорректный ввод. Пожалуйста, введите 'да' или 'нет'.")

if __name__ == "__main__":
    main()
