total = 0
count = 0

file = open("orders.txt", "r")

while True:
    item = file.readline().strip()
    if not item:
        break

    quantity = int(file.readline().strip())
    price = float(file.readline().strip())

    extended = quantity * price

    total += extended
    count += 1

    print(f"{item:<10} Qty: {quantity:<5} Price: ${price:>8.2f} Total: ${extended:>10.2f}")

file.close()

average = total / count if count > 0 else 0

print(f"\nTotal Sales: ${total:.2f}")
print(f"Number of Orders: {count}")
print(f"Average Order: ${average:.2f}")
