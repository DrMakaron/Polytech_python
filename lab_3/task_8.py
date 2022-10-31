def calculate_lifetime(money_capital: int, salary: int, spend: int, increase: float) -> int:
    month = 0

    while money_capital > 0:
        if month >= 1:
            month_spend = spend * (1 + increase)
            spend = month_spend
        else:
            month_spend = spend

        if money_capital - month_spend > 0:
            month += 1
        else:
            break

        money_capital -= month_spend
        money_capital += salary

    return month


if __name__ == '__main__':
    result = calculate_lifetime(10000, 5000, 6000, 0.05)
    print(result)
