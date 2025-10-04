# import art

# title case
def format_name(f_name, l_name):
    """Docstring, it can be multiline
    like this"""
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    # print(f"{formatted_f_name} {formatted_l_name}")
    return f"Result: {formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))

# formatted_string = format_name('angela', 'YU')
# print(formatted_string)

# # or
# print(format_name('angela', 'YU'))
#
# output = len("Angela")




def function_1(text):
    return text + text

def function_2(text):
    return text.title() # dont forget the ()

output = function_2(function_1("hello"))
print(output)



# coding exercise - leap year
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(is_leap_year(2020))


# calculator
def add (n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# print(operations["*"](4, 8))

def calculator():
    # print(art.logo)
    should_accumulate = True
    num1 = float(input("What is your first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = (input("Pick an operation: "))
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")


        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator() # recursion, goes to very beginning

calculator()
