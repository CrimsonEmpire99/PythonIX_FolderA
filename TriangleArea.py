A = float(input('Enter A = '))
B = float(input('Enter B = '))
C = float(input('Enter C = '))
import math
S = (A+B+C)/2
if (A+B < C or B+C < A or C+A < B): print("ABC is not a triangle")
else:
  area = math.sqrt(S*(S-A)*(S-B)*(S-C))
  H = (2*area)/B
  print(f'semi perimeter = {S}')
  print(f'area of triangle ABC = {area}')
  print(f'perimeter of triangle ABC = {2*S}')
  print(f'Height of triangle ABC = {H}')
