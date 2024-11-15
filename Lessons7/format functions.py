text = "Python"
result = "{:<10}".format(text)
print(result + "is awesome!")

result = "{1}, {0}".format("world", "hello")
print(result)

result = "Name: {name}, Age: {age}".format(name="Alice", age=25)
print(result)

name = "John"
age = 30
result = "Name: {}, Age: {}".format(name, age)
print(result)

original_string = "PyThOn iS aWeSoMe!"
modified_string = original_string.swapcase()
print(modified_string)