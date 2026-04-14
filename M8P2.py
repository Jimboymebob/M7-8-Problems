start = int(input("Enter start value: "))
stop = int(input("Enter stop value: "))
increment = int(input("Enter increment value: "))

if increment == 0:
    increment = 1 

i = start

while (increment > 0 and i <= stop) or (increment < 0 and i >= stop):
    print(i)
    i += increment
