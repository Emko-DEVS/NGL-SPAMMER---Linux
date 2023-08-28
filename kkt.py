inputx = input("Number>> ")

try:
    # Validate that the input contains only allowed characters
    if all(c.isdigit() or c.isspace() or c in "+-*/()" for c in inputx):
        result = eval("2 + {}".format(inputx))
        print(result)
    else:
        print("Invalid input")
except:
    print("Error evaluating expression")