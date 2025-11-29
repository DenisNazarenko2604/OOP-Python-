import colorama
import inspect

mylist = []
for method in dir(mylist):
    print(method)


print(inspect.ismodule(colorama))
print(inspect.isclass(colorama))
print(inspect.isfunction(colorama))
print(inspect.getmodule(colorama))
print(inspect.getmodule(list))



 help(colorama)

 def test():
     pass

 class Human:
     pass

 color = colorama
 test_f = test
 nick = Human

 print(colorama.__name__)
 print(color.__name__)
 print(test.__name__)
 print(test_f.__name__)
 print(Human.__name__)
 print(nick.__name__)
 print(__name__)
 print(type(5))




sig = inspect.signature(colorama.Fore.__init__)
for param in sig.parameters.values():
    print(param.name, param.default)