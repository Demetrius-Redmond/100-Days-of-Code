def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add, 
    "-" : subtract, 
    "*" : multiply, 
    "/" : divide,  
}
def calculator():
    finished = False


    while not finished:
        num1 = float(input("What's the first number?: "))
        for x in operations:
            print(x)
        user_op = input("Which operator would you like to use?: ")
        num2 = float(input("What's the next number?: "))

        answer = 0
        
        for x in operations:
            if x == user_op:
                answer = operations[x](num1, num2)

        print(f"{num1} {user_op} {num2} = {answer}")
        keep_going = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
        if keep_going == "y":
            user_op = input("Which operator would you like to use?: ")
            num3 = float(input("What's the next number?: "))
            answer_2 = operations[user_op](answer, num3)
            print(f"{answer} {user_op} {num3} = {answer_2}")
        else:
            finished = True
            print("Goodbye!")
            calculator()   
            
calculator() 