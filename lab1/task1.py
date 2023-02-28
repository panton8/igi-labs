print("Hello, world")


def operation_with_nums(num1, num2, operation):
    operation = operation.lower()
    match operation:
        case "add":
            return num1 + num2
        case "sub":
            return num1 - num2
        case "mul":
            return num1 * num2
        case "div":
            if num2 != 0:
                return num1 / num2
            else:
                return "Infinity"
        case _:
            return "Invalid operation. Check your input"


def even_list(list_of_nums):
    return [num for num in list_of_nums if num % 2 == 0]

print("Enter the num")
num1 = int(input())
print(operation_with_nums(num1, 2, "add"))
print(operation_with_nums(8, 8, "mul"))
print(operation_with_nums(1, 0, "div"))
print(operation_with_nums(0, 0, "Anton"))
print(even_list([num for num in range(14, 27)]))
