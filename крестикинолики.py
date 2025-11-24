import random, os
from datetime import datetime

STATS_DIR, STATS_FILE_NAME = "tictactoe_stats", "stats.txt"
STATS_FILE = os.path.join(STATS_DIR, STATS_FILE_NAME)
WIN_COUNT = 3

def setup_stats():
    global STATS_FILE
    try:
        if not os.path.exists(STATS_DIR): os.makedirs(STATS_DIR)
        if not os.path.exists(STATS_FILE):
            with open(STATS_FILE, 'w', encoding='utf-8') as f: f.write("Дата и время | Размер поля | Победитель\n")
    except OSError:
        STATS_FILE = None

def save_stats(winner, size):
    if STATS_FILE is None: return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result_line = f"{timestamp} | {size}x{size} | {winner}\n"
    try:
        with open(STATS_FILE, 'a', encoding='utf-8') as f: f.write(result_line)
    except IOError: pass

def get_board_size():
    while True:
        try:
            size_input = input("Введите размер игрового поля (минимум 3): ")
            size = int(size_input)
            if size >= 3: return size
            print("Размер поля должен быть не менее 3.")
        except ValueError: print("Некорректный ввод. Пожалуйста, введите целое число.")

def display_board(board):
    size = len(board)
    print("\n--- Игровое поле ---")
    print("   " + "   ".join(str(i + 1) for i in range(size)))
    separator = "-" * (size * 4 + 7)
    print(separator)
    for r in range(size):
        row_cells = []
        for c in range(size):
            cell_content = board[r][c]
            if cell_content == ' ': row_cells.append('.')
            else: row_cells.append(cell_content)
        row_content = f"{r + 1}: " + " | ".join(row_cells)
        print(row_content)
    print(separator)
    print("-------------------\n")

def check_win(board, player):
    size = len(board)
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for r in range(size):
        for c in range(size):
            if board[r][c] != player: continue
            for dr, dc in directions:
                count = 1
                for i in range(1, WIN_COUNT):
                    nr, nc = r + dr * i, c + dc * i
                    is_in_bounds = (0 <= nr < size) and (0 <= nc < size)
                    if is_in_bounds and board[nr][nc] == player: count += 1
                    else: break
                if count == WIN_COUNT: return True
    return False

def get_move(board, player):
    size = len(board)
    while True:
        try:
            move_input = input(f"Игрок '{player}', введите координаты (строка,столбец, например 1,2): ")
            parts = move_input.split(',')
            r_in = int(parts[0].strip())
            c_in = int(parts[1].strip())
            r, c = r_in - 1, c_in - 1
            if 1 <= r_in <= size and 1 <= c_in <= size:
                if board[r][c] == ' ': return r, c
                print("Эта ячейка уже занята. Выберите другую.")
            else: print(f"Координаты должны быть от 1 до {size}.")
        except (ValueError, IndexError): print("Некорректный формат. Введите два числа через запятую (например, 1,2).")
        except Exception: print("Произошла ошибка ввода. Попробуйте снова.")

def start_game(size):
    board = [[' ' for _ in range(size)] for _ in range(size)] 
    current_player = random.choice(['X', 'O'])
    print(f"Первым ходит игрок: '{current_player}'")
    moves_made, winner = 0, None
    while True:
        display_board(board)
        row, col = get_move(board, current_player)
        board[row][col] = current_player
        moves_made += 1
        if check_win(board, current_player): winner = current_player; break
        elif moves_made == size * size: winner = "Ничья"; break
        if current_player == 'X': current_player = 'O'
        else: current_player = 'X'
    display_board(board)
    if winner == "Ничья": print("Ничья! Игровое поле заполнено.")
    else: print(f"Поздравляем! Игрок '{winner}' победил, собрав {WIN_COUNT} в ряд!")
    save_stats(winner, size)

def main():
    print("--- Добро пожаловать в игру Крестики-нолики! ---") 
    setup_stats()
    while True:
        board_size = get_board_size()
        start_game(board_size) 
        while True:
            play_again = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
            if play_again == 'да': print("\n--- Запуск новой игры ---\n"); break
            elif play_again in ['нет', 'no', 'н']: print("Спасибо за игру! До свидания."); return
            else: print("Некорректный ввод. Пожалуйста, введите 'да' или 'нет'.")

if __name__ == "__main__":
    main()