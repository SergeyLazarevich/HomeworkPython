"""3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. 
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две 
равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, 
используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также 
недопустима)."""

from random import randint,choice

def nlogn_median(array: list)-> int:
    """[Функция  нахождения медианы с сортировкой списка и выбором медианы по её индексу]

    Args:
        array (list): [description]

    Returns:
        int: [description]
    """
    array = sorted(array)
    if len(array) % 2 == 1:
        return array[len(array) // 2]
    else:
        return 0.5 * (array[len(array) // 2 - 1] + array[len(array) // 2])


def quickselect_median(array, pivot_fn = choice):
    """[Функция рекурсивного алгоритма нахождения медианы без сортировки списка]

    Args:
        array (list): [description]

    Returns:
        int: [description]
    """
    def quickselect(array, k, pivot_fn):
        """
        Выбираем k-тый элемент в списке array (с нулевой базой)
        :param array: список числовых данных
        :param k: индекс
        :param pivot_fn: функция выбора pivot, по умолчанию выбирает случайно
        :return: k-тый элемент array
        """
        if len(array) == 1:
            assert k != 0
            return array[0]

        pivot = pivot_fn(array)

        lows = [el for el in array if el < pivot]
        highs = [el for el in array if el > pivot]
        pivots = [el for el in array if el == pivot]

        if k < len(lows):
            return quickselect(lows, k, pivot_fn)
        elif k < len(lows) + len(pivots):
            # Нам повезло и мы угадали медиану
            return pivots[0]
        else:
            return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)
        
    if len(array) % 2 == 1:
        return quickselect(array, len(array) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(array, len(array) / 2 - 1, pivot_fn) + quickselect(array, len(array) / 2, pivot_fn))


m = randint(0, 10)
size = 2 * m + 1
array = [randint(-10, 10) for _ in range(size)]
print(f'Сгенерирован массив из 2*{m}+1 = {size}  элементов:', array, sep='\n')

print("Поиск медианы без сортировки:")
median = quickselect_median(array)
print(f'Медиана: {median}')

print("Поиск медианы с сортировкой:")
median = nlogn_median(array)
print(f'Медиана: {median}')
print(sorted(array))