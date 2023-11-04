def qan_tic():  # (1)

    tic = "QAN.AX"  # (2)

    # return tic            # (4)     <-- Function will exit here!

    print(tic)  # (3)     <-- Will not be printed!


# Call the function

res = qan_tic()  # (5b)

print(res)  # --> QAN.AX

def even(list):
    even_list = []
    for num in list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            continue
    return even_list
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]

print(even(list1))

lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]
square = [v**2 for v in lst if v**2 > 150]
print(square)

numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
unique = set(n for n in numbers if n % 2 == 0 and n)
print(unique)