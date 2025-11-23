# try:
#     print(5/0)
# except (NameError, SyntaxError):
#    print("Та нельзя на 0 делить")
# except ZeroDivisionError:
#      print("123")
# except BaseException as error:
#     print("Error")
# else:
#     print("Все ок!")
# finally:
#     pass


# class NotStringError(Exception):
#     def __str__(self):
#         return f"Sorry, we can't work with, we need string"
#
#
# def checker(var1)
#     if type(var1) != str:
#         raise NotStringError()
#     else:
#         print("Ok!")
#
# try:
#     checker(1)
# except BaseException as err:
#     print(err)




import warnings

warnings.warm("Warning, no code here", SyntaxWarning)