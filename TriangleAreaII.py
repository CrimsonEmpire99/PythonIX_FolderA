print('Triangle ABC')
print("Note: If the Semi-perimeter or any other side of the triangle is not a natural number, output values won't be clarified.")
print('.................................................................')
A = float(input('Enter value for A = '))
B = float(input('Enter value for B = '))
C = float(input('Enter value for C = '))
print("-----------------------------------------------------------------")
import math
S = (A+B+C)/2
print('_________________________________________________________________')
if (A+B <= C or B+C <= A or C+A <= B):
  print("ABC is not a triangle")
  print('.................................................................')
elif (A==B==C):
  print('ABC is an Equilateral triangle')
  area = (A**2)*((math.sqrt(3))/4)
  H = (2*area)/B
  print(f'Area of the Equilateral triangle ABC = {area} = ({A**2}/4)x√3 = {(A**2)/4}√3')
  print(f'Perimeter of the Equilateral triangle ABC = {2*S}')
  print(f'Height of the Equilateral triangle ABC = {H} = {A/2} x √3')
  print('..............................................................')
elif (A==B or B==C or C==A):
  print('ABC is an Isosceles Triangle')
  E = A if (A==B or A==C) else B if (B==C or B==A) else C
  U = A if (B==C) else B if (A==C) else C
  area = (U/4)*(math.sqrt(4*E**2 - U**2))
  H = (2*area)/B
#===============================================================================
  if isinstance(S, float) and S.is_integer() and A.is_integer() and B.is_integer() and C.is_integer():
      given_value = 4*E**2 - U**2
      y = 1
      while True:
        x = math.sqrt(given_value / y)
          
        if x.is_integer():
            break
                                
        y += 1
      print(f'Area of the Isosceles triangle ABC = {area} = {(U/4)*x} x √{y}')
      print(f'Height of the Isosceles triangle ABC = {H} = ({x} x √{y})/2')
#===============================================================================
  else:
    print(f"Area of the Isosceles triangle ABC = {area} = {U/4}√{4*E**2 - U**2}")
    print(f'Height of an Isosceles triangle ABC = {H} = 1/2 x √{4*E**2 - U**2}')
  print(f'Perimeter of Isosceles triangle ABC = {2*S}')
  print('.................................................................')
else:
  print('ABC is a Scalene Triangle')
  area = math.sqrt(S*(S-A)*(S-B)*(S-C))
  H = (2*area)/B
#===============================================================================
  if isinstance(S, float) and S.is_integer() and A.is_integer() and B.is_integer() and C.is_integer():
    given_value = S*(S-A)*(S-B)*(S-C)
    y = 1
    while True:
      x = math.sqrt(given_value / y)

      if x.is_integer():
        break

      y += 1

    print(f'Area of triangle ABC = {area} = {x}√{y}')
    print(f'Height of triangle ABC = {H} = ({x}/{B})√{y} = ({x/B})√{y}')
#===============================================================================
  else:
    print(f'Area of triangle ABC = {area}')
    print(f'Height of triangle ABC = {H}')
  print(f'Perimeter of triangle ABC = {2*S}')
  print('.................................................................')
