a = float(input())
b = int(input())
print("{:.0f}".format(a*(b%10)))
print("{:.0f}".format(a*(b%(10**2)-(b%10**1))/(10**1)))
print("{:.0f}".format(a*(b%(10**3)-(b%10**2))/(10**2)))
print("{:.0f}".format(a*b))