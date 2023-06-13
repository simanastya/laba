def print_odd_numbers(arr):
    for num in arr:
        if num % 2 != 0:
            print(num)

# Пример использования
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_odd_numbers(numbers)