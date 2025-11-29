users = {"Nick": "Adult","Kamilla": "Teenager","Carl": "Child","Anna": "Teenager"}

try:
    name = input("Enter name of user: ")

    age_group = users[name]

    print(f"User age group: {name}: {age_group}")

except KeyError:
    print("No user with this name found")

except BaseException as error:
    print("There is an error:", error)

else:
    print("Everything is fine")


