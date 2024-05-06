def calculate_final_amount(principal, interest_rate, years):
    # Преобразование процентной ставки в десятичную дробь
    interest_rate_decimal = interest_rate / 100

    # Расчет итоговой суммы по формуле сложного процента
    final_amount = principal * (1 + interest_rate_decimal) ** years

    return final_amount

def main():
    # Ввод данных от пользователя
    principal = float(input("Введите начальную сумму: "))
    interest_rate = float(input("Введите процентную ставку (%): "))
    years = int(input("Введите количество лет: "))

    # Расчет и вывод итоговой суммы
    final_amount = calculate_final_amount(principal, interest_rate, years)
    print("Итоговая сумма после", years, "лет:", final_amount)
main()