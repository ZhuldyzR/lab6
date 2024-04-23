name = "Alice"
age = 30
formatted_string = "Привет, меня зовут {0} и мне {1} лет.".format(name, age)
print(formatted_string)

name = "Bob"
age = 25
formatted_string = "Привет, меня зовут {} и мне {} лет.".format(name, age)
print(formatted_string)

name = "Charlie"
age = 35
formatted_string = "Привет, меня зовут {name} и мне {age} лет.".format(name=name, age=age)
print(formatted_string)
