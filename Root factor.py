import math
given_value = float(input("Enter the given value: "))
y = 1
while True:
  x = math.sqrt(given_value / y)

  if x.is_integer():
    break

  y += 1

print("x =", x)
print("y =", y)
