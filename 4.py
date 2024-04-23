def calculate_statistics(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average
# 
numbers = [5, 10, 15, 20, 25]
min_value, max_value, avg_value = calculate_statistics(numbers)
print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)
print("Среднее значение:", avg_value)
