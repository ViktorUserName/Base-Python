phone = 1200
money = 200


def days(N, k):
    week = 6 * k

    full_weeks = N // week
    amount = N % week

    days_needed = full_weeks * 7

    if amount > 0:
        while amount > 0:
            days_needed += 1
            amount -= k

    return print(days_needed)




days(phone, money)