total_tuition = 0
student_count = 0

file = open("students.txt", "r")

while True:
    name = file.readline().strip()
    if not name:
        break

    district = file.readline().strip()
    credits = int(file.readline().strip())

    if district.upper() == "I":
        cost_per_credit = 250.00
    else:
        cost_per_credit = 500.00

    tuition = credits * cost_per_credit

    total_tuition += tuition
    student_count += 1

    print(f"{name:<10} Credits: {credits:<5} Tuition: ${tuition:>10.2f}")

file.close()

print(f"\nTotal Tuition: ${total_tuition:.2f}")
print(f"Number of Students: {student_count}")
