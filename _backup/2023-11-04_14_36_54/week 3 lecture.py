
# Week 3

hrs = input('Hours Worked:')
hrs = float(hrs)

if hrs > 35:
    pay = (51.45 * hrs) + (hrs - 35) * 88.9
    print(pay)
else:
    pay = 51.45 * hrs
    print(pay)

for a in range(1, 1000):
    print(a)

x = [5, 4, 6, 78, 6]

numbers = [3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15]
max = 0

for a in numbers:
    if a > max:
        max = a
        a += 1
    else:
        a += 1

for a in [1, 2, 3]:
    for b in [1, 2, 3]:
        if a <= b:
            print(a, b)