# Function For Grade
def Grade(Sub) :
  if Sub>=80 and Sub<=100 :
    return "A+"
  elif Sub>=70 and Sub<=79 :
    return "A"
  elif Sub>=60 and Sub<=69 :
    return "A-"
  elif Sub>=50 and Sub<=59 :
    return "B"
  elif Sub>=40 and Sub<=49 :
    return "C"
  elif Sub>=33 and Sub<=39 :
    return "D"
  elif Sub>=0 and Sub<=32 :
    return "F"

# Function For Grade Point
def GradePoint(Sub) :
  if Sub>=80 and Sub<=100 :
    return 5
  elif Sub>=70 and Sub<=79 :
    return 4
  elif Sub>=60 and Sub<=69 :
    return 3.5
  elif Sub>=50 and Sub<=59 :
    return 3
  elif Sub>=40 and Sub<=49 :
    return 2
  elif Sub>=33 and Sub<=39 :
    return 1
  elif Sub>=0 and Sub<=32 :
    return 0

# Input Section
Bangla = int(input("Enter Your Marks On Bangla : "))
English = int(input("Enter Your Marks On English : "))
Math = int(input("Enter Your Marks On Math : "))
Religion = int(input("Enter Your Marks On Religion : "))
Science = int(input("Enter Your Marks On Science : "))
Sociology = int(input("Enter Your Marks On Sociology : "))

# Grade Print Section

print("\n\nIn Bangla Your Grade Is :",Grade(Bangla))
print("In English Your Grade Is :",Grade(English))
print("In Math Your Grade Is :",Grade(Math))
print("In Religion Your Grade Is :",Grade(Religion))
print("In Science Your Grade Is :",Grade(Science))
print("In Sociology Your Grade Is :",Grade(Sociology))

# Grade Point Print Section

print("\n\nIn Bangla Your Grade Point Is :",GradePoint(Bangla))
print("In English Your Grade Point Is :",GradePoint(English))
print("In Math Your Grade Point Is :",GradePoint(Math))
print("In Religion Your Grade Point Is :",GradePoint(Religion))
print("In Science Your Grade Point Is :",GradePoint(Science))
print("In Sociology Your Grade Point Is :",GradePoint(Sociology))

# Total Grade Point

TotalInPoint = (GradePoint(Bangla)+GradePoint(English)+GradePoint(Math)+GradePoint(Religion)+GradePoint(Science)+GradePoint(Sociology))/6

if GradePoint(Bangla)>0 and GradePoint(English)>0 and GradePoint(Math)>0 and GradePoint(Religion)>0 and GradePoint(Science)>0 and GradePoint(Sociology)>0 :
  print("\n\nYour Total Grade Point Is :",f'{TotalInPoint:.2f}')

else :
    print("\n\nYour Grade Point Cannot Be Count Cause You Fail In Exam")

# Total Grade Result

if GradePoint(Bangla)>0 and GradePoint(English)>0 and GradePoint(Math)>0 and GradePoint(Religion)>0 and GradePoint(Science)>0 and GradePoint(Sociology)>0 :
  if TotalInPoint==5 :
    print("And Your Total Grade Result Is : A+")
  elif TotalInPoint>=4 and TotalInPoint<=4.99 :
    print("And Your Total Grade Result Is : A")
  elif TotalInPoint>=3.50 and TotalInPoint<=3.99 :
    print("And Your Total Grade Result Is : A-")
  elif TotalInPoint>=3 and TotalInPoint<=3.49 :
    print("And Your Total Grade Result Is : B")
  elif TotalInPoint>=2 and TotalInPoint<=2.99 :
    print("And Your Total Grade Result Is : C")
  elif TotalInPoint>=1 and TotalInPoint<=1.99 :
    print("And Your Total Grade Result Is : D")
