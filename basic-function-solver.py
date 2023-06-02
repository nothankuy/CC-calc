while True:
    function_letter = input("Enter the function letter: ")

    function_letters = [function_letter]

    function_number = int(input("Enter the function number: "))

    question1 = int(input("Enter question number 1: "))

    question2 = int(input("Enter question number 2: "))

    use_another = input("Do you want to use another function letter? (y/n) ")

    if use_another.lower() == "y":
        function_letter2 = input("Enter the other function letter: ")
        function_letters.append(str(function_number))
        other_func_question = input("Do you want to put the other function letter at Question number 1 or Question number 2 (1/2): ")
        if other_func_question == "1":
            question1 *= function_number
        elif other_func_question == "2":
            question2 *= function_number
        operation1 = input("What is the first operation (+, -, *, /): ")
        operation2 = None
    else:
        operation1 = input("What is the first operation (+, -, *, /): ")
        operation2 = input("What is the second operation (+, -, *, /): ")

    if operation2:
        if operation1 == "+":
            result = question1 + question2
        elif operation1 == "-":
            result = question1 - question2
        elif operation1 == "*":
            result = question1 * question2
        elif operation1 == "/":
            result = question1 / question2

        if operation2 == "+":
            result += function_number
        elif operation2 == "-":
            result -= function_number
        elif operation2 == "*":
            result *= function_number
        elif operation2 == "/":
            result /= function_number
    else:
        if operation1 == "+":
            result = question1 + question2
        elif operation1 == "-":
            result = question1 - question2
        elif operation1 == "*":
            result = question1 * question2
        elif operation1 == "/":
            result = question1 / question2

    print(f"The result is: {result}\n")

