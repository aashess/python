
def func(first,second):
    # print(first.title())
    # print(second.title())
    """Hellow this my first function with doc string."""
    if first == "" or second == "":
        return "You didn't prove any value."

    format1 = first.title()
    format2 = second.title()
    return f"Resutl: {format1} {format2}"


print(func(input("What is Your First Name: "),input("What is your Last Name: ")))
# variable = func(first="aashish",second="Jha")

# print(f"{variable}")
# print(f"{len(variable)}")