#Ratio & Perimeter to Area
a = float(input('Enter the First Term (SideA) = '))
b = float(input('Enter the Second Term (SideB) = '))
c = float(input('Enter the Third Term (SideC) = '))
P = float(input("Enter Perimeter = "))
import math
x = P/(a+b+c)
A=a*x
B=b*x
C=c*x
S = P/2
if (A+B <= C or B+C <= A or C+A <= B): print("ABC is not a triangle")
else:
  area = math.sqrt(S*(S-A)*(S-B)*(S-C))
  H = (2*area)/B
  print('Sides A,B,C =', [A,B,C])
  print(f'semi perimeter = {S}')
  print(f'area of triangle ABC = {area}')
  print(f'perimeter of triangle ABC = {P}')
  print(f'Height of triangle ABC = {H}')
