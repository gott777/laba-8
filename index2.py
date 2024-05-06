num = int(input())
def reverse_number(num):
    num = str(num)
    return num[::-1]
print(reverse_number(num))


num2 = int(input())
def is_palindrome(num2):
    num2reverse = str(num2)
    num2reverse = num2reverse[::-1]
    num2 = str(num2)
    if num2reverse==num2:
        return 'число является полиндромом'
    else:
        return 'число не является полиндромом'
print(is_palindrome(num2))

def process_numbers(numbers):
    reversed_numbers = []
    for num in numbers:
        num_str = str(num)
        reversed_num_str = num_str[::-1]
        reversed_num = int(reversed_num_str)
        if num == reversed_num:
            print(f"{num} является палиндромом")
        reversed_numbers.append(reversed_num)
    return reversed_numbers

# Пример использования
numbers = [123, 456, 121, 1331,11]
reversed_numbers = process_numbers(numbers)
print("Перевернутые числа:", reversed_numbers)