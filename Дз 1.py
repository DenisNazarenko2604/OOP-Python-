#перше завдання:

name = input("Ваше ім'я: ")
age = input("Ваш вік: ")

print(f"Привіт {name}, тобі {age} років !")


#Друге завдання:

age = int(input("Ваш вік?"))
if age < 18:
    print("вхід заборонено")
elif age >= 18:
    print("вхід дозволено")



# четверте завдання:


num1 =  int(input("Введить перше число"))
num2 =  int(input("Введить друге число"))

if num1 <= num2:
    for i in range(num1, num2 + 1):
        print(i)
else:
    for i in range(num1, num2 - 1, -1):
        print(i)

