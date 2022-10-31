def calculate_money(salary: int, spend: int, month: int, increase: float) -> int:
    need_money = 0

    for current_month in range(month):
        if current_month >= 1:
            month_spend = spend * (1 + increase)
            spend = month_spend
        else:
            month_spend = spend

        waste = month_spend - salary
        need_money += waste

    return int(need_money)


if __name__ == '__main__':
    result = calculate_money(5000, 6000, 10, 0.03)
    print(result)
