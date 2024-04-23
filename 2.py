global_variable = "Глобальная переменная"

def test_function():
    local_variable = "Локальная переменная"
    print("Внутри функции:")
    print("Глобальная переменная:", global_variable)
    print("Локальная переменная:", local_variable)

# 1
print("До вызова функции:")
print("Глобальная переменная:", global_variable)

# 2
test_function()
