# Lecture 2
object = '''John said: "Let's learn python together"'''
print(object)

a1 = 1

y = 'abc'.upper()
print(y)

Height = 30.5
Width = 33
Length = 56
Volume = Height * Width * Length
print(f"The volume of the box is {Volume}")

lst = [1, "string", True, None, True]
lst.remove(True)
print(lst)

line = 'From firstname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020'
domain = line.split()[1].split('@')[1]