num1=int(input("Enter number1: "))
num2=int(input("Enter number2: "))

operator=input("Enter operator like (+ - * / % // **): ")

match operator:
    case "+":
        print("sum is ",num1+num2)
    case "-":
        print("Difference is ",num1-num2)
    case "*":
        print("Multiplication is ",num1*num2)
    case "/":
        print("Divison is ",num1/num2)
    case "**":
        print("Square is ",num1**num2)
    case "%":
        print("Modulo is ",num1%num2)
    case "//":
        print("Floor divison is ",num1//num2)
    case _:
        print("Enter a valid operator")