import numpy as np

# Функция для проверки работы алгоритма
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    

# Функция для угадывания числа
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Вводим переменную-счетчик попыток
    count = 0
    # Максимальное и минимальное значения в последовательности
    max_value = 101
    min_value = 0

    # Создаем бесконечный цикл
    while True:
        # Добавляем одну попытку
        count += 1
        # Воспользуемся методом бинарного поиска
        # Находим середину последовательности предполагаемых значений
        middle = (max_value + min_value) // 2
        # Если значение совпадает с загаданным числом, выходим из цикла
        if middle == number:
            break
        # Если загаданное число меньше середины, присваиваем это значение минимуму последовательности и работаем с правой половиной
        elif middle < number:
            min_value = middle
        # В противном случае присваиваем это значение максимуму и ищем в правой половине
        else:
            max_value = middle


    return count


# Проверяем работу алгоритма
print('Run benchmarking for game_core_v3: ', end='')
# RUN
if __name__ == '__main__':
    score_game(game_core_v3)