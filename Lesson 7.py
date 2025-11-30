
#Не используеться:
# my_list = [1,2,3]
# for i in my_list:
#     print(i)

# iterator = iter(my_list)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


#Используеться:
class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max = max_number
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.max:
            raise StopIteration
        return self.i

count = Counter(10)
for i in count:
    print(i)


#Аналог:
print(range(5,10))



#Создание об'єкта для разбора без создания класса:
def raise_to_the_degrees(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number**i
        i += 1

res = raise_to_the_degrees(2,10)
print(res)



def helper(work):
    work_in_memory = work
    def helper(work):
        return f"I will help you with your {work_in_memory}. Afterwards I will help you with {work}"
    return helper
helper = helper("homework")
print(helper("cleaning"))
print(helper("driving"))



def checker(*exc_types):
    def checker(function):
        def checker(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
            except:
                print(f"We have problems {exc}")
            else:
                print(f"No problems. Result - {result}")
        return checker
    return checker

@checker(NameError, TypeError, SyntaxError)
def calculate(expression)
    return eval(expression)
calculate("2+2")














