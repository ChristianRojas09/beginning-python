# beginning-python
This repository shows my first python projects

# at this point (10-11-2019) I have been coding python for about two weeks
# Here are a few projects I have been working on:

# This is a pay calculator that also calculates overtime using a function and if else statements

h = int(input("Enter Hours: "))
r = float(input("Enter Rate: "))

def computepay(h,r):
    if h <= 40:
        p = h*r
    else:
        p = (h - 40) * 1.5 * r + (40 * r)
        return p
p = computepay(h,r)
print(p)

