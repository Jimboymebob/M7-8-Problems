count = 0

answer = input("Do you want to enter student data? (Yes/No): ")

while answer.lower() == "yes":
    name = input("Enter last name: ")
    score1 = float(input("Enter first exam score: "))
    score2 = float(input("Enter second exam score: "))

    average = (score1 + score2) / 2

    print(f"{name:<10} Average Score: {average:.2f}")

    count += 1

    answer = input("Do you want to enter another student? (Yes/No): ")

print(f"\nNumber of students entered: {count}")
