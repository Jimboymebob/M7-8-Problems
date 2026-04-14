start = int(input("Enter start value: "))
stop = int(input("Enter stop value: "))
increment = int(input("Enter increment value: "))

if increment == 0:
    print("Increment cannot be zero. Setting to 1.")
    increment = 1 

print("\n--- First Loop (Simple) ---")
current = start
while current <= stop:
    print(current)
    current += increment
  
print("\n--- Second Loop (Direction-Aware) ---")
i = start
while (increment > 0 and i <= stop) or (increment < 0 and i >= stop):
    print(i)
    i += increment
