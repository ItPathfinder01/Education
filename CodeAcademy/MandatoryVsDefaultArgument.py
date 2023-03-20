def test(param=5):
    print(param)

test() # если аргумент при вызове функции не указан будет использовано дефолтное значение - param=5
test("Hallo")

var = input()
print("Your name", var)
print("Is it a string?", not var.strip().isdigit())
