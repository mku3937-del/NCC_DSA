def max_num (a,y,z):
    if a > y and z:

        return a

    elif y > a and z:

        return y

    elif z > a and y:

        return z

a = float(input("enter a:"))

y = float(input("enter y:"))

z = float(input("enter z:"))


largest_number = max_num (a,y,z)


print(f"largest number is **{max_num}**")