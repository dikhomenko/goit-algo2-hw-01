# Реалізуйте функцію, яка знаходить максимальний та мінімальний елементи в масиві,
# використовуючи метод «розділяй і володарюй».
# Функція приймає масив чисел довільної довжини.
# Використано рекурсивний підхід.
# Повертається кортеж значень (мінімум, максимум).
# Складність алгоритму — O(n).


def find_max_and_min(arr: int) -> tuple:
    # base cases
    if len(arr) == 0:
        raise ValueError("Array cannot be empty")

    if len(arr) == 1:
        return arr[0], arr[0]

    mid = len(arr) // 2
    left_max, left_min = find_max_and_min(arr[:mid])
    right_max, right_min = find_max_and_min(arr[mid:])

    return max(left_max, right_max), min(left_min, right_min)


if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9]
    (max_val, min_val) = find_max_and_min(arr)
    print(f"Max: {max_val}, Min: {min_val}")


# Time complexity: O(n)
# Space complexity: O(log n) (due to recursion stack).
