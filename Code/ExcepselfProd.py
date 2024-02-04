from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)

    # Erzeuge zwei Listen, um die Produkte der linken und rechten Seite zu speichern
    left_products = [1] * n
    right_products = [1] * n
    result = [1] * n

    # Berechne die Produkte der linken Seite
    left_product = 1
    for i in range(1, n):
        left_product *= nums[i - 1]
        left_products[i] = left_product

    # Berechne die Produkte der rechten Seite
    right_product = 1
    for i in range(n - 2, -1, -1):
        right_product *= nums[i + 1]
        right_products[i] = right_product

    # Multipliziere die Produkte der linken und rechten Seite
    for i in range(n):
        result[i] = left_products[i] * right_products[i]

    return result


print(productExceptSelf([1, 2, 3, 4]))
