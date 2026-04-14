total_bonus = 0

file = open("employees.txt", "r")

while True:
    name = file.readline().strip()
    if not name:
        break

    salary = float(file.readline().strip())

    if salary >= 100000:
        rate = 0.20
    elif salary >= 50000:
        rate = 0.15
    else:
        rate = 0.10

    bonus = salary * rate
    total_bonus += bonus

    print(f"{name:<10} Salary: ${salary:>10.2f} Bonus: ${bonus:>10.2f}")

file.close()

print(f"\nTotal Bonuses Paid: ${total_bonus:.2f}")
