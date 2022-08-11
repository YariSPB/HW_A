# 1. На языке Python реализовать алгоритм (функцию) определения четности целого числа,
# который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути.
# Объяснить плюсы и минусы обеих реализаций.

# Реализация 1
# def isEven(value):return value%2==0

# плюсы:
# 1. простота и понятность, сложно сделать ошибку
# 2. логарифическое время (вероятно используется рекурсивный алгоритм Эвклида сложностью O(log(min(a,b))))
# минусы:
# 1. лишняя работа в логарифмическое время, потраченное на поиск GCD

# реализация 2. Чтение последнего бита, который определяет четность числа.
# плюсы:
# - O(1) время, так как считывается бинарное отображение числа, а точнее последний бит, который определяет нечетность.
# минусы:
# -сложность в восприятии, можно сделать ошибку

def isEven(value):
    return bin(value)[-1] != '1'


# 2 На языке Python (2.7) реализовать минимум
# по 2 класса реализовывающих циклический буфер FIFO.
# Объяснить плюсы и минусы каждой реализации.

# реализация 1. Линейная презентация
# плюсы:
# - Скорость, благодаря возможности сохранить Cache Locality, поскольку все элементы хранятся последовательно в куче в едином массиве в памяти
# и загружаются в кеш единым куском.
# минусы:
# - Ускорение может страдать, когда в массив записываются элементы разного типа или размера.

class FIFO_Linear:
    def __init__(self, size):
        self.size = size
        self.items = 0
        self.queue = [None] * size
        self.head = 0
        pass

    def get(self):
        if self.items == 0:
            raise Exception('Empty queue')
        value = self.queue[self.head]
        self.head = (self.head + 1) % self.size
        self.items -= 1
        return value

    def put(self, value):
        if self.items == self.size:
            raise Exception('Full capacity')
        tail = (self.head + self.items) % self.size
        self.queue[tail] = value
        self.items += 1

    def get_free(self):
        return self.items


# реализация 2. Linked List презентация
# плюсы:
# Хорошо для данных с разным размером, так как каждый элемент может хранится отдельно от предыдущего в куче
# и иметь свой доступ к памяти
# минусы :
# 1. Менее эффективное использвание Кеша и медлительность, поскольку для каждого элемента из кучи нужно будет использвать новую линию кеша.

class FIFO_Linked:
    def __init__(self, size):
        self.size = size
        curr = self.head = self.Node()
        self.items = 0
        for i in range(size - 1):
            node = self.Node()
            curr.next = node
            curr = node
        curr.next = self.head
        self.tail = curr

    class Node:
        def __init__(self):
            self.value = None
            self.next = None

    def get(self):
        if self.items == 0:
            raise Exception('Empty queue')
        value = self.head.value
        self.head = self.head.next
        self.items -= 1
        return value

    def put(self, value):
        if self.items == self.size:
            raise Exception('Full capacity')
        self.tail = self.tail.next
        self.tail.value = value
        self.items += 1

    def get_free(self):
        return self.items


# 3. На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам)
# отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел
# (в том числе и отсортированным).
# Объяснить почему вы считаете, что функция соответствует заданным критериям.

# Таким образом, массив может быть как маленьким так и большим. Отсортированным или не отсортированным.
# Также не указано, какие ограничения по памяти имеются и можно ли реализовать паралельное вычисление.
# Поэтому выбираю in-place Quicksort с делением по медиане n/2, чтобы удовлетворить любой из вышереперечисленных вариантов в
# логирифмическое время O(nlongn).
# Примущество данного решения в том, что оно:
# - не O(n*n)
# - делает O(nlongn) для уже отсортированного массива
# - in-place и не требует дополнительной памяти.
# Недостатком является усредненная производительность O(nlongn), которую можно было бы сделать O(N) в некоторых случаях, если были бы известны доп. детали.

# use in-place Quicksort with n/2 partition

def partition(arr, start, end):
    mid = (end + start) // 2
    pivot = arr[mid]
    (arr[mid], arr[end]) = (arr[end], arr[mid])
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i = i + 1
            # Swapping element at i with element at j
            (arr[i], arr[j]) = (arr[j], arr[i])
    return i + 1


def qsort(array, start, end):
    if start >= end:
        return
    m = partition(array, start, end)
    qsort(array, start, m - 1)
    qsort(array, m + 1, end)


